from typing import Any
from django import forms

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('Start with a')
    
def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('length is greater than 5')
class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_a,validate_for_len])
    Sprincipal=forms.CharField(validators=[validate_for_a])
    Slocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    
    def clean_botcatcher(self):
        b=self.cleaned_data["botcatcher"]
        if len(b)>0:
            raise forms.ValidationError("bot")
    

    def clean(self):
        em=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if em!=re:
            raise forms.ValidationError('Email Doesnot match')