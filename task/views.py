from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import TaskList, CATEGORY_CHOICES
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
    selected_category = request.GET.get('category', 'all')
    if selected_category == 'all':
        tasks = TaskList.objects.filter(user=request.user).order_by('due_date')
    else:
        tasks = TaskList.objects.filter(
            user=request.user, category=selected_category).order_by('due_date')
    context = {
        'tasks': tasks,
        'categories': CATEGORY_CHOICES,
        'selected_category': selected_category,
        'form': TaskForm(),
    }

    return render(request, 'task/task_view.html', context)


@login_required
def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_view')
        else:
            # form invalid → re-render task_view with errors
            tasks = TaskList.objects.filter(user=request.user)
            return render(request, 'task/task_view.html', {
                'form': form,
                'tasks': tasks,
                'categories': CATEGORY_CHOICES,
                'selected_category': 'all',
                'show_modal': True  # tells template to reopen modal
            })

    # GET request
    return redirect('task_view')


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
