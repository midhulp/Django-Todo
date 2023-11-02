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
