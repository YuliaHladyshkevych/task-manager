from django.urls import path

from task.views import (
    index, TaskTypeListView, TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasktypes/",
        TaskTypeListView.as_view(),
        name="tasktype-list",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
]

app_name = "task"
