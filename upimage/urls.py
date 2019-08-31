from django.urls import path,include
from upimage.views import *

app_name="upimages"
urlpatterns=[
path('up/',upimages),
path('display/',display,name='disp')
]
