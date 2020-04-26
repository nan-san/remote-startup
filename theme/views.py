from django.views.generic import TemplateView 
from .models import Sort

class Home(TemplateView):
    template_name ='theme/home.html'

class SortListView(ListView):
    models = Product
    template_name = 'theme/list.html'
    
