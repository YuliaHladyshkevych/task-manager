from django.urls import path

from task.views import (
    index, TaskTypeListView, TaskListView, PositionListView,
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
    path(
        "positins/",
        PositionListView.as_view(),
        name="position-list",
    ),
]

app_name = "task"
