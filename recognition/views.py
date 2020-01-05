from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import base64
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})


def registration(request):
    return render(request, 'registration.html', {})

@csrf_exempt
def image_capture(request):
    # csrfContext = RequestContext(request)
    print("captured")
    if request.method == 'POST':
        print(request.POST.get('emp'))
        empid=request.POST.get('emp')
        count=request.POST.get("count")
        print(count)
        print(request.POST.get('ip'))
        print(request.FILES['image'])
        # img=request.FILES['image']
        # print(img.read())
        # print("saved")
        data = request.FILES['image']  # or self.files['image'] in your form

        path = default_storage.save('dataset/'+empid+'/'+str(count)+'.jpeg', ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        print("saved",tmp_file)
        # img = Image.open(request.POST["image0"])


def recognition(request):
    return render(request, 'recognition.html', {})