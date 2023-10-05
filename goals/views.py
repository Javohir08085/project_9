from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Goal
from django.urls import reverse_lazy
# Create your views here.


class GoalsList(ListView):
    model = Goal
    template_name = 'config/home.html'
    context_object_name = 'goals'


class GoalDelete(DeleteView):
    model = Goal
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)