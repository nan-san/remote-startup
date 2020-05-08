from django.urls import path,include
from . import views
from django.conf.urls import url

app_name = 'theme'

urlpatterns =[
    path('home/', views.Home.as_view(), name='home'),
    path('sorts/', views.SortListView.as_view(), name='sort_data'),
    path('', views.base, name='base'), 
    path('', views.list, name='list'), 
]
