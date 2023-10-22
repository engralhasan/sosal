from django.urls import path
from .views import login,sinup,signout,forget_pass,verify_otp,resetpassword

urlpatterns = [
    path('', login,name='login'),
    path('sinup/', sinup,name='sinup'),
    path('signout/', signout,name='signout'),
    path('forget_pass/', forget_pass,name='forget_pass'),
    path('verify_otp/', verify_otp,name='verify_otp'),
    path('resetpassword/', resetpassword,name='resetpassword'),
    
]