from django.http import HttpResponse

from .models import Task

from django.shortcuts import render

from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

# Create your views here.

def addTask(request):
    task1= request.POST['task']
    Task.objects.create(task=task1)
    return redirect('home')

def mark_as_done(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task1 = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task1.task = new_task
        get_task1.save()
        return redirect('home')

    else:
        context = {
            'get_task': get_task1,
        }
    return render(request,'edit_task.html', context)


def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

