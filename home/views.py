from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'

# class Menu(TemplateView):
#     template_name = 'menu/menu.html'

# class Contact(TemplateView):
#     template_name = 'contact/contact.html'

# class Newsletter(TemplateView):
#     template_name = 'homenewsletter/newsletter.html'

