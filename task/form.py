from django import forms
from .models import TaskList


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:
        model = TaskList
        fields = ['title', 'description', 'due_date',
                  'priority', 'status', 'category']
