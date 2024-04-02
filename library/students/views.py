from django.shortcuts import render, redirect
from students.models import Students,details,CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def register(request):
    if (request.method == 'POST'):
        u = request.POST['username']
        p = request.POST['password']
        cnf = request.POST['cnfpass']
        eml = request.POST['email']
        fnm = request.POST['fname']
        lnm = request.POST['lname']
        phn = request.POST['phn']
        addr=request.POST['adrs']
        if(p==cnf):
            user = CustomUser.objects.create_user(username=u, password=p, email=eml,first_name=fnm,last_name=lnm,phone=phn,address=addr)
            user.save()
    return render(request,'register.html')
def user_login(request):
    if (request.method == 'POST'):
        u = request.POST['username']
        p = request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request, user)
            return redirect('books:addlibrary')
    return render(request,'login.html')
@login_required
def add_students(request):
    if(request.method=='POST'):
        N = request.POST['Name']
        A= request.POST['Age']
        P = request.POST['Place']
        S = Students.objects.create(name=N, age=A, place=P)
        S.save()
        return register(request)
    return render(request,'addstudent.html')
def user_logout(request):
    logout(request)
    return user_login(request)

