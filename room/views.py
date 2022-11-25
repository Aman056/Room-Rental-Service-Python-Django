from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *


def index(request):
    return render(request,'index.html')

def login(request):
    error = ""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pswd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                auth.login(request,user)

                error = "not"
            else:
                error = "yes"
        except:

            error = "yes"
    d = {'error': error}
    return render(request,'login.html',d)




def signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        c = request.POST['contact']
        dob = request.POST['dob']
        pd = request.POST['pwd']
        g = request.POST['gender']
        img = request.FILES['image']
        a = request.POST['add']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=pd)
            Signup.objects.create(user=user,mobile=c,image=img,gender=g,dob=dob,address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'signup.html',d)



def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')


def Logout(request):
    logout(request)
    return redirect('login')

def add_room(request):

    return render(request,'add_room.html')

def contact_us(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        m = request.POST['mobile']
        e = request.POST['email']
        c = request.POST['comment']
        try:
            Contact.objects.create(full_name=f,email=e,mobile=m,comment=c)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'contact_us.html', d)


def view_contact(request):
    data = Contact.objects.all()
    data2 = Feedback.objects.all()
    d = {'data': data,'data2':data2}
    return render(request,'view_contact.html', d)



def delete_contact(request,id):
    data = Contact.objects.get(id=id)
    data.delete()
    return redirect('view_contact')


def feedback(request):
    error = ""
    user = request.user
    data = Signup.objects.get(user=user)
    if request.method == "POST":
        f = request.POST['fname']
        m = request.POST['contact']
        e = request.POST['email']
        c = request.POST['comment']
        try:
            Feedback.objects.create(full_name=f,email=e,mobile=m,feedback=c)
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'data':data}
    return render(request,'feedback.html',d)


def delete_feedback(request,id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_contact')

def view_room_user(request):
    data = Room.objects.all()
    d = {'data': data}

    return render(request,'view_room_user.html',d)

def add_room(request):
    error = ""
    if request.method == 'POST':
        r = request.POST['roomno']
        p = request.POST['price']
        t = request.POST['rtype']
        i = request.FILES['image']
        s = request.POST['status']
        try:
            Room.objects.create(room_no=r,price=p,r_type=t,r_image=i,status=s)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}

    return render(request,'add_room.html',d)

def view_room_admin(request):
    data = Room.objects.all()
    d = {'data': data}
    return render(request,'view_room_admin.html',d)
def delete_room(request,id):
    data = Room.objects.get(id=id)
    data.delete()
    return redirect('view_room_admin')

def edit_room(request,id):
    error=""
    data = Room.objects.get(id=id)
    if request.method=="POST":
        r = request.POST['roomno']
        p = request.POST['price']
        t = request.POST['rtype']
        s = request.POST['status']
        i = request.FILES['r_img']
        data.room_no=r
        data.price=p
        data.r_type=t
        data.r_image=i
        data.status=s
        try:
            data.save()
            error="no"
        except:
            error="yes"

    d = {'data': data,'error': error}

    return render(request,'edit_room.html',d)