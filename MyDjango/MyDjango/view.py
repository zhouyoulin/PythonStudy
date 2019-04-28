from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from . import settings
import os
import json
import dlib

def hello(request):
    return HttpResponse("hello word")

def index(request):
    return render(request, 'index.html')

@requires_csrf_token
def uploadImg(request):
    print(request.method)
    if request.method == 'POST':
        rect = {'status': 'error', 'code': '400', 'msg': 'no error'}
        print(type(rect))
        try:
            user = request.POST.get('user')
            img = request.FILES.get('img')
            print(img.name)
            print(os.path.join(os.path.join(settings.BASE_DIR, 'static'), img.name))
            f = open(os.path.join(os.path.join(settings.BASE_DIR, 'static'), img.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            rect['status'] = 'success'
            rect['code'] = '200'
            f.close()
        except Exception as e:
            rect['msg'] = str(e)
        finally:
            json_str = json.dumps(obj=rect)
            return HttpResponse(json_str)
    return render_to_response('upload.html')
