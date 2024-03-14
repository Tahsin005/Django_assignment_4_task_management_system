from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import TaskModel
# Create your views here.
def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print (form.cleaned_data)
            return redirect('task_list')
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, id):
    task = TaskModel.objects.get(pk = id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print (form.cleaned_data)
            return redirect('task_list')
    form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk = id)
    task.delete()
    return redirect('task_list')

def task_list(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})