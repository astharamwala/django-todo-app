from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    """
        Login for users.
    """
    template_name = 'base/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin, ListView):
    """
        List all the tasks.
    """
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/tasks.html'


class TaskDetail(LoginRequiredMixin, DetailView):
    """
        Display task details.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    """
        Create task.
    """
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
        Update a task.
    """
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    """
        Delete a task.
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
