from django.shortcuts import render


# Create your views here.

def  index(request):
    ''' A view to return the index page '''
    
    template = 'home/index.html'
   
    return render(request, template)

def  menu(request):
    ''' A view to return the menu page '''
    
    template = 'home/menu.html'
   
    return render(request, template)

def  contact(request):
    ''' A view to return the contact page '''
    
    template = 'home/contact.html'
   
    return render(request, template)


