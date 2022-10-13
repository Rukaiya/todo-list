from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
]
