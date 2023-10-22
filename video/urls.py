from django.urls import path
from .views import  video,videoin

urlpatterns = [
    path('', video,name='video'),
    path('videoin/', videoin,name='videoin'),
     
    
]