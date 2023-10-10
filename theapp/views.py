from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def Index(request):
    title_name = Shior.objects.all()
    about_team = Team.objects.all()
    type_of_property = Category.objects.all()
    list_property = Home.objects.all()
    category = Category_home.objects.all()
    
    paginator = Paginator(list_property, 1) 
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'title_name':title_name,
        'about_team':about_team,
        'type_of_property':type_of_property,
        'list_property':list_property,
        'category':category,
        "page": page
    }
    return render(request, 'index.html', context)

def A404(request):
    return render(request, '404.html')

def About(request):
    return render(request, 'about.html')

def Contact_Data(request):
    if request.method == "POST":
        name1 = request.POST.get('name1')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data_contact = Contact(name1=name1, email=email, subject=subject, message=message)
        data_contact.save()
    return render(request, 'contact.html')

def Property_Agent(request):
    return render(request, 'property-agent.html')

def Property_List(request):
    return render(request, 'property-list.html')

def Property_Type(request):
    return render(request, 'property-type.html')

def Testimonial(request):
    return render(request, 'testimonial.html')
