from django import forms
from .models import Message


class Messages(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
