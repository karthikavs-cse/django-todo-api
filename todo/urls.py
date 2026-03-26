from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserProfileView, ItemListCreateView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('user/<int:pk>/', UserProfileView.as_view()),

    # ✅ ADD THIS
    path('items/', ItemListCreateView.as_view()),
]