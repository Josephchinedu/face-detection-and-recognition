from django import forms
from .models import Records

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = '__all__'