from django.db.models.fields import return_None
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)

        if User.objects.filter(username=fnm).exists():
            messages.error(request, "That username is already taken!")
            return render(request, 'signup.html')
        try:
            my_user=User.objects.create_user(fnm,emailid,pwd)
            my_user.save()
            return redirect('/loginn')
        except Exception as e:
            messages.error(request, "Something went wrong")
    return render(request,'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todo')
        else:
            return redirect('/login')


    return render(request,'loginn.html')

def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title, user=request.user)
        obj.save()
        res=models.TODOO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo',{'res':res})
    res = models.TODOO.objects.filter(user=request.user).order_by('-date')

    return render(request,'todo.html',{'res':res})

def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO.objects.get(srno=srno)
        obj.title=title
        obj.save()
        user=request.user
        return redirect('/todo')

    obj = models.TODOO.objects.get(srno=srno)
    res = models.TODOO.objects.filter(user=request.user).order_by('-date')

    return render(request, 'edit_todo.html', {'obj': obj})
#the srno passed is from urls.py ,now its is checked from the srno of models
def delete_todo(request, srno):
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')

def sign_out(request):
    logout(request)
    return redirect('/loginn')
