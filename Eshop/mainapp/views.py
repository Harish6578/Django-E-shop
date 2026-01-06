from django.shortcuts import render

from .models import CarouselImage

# Create your views here.

def homeView(request):
    template ='mainapp/home.html'
    context = {
        'current_page': 'Home',

        #Let's collect all existing record of carousel image table to be sent to template
        'carousel_images' : CarouselImage.objects.all() # select * from carousel_image;
    }

    return render(request, template_name=template, context= context)

def aboutView(request):
    template = 'mainapp/about.html'
    context={
          'current_page' : 'About'
    }

    return render(request, template_name=template,context= context)

def contactView(request):
    template = 'mainapp/contact.html'
    context={
        'current_page' : 'Contact'
    }

    return render(request, template_name=template,context= context)

