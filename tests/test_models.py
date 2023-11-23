from datetime import datetime, date

from django.contrib.auth import get_user_model
from django.test import TestCase

from task.models import TaskType, Position, Task


class ModelsTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="test_tasktype")
        self.position = Position.objects.create(name="test_position")
        self.user = get_user_model().objects.create(
            username="test",
            password="test321",
            first_name="first",
            last_name="last",
            position=self.position
        )

        self.task = Task.objects.create(
            name="task",
            description="description",
            deadline=datetime.now().date(),
            is_completed=False,
            priority="low",
            task_type=self.task_type,
        )

        self.task2 = Task.objects.create(
            name="task2",
            description="description2",
            deadline=date(2022, 12, 23),
            is_completed=False,
            priority="low",
            task_type=self.task_type,
        )

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "test_tasktype")

    def test_task_str(self):
        self.assertEqual(str(self.task), "task")

    def test_position_str(self):
        self.assertEqual(str(self.position), "test_position")

    def test_worker_str(self):
        self.assertEqual(str(self.user), "test (first last)")

    def test_check_time(self):
        self.assertTrue(self.task.completed_before_deadline())
        self.assertFalse(self.task2.completed_before_deadline())
