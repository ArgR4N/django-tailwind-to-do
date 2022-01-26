from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from .models import toDo


def toDoS(req):
    toDoList = toDo.objects.all().order_by('-id')
    return render(req, 'toDoApp/toDoView.html', {'toDoList':toDoList})

@require_http_methods(['POST'])
def add_toDo(req):
    newToDo = None
    title = req.POST.get('title', '')
    if title:
        newToDo = toDo.objects.create(title=title)

    return render(req, 'toDoApp/partials/toDoItem.html', {'toDo':newToDo})


@require_http_methods(['DELETE'])
def delete_toDo(req, pk):
    forDeleteToDo = toDo.objects.get(pk=pk)
    forDeleteToDo.delete()
    return HttpResponse()

@require_http_methods(['PUT'])
def done_toDo(req, pk):
    doneToDo = toDo.objects.get(pk=pk)
    doneToDo.is_done = not doneToDo.is_done
    doneToDo.save()

    return render(req, 'toDoApp/partials/toDOItem.html', {'toDo':doneToDo})