from django.shortcuts import render
from django.http import HttpResponse
from upimage.forms import *

def upimages(request):
 form=UploadForm()
 if request.method=="POST":
  print("post")
  form=UploadForm(request.POST,request.FILES)
  if form.is_valid():
   form.save()
   return HttpResponse("success")
 return render(request,"upimages/upload.html",{'form':form})
def display(request):
 up_images=Student.objects.all()
 return render(request,"upimages/display.html",{'up_images':up_images})
