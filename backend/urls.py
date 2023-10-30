from django.contrib import admin
from django.urls import path
from todo.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoFinishView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="todo/", permanent=False)),
    path('todo/', TodoListView.as_view(), name='todo'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='todo_delete'),
    path('finish/<int:pk>', TodoFinishView.as_view(), name='todo_finish')
]
