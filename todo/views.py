from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo')


class TodoFinishView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.end_date = date.today()
        todo.save()
        return redirect('todo')
