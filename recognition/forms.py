from django import forms

class ImageForm(forms.Form):
    image=forms.ImageField()
    emp=forms.CharField(max_length=100)
    ip=forms.CharField(max_length=100)
