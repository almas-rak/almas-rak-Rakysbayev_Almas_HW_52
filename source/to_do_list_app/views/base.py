from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_list_app.models import Todo


def index_view(request: WSGIRequest):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context=context)
