from django import forms
from upimage.models import *
class UploadForm(forms.ModelForm):
 class Meta:
  model=Student
  fields='__all__'
