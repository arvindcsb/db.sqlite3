from django.shortcuts import render, redirect
from salonapp.models import *
from salonapp.forms import *
# Create your views here.

def salon_register(request):
    if request.method=="POST":
        salon=SalonsForm(request.POST)
        if salon.is_valid():
            salon.save()
        return render(request,"salon_login.html",{})
    return render(request,"salon_register.html",{})

def salon_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        request.session["email"]=email
        try:
            salon=Salons.objects.get(email=email,password=password)
            msg="data found"
            return render(request,"salon_home.html",{"salon":salon,"msg":msg})
        except:
            msg="invalid data"
            return render(request,"salon_login.html",{"msg":msg})
    return render(request,"salon_login.html",{})

def salon_home(request):
    return render(request,"salon_home.html",{})

def salon_logout(request):
    request.session['email']=''
    del request.session["email"]
    return render(request,"salon_login.html",{})

def is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def salon_change_password(request):
    if is_login(request):
        if request.method=="POST":
            email=request.session['email']
            password=request.POST['password']
            new_password=request.POST['new_password']
            try:
                salon=Salons.objects.get(email=email,password=password)
                salon.password=new_password
                salon.save()
                msg="success fully change your password"
                return render(request,"salon_login.html",{"msg":msg})
            except:
                msg="invalid data"
                return render(request,"salon_change_password.html",{"msg":msg})
        return render(request,"salon_change_password.html",{})
    else:
        return render(request,"salon_login.html",{})


def salon_display(request):
    salons=Salons.objects.all()
    return render(request,"salon_display.html",{"salons":salons})


def salon_edit(request):
    email=request.session["email"]
    salon=Salons.objects.get(email=email)
    return render(request,"salon_edit.html",{"salon":salon})


def salon_update(request):
    if request.method == "POST":
        try:
            email = request.session["email"]
            print("h")
            salon = Salons.objects.get(email=email)
            salon.title = request.POST["title"]
            salon.mobile = request.POST["mobile"]
            salon.city = request.POST["city"]
            salon.about=request.POST["about"]
            salon.address=request.POST["address"]
            salon.gender=request.POST["gender"]
            salon.save()
            print("HI")

            return redirect("/salon_display")

        except Exception as a:
            print(a)
            return render(request, 'salon_edit.html', {})

    return render(request, "salon_edit.html", {})



def booking_display(request):
    books=Booking.objects.all()
    return render(request,"booking_display.html",{"books":books})


def rating_display(request):
    ratings=Rating.objects.all()
    return render(request,"rating_display.html",{"ratings":ratings})