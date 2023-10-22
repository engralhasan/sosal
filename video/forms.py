from .models import videoinput
from django import forms
class video_from(forms.ModelForm):
    class Meta:
        model=videoinput
        fields=('caption','video')