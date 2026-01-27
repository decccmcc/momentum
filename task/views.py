from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import TaskList
from .form import TaskForm


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

def task_add(request):
    """
    Create a new task
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_view')
    else:
        form = TaskForm()
    
    context = {
        'form': form
    }
    return render(request, 'task/task_add.html', context)