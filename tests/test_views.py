from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime

from task.models import TaskType, Task, Position


TASKTYPE_URL = reverse("task:tasktype-list")
TASK_URL = reverse("task:task-list")
POSITION_URL = reverse("task:position-list")
WORKER_URL = reverse("task:worker-list")


class PublicTests(TestCase):
    def test_tasktype_login_required(self):
        res = self.client.get(TASKTYPE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_task_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_position_login_required(self):
        res = self.client.get(POSITION_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_worker_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTypeTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test position")
        self.user = get_user_model().objects.create_user(
            username="test", password="test321", position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_tasktype(self):
        TaskType.objects.create(name="Homework")
        TaskType.objects.create(name="Meeting")
        response = self.client.get(TASKTYPE_URL)
        tasktype_list = TaskType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tasktype_list"]), list(tasktype_list))
        self.assertTemplateUsed(response, "task/tasktype_list.html")


class PrivateTaskTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test position")
        self.user = get_user_model().objects.create_user(
            username="test", password="test321", position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        Task.objects.create(
            name="Task 1",
            description="Description 1",
            deadline=datetime.now().date(),
            priority="High",
            task_type=TaskType.objects.create(name="Homework"),
        )
        Task.objects.create(
            name="Task 2",
            description="Description 2",
            deadline=datetime.now().date(),
            priority="Medium",
            task_type=TaskType.objects.create(name="Meeting"),
        )

        response = self.client.get(TASK_URL)
        task_list = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]), list(task_list))
        self.assertTemplateUsed(response, "task/task_list.html")

    def test_search_form_initial_value(self):
        response = self.client.get(TASK_URL)
        form = response.context["search_form"]

        self.assertEqual(form.initial["name"], "")


class PrivatePositionTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test position")
        self.user = get_user_model().objects.create_user(
            username="test", password="test321", position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_positions(self):
        Position.objects.create(name="Manager")
        Position.objects.create(name="Supervisor")

        response = self.client.get(POSITION_URL)
        position_list = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["position_list"]), list(position_list))
        self.assertTemplateUsed(response, "task/position_list.html")


class PrivateWorkerTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test position")
        self.user = get_user_model().objects.create_user(
            username="test", password="test321", position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_workers(self):
        get_user_model().objects.create(
            username="user1",
            first_name="first1",
            last_name="last1",
            email="user1@example.com",
            position=self.position,
        )
        get_user_model().objects.create(
            username="user2",
            first_name="first2",
            last_name="last2",
            email="user2@example.com",
            position=self.position,
        )

        response = self.client.get(WORKER_URL)
        worker_list = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["worker_list"]), list(worker_list))
        self.assertTemplateUsed(response, "task/worker_list.html")
