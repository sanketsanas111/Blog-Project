from dataclasses import field
import imp
from django import forms
from blogapp.models import Add_Blog

class Add_Blog_Form(forms.ModelForm):
    class Meta:
        model = Add_Blog
        exclude = ("User", )