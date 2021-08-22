from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .serializers import ContextSerializer
from .models import Context, Task


def formatData(contexts):
    context_name = Context.context_name
    res = []
    for i, context in enumerate(contexts):
        res.append({
            "name": context_name[context["name"]],
            "id": i
        })
    return(res)


@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': '/all-tasks/',
        'View Task': '/task/<str:pk>/',
        'Add Task': '/add-task/',
        'Update Task': '/update-task/<str:pk>/',
        'Delete Task': '/delete-task/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def contextList(request):
    contexts = Context.objects.all()
    serializer = ContextSerializer(contexts, many=True)
    formatData(serializer.data)
    return Response(formatData(serializer.data))


@api_view(['GET'])
def viewTask(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Deleted")
