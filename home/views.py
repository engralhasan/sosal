from django.shortcuts import render,redirect
from .models import Ediprof
import os
# Create your views here.
def home(request):
    
    return render(request, 'home/home.html')

def profileShow(request):
    addpro=Ediprof.objects.all()
    return render(request,'home/profile.html',locals())

def profileEdit(request,id):
    prof = Ediprof.objects.get(id=id)
    if request.method == "POST":
        prof.profimg =request.FILES['profimg']
        prof.coverimg =request.FILES['coverimg']
        prof.name = request.POST.get("name")
        prof.job = request.POST.get("job")
        prof.scholnam = request.POST.get("scholnam")
        prof.univarName = request.POST.get("univarName")
        prof.liveName = request.POST.get("liveName")
        prof.fromName = request.POST.get("fromName")
        prof.save()
        return redirect('profileShow')
    return render(request,'home/profileEdit.html',locals())

 