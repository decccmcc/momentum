from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRIORITY = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]
STATUS = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
]
CATEGORY_CHOICES = [
    ("work", "Work"),
    ("personal", "Personal"),
    ("home", "Home"),
]


class TaskList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(
        choices=PRIORITY, default='medium')
    status = models.CharField(choices=STATUS, default='pending')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default="personal"
    )

    class Meta:
        ordering = ['due_date', 'priority']

    def __str__(self):
        return self.title
