from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

class Home(TemplateView):
    template_name = 'base.html'