from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task


# Create your views here.
class TaskList(ListView):
    """
        List all the tasks.
    """
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/tasks.html'


class TaskDetail(DetailView):
    """
        Display task details.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    """
        Create task.
    """
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    """
        Update a task.
    """
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    """
        Delete a task.
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
