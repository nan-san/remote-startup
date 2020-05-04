from django.views.generic import TemplateView, ListView
from .models import Sort

class Home(TemplateView):
    template_name ='rpg/home.html'

class SortListView(ListView):
    models = Sort
    template_name = 'rpg/list.html'
    
 