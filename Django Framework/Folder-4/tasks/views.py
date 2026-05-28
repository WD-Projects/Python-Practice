# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib import messages


# def sample(request):
#     context = {"name": "Zayed"}
#     return render(request, "tasks/tasks.html", context)


# def unknown(request):
#     messages.success(request, "All good!")
#     return HttpResponse("OK")


from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Task
from .forms import TaskForm

from django.http import HttpResponse, HttpRequest


# 1. LIST - Show all tasks
def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, "tasks/task_list.html", {"tasks": tasks})


class TaskListView2(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"


# 2. DETAIL - Show single task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


# 3. CREATE - Add new task
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "action": "Create"})


class TaskCreateView2(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_message = "Task successfully created!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(
            request, "tasks/task_form.html", {"form": form, "action": "Create"}
        )

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect("task_detail", pk=task.pk)
        return render(
            request, "tasks/task_form.html", {"form": form, "action": "Create"}
        )


# 4. UPDATE - Edit existing task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect("task_detail", pk=task.pk)
    else:
        #This line:
        #     form = TaskForm(instance=task)
        # inside GET request:
        # else:
        #     form = TaskForm(instance=task)
        # pre-fills the form with existing data.
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "action": "Update", "task": task},
    )


# 5. DELETE - Remove task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" deleted successfully!')
        return redirect("task_list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})
