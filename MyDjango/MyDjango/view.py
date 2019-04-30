from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from . import settings
import os
import json
import dlib
import cv2
import numpy as np

predictor_path = 'C:/FaceRecognition/shape_predictor_68_face_landmarks.dat'
face_rec_path = 'C:/FaceRecognition/dlib_face_recognition_resnet_model_v1.dat'
face_folder_path = os.path.join(settings.BASE_DIR, 'static\\face')

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
            checkFace(os.path.join(os.path.join(settings.BASE_DIR, 'static'), img.name))
        except Exception as e:
            rect['msg'] = str(e)
        finally:
            json_str = json.dumps(obj=rect)
            return HttpResponse(json_str)
    return render_to_response('upload.html')

def checkFace(filepath):
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_path)
    # image = cv2.imread(filepath)
    image = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), -1)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dets = detector(gray_img, 1)
    print(enumerate(dets))
    print(dets)
    for face in dets:
        shape = sp(gray_img, face)
        for po in shape.parts():
            pos = (po.x, po.y)
            cv2.circle(gray_img, pos, 2, (0, 255, 0), 1)
    cv2.imshow("img", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("C:/FaceRecognition/face.png", gray_img)
