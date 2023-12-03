from django.test import TestCase
from django.contrib.auth import get_user_model

from task.models import Position
from task.forms import TaskTypeSearchForm, WorkerForm, PositionSearchForm


class FormsTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.user_model = get_user_model()
        self.worker = self.user_model.objects.create_user(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="test@user.com",
            position=self.position,
        )

    def test_task_type_search_form_valid(self):
        form_data = {"name": "TaskType"}
        form = TaskTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_form_valid(self):
        form_data = {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "new@user.com",
            "position": self.position.id,
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        form = WorkerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_form_invalid(self):
        form_data = {
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "new@user.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        form = WorkerForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_position_search_form_valid(self):
        form_data = {"name": "Manager"}
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
