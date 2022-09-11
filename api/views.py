import os

import cv2
from django.shortcuts import render
from easyocr import easyocr
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
import PIL

from ocr import settings


# Create your views here.
@api_view(['POST'])
def get_processed_data(request):
    if request.method == 'POST':
        context = {"data" : "not"}
        request_file = Image.open(request.data['image'])
        request_file.convert("RGB")
        path = request_file.save('pijush.jpg')

        reader = easyocr.Reader(['en', 'bn'], gpu=True)
        # result = reader.readtext('pijush.jpg')
        # top_left = tuple(result([16][0][0]))
        # top_right = tuple(result([16][0][2]))
        # nid = result[16][1]
        # dob = result[14][1]
        # nom = result[12][1]
        cv_image = cv2.imread('pijush.jpg')
        h, w, c = cv_image.shape
        cv_image = cv2.resize(cv_image,(w//3,h//3))
        cv2.imshow("imaage", cv_image)
        cv2.waitKey(0)
        # context = {"nid": nid,"date_of_birth": dob,"mother_name":nom}
    return Response(data=context, status=200)
