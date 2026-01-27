from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TaskList


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

def task_view(request):
    """
    Displays list of tasks
    """
    queryset = TaskList.objects.all()

    context = {
        'tasks': queryset
    }

    return render(request, 'task/task_view.html', context)

