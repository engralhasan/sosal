from django.shortcuts import render,HttpResponse
from .forms import video_from
from .models import videoinput

# Create your views here.
def video(request):
    all_video=videoinput.objects.all()
    return render(request,'video/videotem.html',locals())

def videoin(request):
    if request.method == 'POst':
        form=video_from(data=request.POST,files=request.FILES)
        if form.is_valid():
            return HttpResponse("<h1> uploaded successfully</h1>")
    else:
        form=video_from()
    return render(request,'video/usin.html',locals())