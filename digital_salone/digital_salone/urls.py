"""digital_salone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customerapp import views
from salonapp import views as salonviews
from adminsapp import views as adminsviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("contact/", views.contact, name="contact"),
    path("customer_register/", views.customer_register, name="customer_register"),
    path("customer_login/", views.customer_login, name="customer_login"),
    path("customer_home/", views.customer_home, name="customer_home"),
    path("customer_logout/", views.customer_logout, name="customer_logout"),
    path("customer_change_password/", views.customer_change_password, name="customer_change_password"),
    path("customer_display/", views.customer_display, name="customer_display"),
    path("customer_forgot_password/", views.customer_forgot_password, name="customer_forgot_password"),
    path("customer_edit/", views.customer_edit, name="customer_edit"),
    path("customer_update/", views.customer_update, name="customer_update"),
    path("customer_salon_display/", views.customer_salon_display, name="customer_salon_display"),
    path("customer_salon_booknow/<int:id>", views.customer_salon_booknow, name="customer_salon_booknow"),
    path("customer_salon_booking/", views.customer_salon_booking, name="customer_salon_booking"),
    path("customer_salon_booking_display/", views.customer_salon_booking_display, name="customer_salon_booking_display"),
    path("booking_delete/<int:id>", views.booking_delete, name="booking_delete"),
    path("booking_edit/<int:id>", views.booking_edit, name="booking_edit"),
    path("booking_update/", views.booking_update, name="booking_update"),
    path("customer_salon_link/<int:id>", views.customer_salon_link, name="customer_salon_link"),
    path("customer_salon_rating/", views.customer_salon_rating, name="customer_salon_rating"),
    path("customer_salon_rating_display/", views.customer_salon_rating_display, name="customer_salon_rating_display"),



    path("salon_register/", salonviews.salon_register, name="salon_register"),
    path("salon_login/", salonviews.salon_login, name="salon_login"),
    path("salon_home/", salonviews.salon_home, name="salon_home"),
    path("salon_logout/", salonviews.salon_logout, name="salon_logout"),
    path("salon_change_password/", salonviews.salon_change_password, name="salon_change_password"),
    path("salon_display/", salonviews.salon_display, name="salon_display"),
    path("salon_update/", salonviews.salon_update, name="salon_update"),
    path("salon_edit/", salonviews.salon_edit, name="salon_edit"),
    path("booking_display/", salonviews.booking_display, name="booking_display"),
    path("rating_display/", salonviews.rating_display, name="rating_display"),



    path("admins_login/", adminsviews.admins_login, name="admins_login"),
    path("admins_home/", adminsviews.admins_home, name="admins_home"),
    path("admins_logout/", adminsviews.admins_logout, name="admins_logout"),
    path("admins_change_password/", adminsviews.admins_change_password, name="admins_change_password"),
    path("admins_customer_display/", adminsviews.admins_customer_display, name="admins_customer_display"),
    path("admins_salon_display/", adminsviews.admins_salon_display, name="admins_salon_display"),
    path("admins_salon_delete/<int:id>", adminsviews.admins_salon_delete, name="admins_salon_delete"),
    path("admins_customer_delete/<int:id>", adminsviews.admins_customer_delete, name="admins_customer_delete"),
    path("admins_salon_booking_display/", adminsviews.admins_salon_booking_display, name="admins_salon_booking_display"),
    path("admins_customer_salon_rating_display/", adminsviews.customer_salon_rating_display,name="admins_customer_salon_rating_display"),

]
