from django . shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Sort
from django.http import HttpResponse

class Home(TemplateView):
    template_name ='rpg/home.html'

class SortListView(ListView):
    models = Sort
    template_name = 'rpg/list.html'

  


def base(request):
    return render(request, 'rpg/base.html')

def home(request):
    return render(request, 'rpg/home.html')

def list(request):
        return render(request, 'rpg/list.html')


 