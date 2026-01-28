from . import views
from django.urls import path

urlpatterns = [

    path('',
         views.task_view, name='task_view'),
    path('add_task/',
         views.task_add, name='task_add'),
    path('delete_task/<int:pk>/',
         views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
]
