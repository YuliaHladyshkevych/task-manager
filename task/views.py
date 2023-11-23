from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from task.models import TaskType, Task, Position, Worker


def index(request):
    """View function for the home page of the site."""

    num_task_types = TaskType.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_task_types": num_task_types,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_visits": num_visits + 1,
    }

    return render(request, "task/index.html", context=context)


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "tasktype_list"
    template_name = "task/tasktype_list.html"
    paginate_by = 5

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(TaskTypeListView, self).get_context_data(**kwargs)
    #     name = self.request.GET.get("name", "")
    #     context["search_form"] = TaskTypeSearchForm(initial={
    #         "name": name
    #     })
    #
    #     return context
    #
    # def get_queryset(self):
    #     queryset = TaskType.objects.all()
    #     form = TaskTypeSearchForm(self.request.GET)
    #
    #     if form.is_valid():
    #         return queryset.filter(name__icontains=form.cleaned_data["name"])
    #
    #     return queryset


