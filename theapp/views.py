from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request, 'index.html')

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
