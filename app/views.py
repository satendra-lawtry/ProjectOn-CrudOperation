from django.shortcuts import render,redirect
from .models import UserApp

def index(request):
    if request.method=='POST':
        u=UserApp()
        u.name=request.POST['name']
        u.email=request.POST['email']
        u.password=request.POST['pass']
        u.contact=request.POST['num']
        u.save()
        return render(request,"AddUser.html",{'message':'data insert success'})

    return render(request,"AddUser.html")

def showRecord(request):
    o=UserApp.objects.all()
    return render(request,"Show.html",{'record':o})

def deleteRecord(request,id):
    data=UserApp.objects.get(id=id)
    data.delete()
    return redirect('/show')

def editdata(request,id):
    data=UserApp.objects.filter(id=id)
    return render(request,"Edit.html",{'mydata':data})

def changeData(request):
    if request.method=='POST':
        id=request.POST['id']
        o=UserApp.objects.get(id=id)
        if(o):
            o.name=request.POST['name']
            o.password=request.POST['password']
            o.contact=request.POST['contact']
            o.save()
            return redirect('/show')
        else:
            return redirect('/show')
    return redirect('/show')





