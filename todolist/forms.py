from django import forms
from django.forms import ModelForm
from todolist.models import *

class TodolistForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'size':'50'}))
    description= forms.CharField(widget=forms.Textarea(attrs={'size': '100'}))

    class Meta:
        model = Task
        fields = ('title', 'description')