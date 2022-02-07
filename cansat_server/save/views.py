from math import asin, cos, pi, sin, sqrt, tan
from django.shortcuts import render
from django.core.files.base import ContentFile

from .forms import ImageForm
from save.models import CapturedImage
import requests
import datetime



def upload_file(request):
    
    if request.method == 'POST':
        print(request.POST)
        r = requests.get('http://192.168.3.13/capture')
        q = CapturedImage(distance=request.POST['distance'])
        q.image.save(str(datetime.datetime.now()) + '.jpg', ContentFile(r.content))
        q.save()
        
    return render(request, 'index2.html', {})

