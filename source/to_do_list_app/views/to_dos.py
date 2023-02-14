from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_list_app.models import Todo


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'add_todo.html')
    print(request.POST)
    todo_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date_of_completion': request.POST.get('date_of_completion')
    }
    if todo_data['date_of_completion'] == "":
        todo_data['date_of_completion'] = None
    todo = Todo.objects.create(**todo_data)

    return redirect(f'/todo/?pk={todo.pk}')


def detail_view(request):
    todo_pk = request.GET.get('pk')
    todo = Todo.objects.get(pk=todo_pk)
    context = {'todo': todo}
    return render(request, 'todo.html', context=context)
