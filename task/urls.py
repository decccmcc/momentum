from . import views
from django.urls import path

urlpatterns = [
    path('add_task/', 
        views.task_add, name='task_add'),
    path('', 
        views.task_view, name='task_view'),
]
