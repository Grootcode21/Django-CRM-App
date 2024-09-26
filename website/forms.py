from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    first_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

def __init__(self,*args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder']  = 'User name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"> <small>Required. 150 characters or fewer-  Letters, digits and @/./+/-/_ only.</small></span>'




    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder']  = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<span class="form-text text-muted"> <small><li>Your password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.</li><li>Your password can\'t be similar to your personal info</li><li>Your password can\'t be entirely numeric</li></small></span>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder']  = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted" <small>Enter password as before, for verification</small></span'
   
    
# Create add record form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),label="")
    last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}),label="")
    email = forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}),label="")
    phone_number = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}),label="")
    address = forms.CharField(required=True,widget=forms.widgets.Textarea(attrs={"placeholder":"Address", "class":"form-control"}),label="")
    city = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}),label="")
    state = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}),label="")
    zip_code = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code", "class":"form-control"}),label="")

    class Meta:
        model = Record
        exclude = ("user",)