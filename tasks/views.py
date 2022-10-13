from django.urls import reverse_lazy
from django.views import generic
from .models import Task


# Create your views here.
class TaskList(generic.ListView):
    model = Task
    context_object_name = 'task_list'


class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreate(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
