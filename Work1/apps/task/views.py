from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Done_by, Task

# Create your views here.
def index(request):
    context = {
        'classes':Task.objects.all()
    }
    return render(request, 'task/index.html', context)

def delete(request, id):
    task = Task.objects.get(id=id)
    context={'id':id,
             'name': task.name,
             'desc': task.description,
             }
    return render(request, 'task/delete.html', context)

def process(request):
    errors = Task.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        print(type(request.POST['done_by']))
        cap_done_by = request.POST['done_by'].capitalize()
        # request.POST['done_by'] = cap_teach
        new_done_by = Done_by.objects.save_done_by(request.POST, cap_done_by)
        new_task = Task.objects.save_task(request.POST, cap_done_by)

    return redirect('/task/index/')

def deleted(request, id):
    task_class = Task.objects.get(id=id)
    task_class.delete()
    return redirect('/task/index/')
