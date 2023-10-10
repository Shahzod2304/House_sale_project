from django.shortcuts import render
from .models import *
# Create your views here.

def Index(request):
    title_name = Shior.objects.all()
    about_team = Team.objects.all()
    type_of_property = Category.objects.all()
    list_property = Home.objects.all()

    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        allcontact = Contact(name=name, email=email, subject=subject, message=message)
        allcontact.save()
        
    context = {
        'title_name':title_name,
        'about_team':about_team,
        'type_of_property':type_of_property,
        'list_property':list_property,
    }
    return render(request, 'index.html', context)

def A404(request):
    return render(request, '404.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Property_Agent(request):
    return render(request, 'property-agent.html')

def Property_List(request):
    return render(request, 'property-list.html')

def Property_Type(request):
    return render(request, 'property-type.html')

def Testimonial(request):
    return render(request, 'testimonial.html')
