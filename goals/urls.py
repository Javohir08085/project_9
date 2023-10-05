from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoalsList.as_view(), name='goalslist'),
    path('delete/<int:pk>', views.GoalDelete.as_view(), name='goaldelete'),
]
