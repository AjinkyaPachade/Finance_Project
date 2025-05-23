from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from FinanceApp.database import Connection
from FinanceProject import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')


def storeUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        db = Connection()
        if db.storeUser(name, email, username, pass1):

            subject = 'Hello! Thank You for Signing Up for Our Personal Finance Application'
            message = "Congratulations! You have successfully signed up for the Personal Finance Application!"
            email_form = 'pachadeajinkya7@gmail.com'
            rec_list = [email]
            
            try:
                send_mail(subject, message, email_form, rec_list)
                return render(request,'index.html')
            
            except Exception as e:
                print(f"Email error: {e}")
                return render(request, 'signup.html', {'error': 'Email could not be sent. Please try again.'})
        else:
            msg = 'SignUp Failed'
            return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'signup.html', {'error': 'Invalid request method.'})
    

def checkLogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')

        db=Connection()
        if db.checkLogin(username,pass1)== True:
            request.session['username']= username
            return render(request,'home.html',)
        else:
            msg="Login Failed !!"
        return render(request,'message.html',{'msg':msg})


def home(request):
    return render(request,'home.html')

def changePass(request):
    if request.method=='POST':
        username=request.POST.get("tusername")
        oldp=request.POST.get("told")
        newp1=request.POST.get("tnew1")
        newp2=request.POST.get("tnew2")

        if newp1 != newp2:
            msg='Password not matched !!'
        else:
            db=Connection()
            if db.changePass(username,oldp,newp1)==True:
                msg="Password Changed Successfully !"
                
            else:
                msg="Password Changed Failed !"
    return render(request,'message.html',{'msg':msg})


def contact(request):
    return render(request,'contact.html')


def contactDetail(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        subject1=request.POST.get('subject')
        message1=request.POST.get('message')
        
        db=Connection()
        if db.contactDetail(name1,email1,subject1,message1)==True:
            return render(request,'contact.html',{})
        else:
            msg='Message does not send !!'
        return render(request,'message.html',{'msg':msg})
    return render(request,'home.html',{})       

def about(request):
    return render(request,'about.html')

def add_income(request):
    return render(request,'add_income.html')

def delete_income(request):
    return render(request,'delete_income.html')

def update_income(request):
    return render(request,'update_income.html')

def users_profile(request):
    return render(request,'users_profile.html')


def storeIncome(request):
    if request.method=='POST':
        uname1=request.POST.get('username')
        title1=request.POST.get('title')
        amount1=float(request.POST.get('amount'))
        date1=request.POST.get('date')
        category1=request.POST.get('category')

        
        db=Connection()
        if db.storeIncome(uname1,title1,amount1,date1,category1)==True:
            request.session['username']=uname1
            request.session['amount']=amount1

            msg='Income add Successfully !!'
            return render(request,'message.html',{})
        else:
            msg='Income add Successfully !!'
        return render(request,'message.html',{'msg':msg})
    return render(request,'home.html',{})  


def view_income(request):
    return render(request,'view_income.html')



def viewIncome(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')

        db = Connection()
        amount = db.viewIncome(username, date)

        if amount is not None:
            msg = f"{username}, your income on {date} is: {amount}"
        else:
            msg = "No income record found for the given username and date."

        return render(request, 'message.html', {'msg': msg})

    

def updateIncome(request):
    if request.method=='POST':
        username1=request.POST.get('username')
        date1 = request.POST.get('date')
        amount1 = float(request.POST.get('amount'))
        category1 = request.POST.get('category')
    
        db = Connection()
        if db.updateIncome(username1,date1,amount1,category1) == True:
            msg = "Income Update Successfully"

        else:
            msg = "Income Update Successfully"

        return render(request,'message.html',{'msg':msg})


def deleteIncome(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        date1 = request.POST.get('date')
        
        db = Connection()
        if db.deleteIncome(username1, date1):
            msg = "Income record deleted successfully."
        else:
            msg = "Failed to delete the income record."

        return render(request, 'message.html', {'msg': msg})
    else:
        return render(request, 'delete_income.html') 