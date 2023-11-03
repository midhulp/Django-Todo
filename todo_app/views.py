from django.http import HttpResponse
from django.shortcuts import redirect, render

from . models import Task

# Create your views here.



def home(request):
    obj1=Task.objects.all()
    if request.method == "POST":
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        obj=Task(name=name,priority=priority)
        obj.save()
    return render(request,"index.html",{'obj':obj1})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == "POST":
        new_name=request.POST.get('name')
        new_priority=request.POST.get('priority')

        task.name=new_name
        task.priority=new_priority
        task.save()
        return redirect('/')
    return render(request,'update.html',{'task':task})
