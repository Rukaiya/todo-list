from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
