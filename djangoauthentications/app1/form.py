from django import forms
from .models import NewUser

class CustomUserCreationForm(forms.ModelForm):
    
    class Meta:
        model = NewUser
        fields = '__all__'