from . import views
from django.urls import path

urlpatterns = [
    path('', 
        views.task_view, name='task_view'),
]
