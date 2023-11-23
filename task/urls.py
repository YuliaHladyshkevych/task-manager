from django.urls import path

from task.views import (
    index, TaskTypeListView, TaskListView, PositionListView, WorkerListView, TaskDetailView, toggle_assign_to_task,
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
        "tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"
    ),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path(
        "positins/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
]

app_name = "task"
