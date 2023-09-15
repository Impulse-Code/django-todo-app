from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView,TaskDeleteView,TaskUpdateView,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
   path('login/',CustomLoginView.as_view(),name='login'),
   path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
   path('register/',RegisterPage.as_view(),name='register'),
   path('',TaskListView.as_view(),name='task_list'),
   path('task/<int:pk>',TaskDetailView.as_view(),name='task'),
   path('create-task/',TaskCreateView.as_view(),name='task-create'),
   path('task-update/<int:pk>',TaskUpdateView.as_view(),name='task-update'),
   path('task-delete/<int:pk>',TaskDeleteView.as_view(),name='task-delete')

]
