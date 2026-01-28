from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import TaskList 
from .form import TaskForm


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


@login_required
def task_view(request):
    """
    Displays list of tasks
    """
    queryset = TaskList.objects.filter(user=request.user)

    context = {
        'tasks': queryset
    }

    return render(request, 'task/task_view.html', context)


@login_required
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


@login_required
def delete_task(request, pk):
    """
    Delete a task
    """
    task = get_object_or_404(TaskList, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_view')


@login_required
def task_edit(request, task_id):
    task = get_object_or_404(TaskList, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task/task_add.html', {'form': form, 'task': task})
