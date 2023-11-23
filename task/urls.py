from django.urls import path

from task.views import (
    index, TaskTypeListView, TaskListView, PositionListView, WorkerListView, TaskDetailView, toggle_assign_to_task,
    WorkerDetailView, TaskTypeCreateView, TaskTypeUpdateView, TaskTypeDeleteView, TaskCreateView, TaskUpdateView,
    TaskDeleteView, WorkerCreateView, WorkerUpdateView, WorkerDeleteView, PositionCreateView, PositionUpdateView,
    PositionDeleteView, MarkTaskAsDoneView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasktypes/",
        TaskTypeListView.as_view(),
        name="tasktype-list",
    ),
    path(
        "tasktypes/create/",
        TaskTypeCreateView.as_view(),
        name="tasktype-create",
    ),
    path(
        "tasktypes/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="tasktype-update",
    ),
    path(
        "tasktypes/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="tasktype-delete",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path('tasks/<int:pk>/mark-as-done/', MarkTaskAsDoneView.as_view(), name="mark-task-done"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "positins/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create",
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
]

app_name = "task"
