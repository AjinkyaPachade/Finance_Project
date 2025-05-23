"""
URL configuration for FinanceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from FinanceApp.views import index, signup, forgotpassword, storeUser, checkLogin, home, changePass, contact, contactDetail, about, add_income, delete_income, update_income, users_profile, storeIncome, view_income, viewIncome, updateIncome, deleteIncome


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name='index'),
    path("signup/",signup,name='signup'),
    path("forgotpassword/",forgotpassword,name='forgotpassword'),
    path("storeUser/",storeUser,name='storeUser'),
    path("checkLogin/",checkLogin,name='checkLogin'),
    path("home/",home,name='home'),
    path("changePass/",changePass,name='changePass'),
    path("contact/",contact,name='contact'),
    path("contactDetails/",contactDetail,name='contactDetails'),
    path("about/",about,name='about'),
    path("add_income/",add_income,name='add_income'),
    path("delete_income/",delete_income,name='delete_income'),
    path("update_income/",update_income,name='update_income'),
    path("users_profile/",users_profile,name='users_profile'),
    path("storeIncome/",storeIncome,name='storeIncome'),
    path("view_income/",view_income,name='view_income'),
    path("viewIncome/",viewIncome,name='viewIncome'),
    path("updateIncome/",updateIncome,name='updateIncome'),
    path("deleteIncome/",deleteIncome,name='deleteIncome'),


]
