from django.shortcuts import render,redirect
from django.http import HttpResponse
from punch.models import contactus
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib. auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,"home.html")
@login_required   
def contactusx(request):
    return render(request,"contactus.html")
def aboutus(request):
    return render(request,"aboutus.html")
def services(request):
    data=contactus.objects.all().order_by("-id")
    context={"mydata":data}
    return render(request,"services.html",context)


def savethis(request):
    # print("datasave")
    if request.method=="POST":
        fullname=request.POST.get("fname")
        useremail=request.POST.get("email")
        phonenumber=request.POST.get("number")
        message=request.POST.get("msg")
        myimg=request.FILES.get('img')
        myemail=f"""
        this is user context us from data
        username:{fullname}
        useremail:{useremail}
        phonenumber={message}
        thanku to all :)
        """
        mail=EmailMessage("this email coming from django file",myemail,"nitesh26028@gmail.com",["nitesh26028@gmail.com"])
        mail.send()
        data=contactus(username=fullname,useremail=useremail,phonenumber=phonenumber,message=message,myimage=myimg)
        data.save()
        messages.success(request,"data save successfully")
    return redirect("services")
def deletethisdata(request,dfg):
    my_data=contactus.objects.get(id=dfg)
    my_data.delete()
    return redirect("services")

def updatethisdata(request,zxc):
    data=contactus.objects.get(id=zxc)
    return render(request,"contactus-update.html",{"up":data})

def nowupdatedata(request,xmn):
    if request.method=="POST":
     fullname=request.POST.get("fname")
     useremail=request.POST.get("email")
     phonenumber=request.POST.get("number")
     message=request.POST.get("msg")  
     myimg=request.FILES.get('img')
     my__data=contactus.objects.get(id=xmn)
     my__data.username=fullname
     my__data.useremail=useremail
     my__data.phonenumber=phonenumber
     my__data.message=message
     my__data.myimage=myimg
     my__data.save()
    return redirect("services") 

def searchthisdata(request):
    xyz=request.GET['query']
    searchdata=contactus.objects.filter(username=xyz) or contactus.objects.filter(phonenumber=xyz)
    context ={"mydata":searchdata}
    return render(request,"services.html",context)

def signup(request):
    if request.method == "POST":
        username=request.POST.get("username")
        Fullname=request.POST.get("fullname")
        email=request.POST.get("email")
        mypass=request.POST.get("mypass")
        
        saveuser=User.objects.create_user(username=username,email=email,first_name=Fullname,password=mypass)
        saveuser.save()
        messages.success(request,"user added successfully")
    return render(request,"signup.html") 

def mylogin(request):
    if request.user.is_authenticated:
        return redirect("contactus")

    if request.method == "POST":
       username=request.POST.get("username")
       mypass=request.POST.get("mypass")

       usercheck = authenticate(username=username,password=mypass)

       if usercheck is not None:
          login(request,usercheck)
          messages.success(request,"login successfully done.......")
          return redirect("contactus")
       
    else:
           messages.warning(request,"please enter valid info")
    return render(request,"login.html") 

def mylogout(request):
    logout(request)
    return redirect("login")
           
     
      
    
