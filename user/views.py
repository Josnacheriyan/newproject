from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')
def index1(request):
    return render(request, 'index.html')
def index2(request):
    if request.session.has_key('lid'):
        a=request.session['lid']
        return render(request, 'index2.html')
    else:
        return HttpResponseRedirect('login')
def about(request):
    return render(request, 'about.html')
def bakery(request):
    return render(request, 'bakery.html')
def beverages(request):
    return render(request, 'beverages.html')
def cleaning(request):
    return render(request, 'cleaning.html')
def confictionery(request):
    return render(request, 'confictionery.html')
def construction(request):
    return render(request, 'construction.html')
def contact(request):
    if request.method == 'POST':
        contact_name =request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']
        send_mail(
            'message from ' + contact_name,
            contact_message,
            contact_email,
            ['josnacc25@gmail.com'],
        )  
        messages.success(request, 'We received your email and will respond shortly')
        	
        return render(request, 'contact.html',{'contact_name':contact_name})
        
    else:    
        
        return render(request, 'contact.html')
def fabric_care(request):
    return render(request, 'fabric-care.html')
def foodingredients(request):
    return render(request, 'foodingredients.html')
def machinery_equipment(request):
    return render(request, 'machinery-equipment.html')
def meat(request):
    return render(request, 'meat.html')
def paint_coating(request):
    return render(request, 'paint-and-coating.html')
def paint(request):
    return render(request, 'paint.html')

def polymer(request):
    return render(request, 'polymer.html')
def pre_mixes(request):
    return render(request, 'pre-mixes.html')
def chemicals(request):
    return render(request, 'speciality-chemicals.html')
def water(request):
    return render(request, 'water.html')
def events(request):
    template = 'events.html'
    form = AddEvent.objects.all()
    
    context = {"form": form}
    return render(request, template, context)
def services(request):
    return render(request, 'services.html')
def login(request):
    return render(request, 'login.html')
def log(request):
    if request.method == 'POST':
        
        username = request.POST['username'] 
        password = request.POST['password']
        user = Loging.objects.all().filter(username=username, password=password)
        if user:
            for x in user:
                username=x.username
                password=x.password
                request.session['lid']=x.id
               
                if username == "AlShihabAdmin" and password=="Admin123":
                    return HttpResponseRedirect('index2')
                
                else:
                    return render(request,'login.html')
        else:
            messages.error(request, 'invalid Username or Passwords')		
            return HttpResponseRedirect('login')
    else:
        
        return render(request,'login.html')

        
        
def eventform(request):
    if request.session.has_key('lid'):
        a=request.session['lid']
        if request.method == 'POST':
            title =request.POST['title']
            description = request.POST['description']
            date = request.POST['date']
            place = request.POST['place']
            image = request.FILES['image']
            form1 = AddEvent(title=title, description=description, date=date, place=place, image=image)
            form1.save()   
            return redirect('viewevent')
        else:
            
            return render(request, 'eventform.html')
        return render(request, 'eventform.html')
    else:
        return HttpResponseRedirect('login')
def viewevent(request):
    if request.session.has_key('lid'):
        a=request.session['lid']
        template = 'viewevent.html'
        form = AddEvent.objects.all()
        context = {"form": form}
        return render(request, template, context)
    else:
        return HttpResponseRedirect('login')
def deleteevent(request):
    if request.method=="GET":
        delid=request.GET['eventid']
        AddEvent.objects.all().filter(id=delid).delete()
        return HttpResponseRedirect('viewevent')
def blog(request):
    template = 'gallery.html'
    form3 = ImageUpload.objects.all()
    context = {"form3": form3}
    return render(request, template, context)
def imageupload(request):
    if request.session.has_key('lid'):
        a=request.session['lid']
        if request.method == 'POST':
            images = request.FILES['images']
            # images1 = request.FILES['images1']
            form2= ImageUpload(images=images)
            form2.save()   
            return redirect('viewgallery')
        else:
            return render(request, 'imageupload.html')
        return render(request, 'imageupload.html')
    else:
        return HttpResponseRedirect('login')
def viewgallery(request):
    if request.session.has_key('lid'):
        a=request.session['lid']
        template = 'viewgallery.html'
        form3 = ImageUpload.objects.all()
        context = {"form3": form3}
        return render(request, template, context)
    else:
        return HttpResponseRedirect('login')


#-------------------------------------For logout--------------------------------------

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')