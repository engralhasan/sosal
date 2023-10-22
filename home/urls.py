from django.urls import path
from .views import home,profileShow,profileEdit

urlpatterns = [
    path('', home,name='home'),
    path('profileShow/', profileShow,name='profileShow'),
    path('profileEdit/<int:id>', profileEdit,name='profileEdit'),
]