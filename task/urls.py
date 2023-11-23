from django.urls import path

from task.views import (
    index, TaskTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasktypes/",
        TaskTypeListView.as_view(),
        name="tasktype-list",
    ),
]

app_name = "task"
