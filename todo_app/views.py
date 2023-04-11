from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from todo_app.forms import Taskform
from todo_app.models import Task


# Create your views here.
class TaskListview(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'obj1'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detailview.html'
    context_object_name = 'i'

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('taliview')


class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'updateview.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    success_url = reverse_lazy('taliview')



def home(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST['task']
        priority = request.POST['priority']
        date=request.POST['date']
        obj = Task(name=name, priority=priority,date=date)
        obj.save()

    return render(request, 'tasks.html', {'obj1': obj1})
    # return render(request,'home.html')
# def tasks(request):
def delete(request,task_id):
    if request.method=='POST':
        task=Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task_id=Task.objects.get(id=id)
    form=Taskform(request.POST or None,instance=task_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task_id':task_id,'form':form})