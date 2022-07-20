from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from .models import Employee

def login(request):
    return render(request, "login.html")
def go(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'mainpage.html')
        else:
            return redirect('login')
def welcome(request):
    return render(request,"mainpage.html")
def update(request):
    return render(request,"update.html")

def add(request):
    return render(request,"add.html")
def display(request):
    record=Employee.objects.all
    return render(request,"display.html",{'employee':record})

def delete(request):
    return render(request,"delete.html")
def reguser(request):
    btn=request.POST.get("sub")
    emp=Employee()
    emp.eid= request.POST.get('eid')
    emp.ename = request.POST.get('ename')
    emp.eemail = request.POST.get('eemail')
    emp.econtact = request.POST.get('econtact')
    emp.save()
    param={"msg":"Record Uploaded...!!!!!"}
    return render(request,"add.html",param)

def moredata(request):
    btn=request.GET.get("sub")
    if btn=="Edit":
        eid= request.GET.get("eid")
        record=Employee.objects.get(eid=eid)
        param={"data":record}
        return render(request,"edit.html",param)
def moreupdate(request):
    eid=request.GET.get('eid')
    ename = request.GET.get('ename')
    eemail = request.GET.get('eemail')
    econtact = request.GET.get('econtact')
    data=Employee.objects.get(eid=eid)
    data.ename=ename
    data.eemail=eemail
    data.econtact=econtact
    data.save()
    param={"msg":"Record Updated Successfully"}
    return render(request,"edit.html",param)
def dele(request):
    btn = request.GET.get("sub")
    if btn == "Delete":
        eid = request.GET.get("eid")
        Employee.objects.filter(eid=eid).delete()
        param = {"msg": "Record Deleted Successfully"}
        return render(request, "delete.html", param)


def logout(request):
    auth.logout(request)
    return render(request, "login.html")

