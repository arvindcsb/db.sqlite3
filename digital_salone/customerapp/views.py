import smtplib

from django.shortcuts import render, redirect
from customerapp.models import *
from customerapp.forms import *

# Create your views here.
def about(request):
    return render(request,"about.html",{})

def index(request):
    return render(request,"index.html",{})

def contact(request):
    if request.method=="POST":
        contact=ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
        return render(request,"contact.html",{})
    return render(request,"contact.html",{})


def customer_register(request):
    if request.method=="POST":
        customer=CustomerForm(request.POST)
        if customer.is_valid():
            customer.save()
        return render(request,"customer_login.html",{})
    return render(request,"customer_register.html",{})

def customer_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        request.session["email"]=email
        try:
            customer=Customer.objects.get(email=email, password=password)
            msg="data found"
            return render(request,"customer_home.html",{"customer":customer,"msg":msg})
        except:
            msg="invalid data"
            return render(request,"customer_login.html",{"msg":msg})
    return render(request,"customer_login.html",{})

def customer_home(request):
    return render(request,"customer_home.html",{})


def customer_logout(request):
    request.session['email']=''
    del request.session["email"]
    return render(request,"customer_login.html",{})

def is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def customer_change_password(request):
    if is_login(request):
        if request.method=="POST":
            email=request.session['email']
            password=request.POST['password']
            new_password=request.POST['new_password']
            try:
                customer=Customer.objects.get(email=email,password=password)
                customer.password=new_password
                customer.save()
                msg="success fully change your password"
                return render(request,"customer_login.html",{"msg":msg})
            except:
                msg="invalid data"
                return render(request,"customer_change_password.html",{"msg":msg})
        return render(request,"customer_change_password.html",{})
    else:
        return render(request,"customer_login.html",{})


def customer_display(request):
    customers=Customer.objects.all()
    return render(request,"customer_display.html",{"customers":customers})


def customer_forgot_password(request):
    if request.method=="POST":
        email=request.POST["email"]
        try:
            customer=Customer.objects.get(email=email)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("salmanshaik0621@gmail.com", "Salman@123")
            message = "greeting from admin team \n your password is" + customer.password
            server.sendmail("salmanshaik0621@gmail.com", [email], message)
            print("mail sent...")
            server.quit()
            msg="success full send you email"
            return render(request,"customer_forgot_password.html",{"msg":msg})
        except:
            msg="invalid data"
            return render(request,"customer_forgot_password.html",{"msg":msg})
    return render(request,"customer_forgot_password.html",{})


def customer_edit(request):
    email=request.session["email"]
    customer=Customer.objects.get(email=email)
    return render(request,"customer_edit.html",{"customer":customer})

def customer_update(request):
    if request.method == "POST":
        try:
            email = request.session["email"]
            print("h")
            customer = Customer.objects.get(email=email)
            customer.fullname = request.POST["fullname"]
            customer.mobile = request.POST["mobile"]
            customer.city = request.POST["city"]
            customer.gender=request.POST["gender"]
            customer.save()
            print("HI")

            return redirect("/customer_display")

        except Exception as a:
            print(a)
            return render(request, 'customer_edit.html', {})

    return render(request, "customer_edit.html", {})


def customer_salon_display(request):
    salons=Salons.objects.all()
    return render(request,"customer_salon_display.html",{"salons":salons})

def customer_salon_booknow(request,id):
    salon=Salons.objects.get(id=id)
    email=request.session['email']
    return render(request,"customer_salon_booking.html",{"salon":salon,"email":email,"id":id})

def customer_salon_booking(request):
    if request.method=="POST":
        book=BookingForm(request.POST)
        if book.is_valid():
            book.save()
        return render(request,"customer_home.html",{})
    return render(request,"customer_salon_booking.html",{})

def customer_salon_booking_display(request):
    books=Booking.objects.all()
    return render(request,"customer_salon_booking_display.html",{"books":books})

def booking_delete(request,id):
    book=Booking.objects.get(id=id)
    book.delete()
    return redirect("/customer_salon_booking_display")

def booking_edit(request,id):
    book=Booking.objects.get(id=id)
    email=request.session['email']
    return render(request,"customer_salon_booking_edit.html",{"book":book,"email":email})


def booking_update(request):
    if request.method=="POST":
        userid=request.POST["id"]
        book=Booking.objects.get(id=userid)
        book=BookingForm(request.POST,instance=book)
        if book.is_valid():
            book.save()
            return redirect("/customer_salon_booking_display")
    return redirect("/customer_salon_booking_display")


def customer_salon_link(request,id):
    salon=Salons.objects.get(id=id)
    email=request.session["email"]
    return render(request,"customer_salon_rating.html",{"salon":salon,"email":email})

def customer_salon_rating(request):
    if request.method=="POST":
        rating=RatingForm(request.POST)
        if rating.is_valid():
            rating.save()
            return render(request,"customer_home.html",{})
    return render(request,"customer_salon_rating.html",{})

def customer_salon_rating_display(request):
    ratings=Rating.objects.all()
    return render(request,"customer_salon_rating_display.html",{"ratings":ratings})