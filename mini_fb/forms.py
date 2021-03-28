# mini_fb/forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new Profile object.'''
   
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.CharField(label="Birth Date", required=True)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email", required=True)
    image_url = forms.URLField(label='Image Url', required=True)

    class Meta:
        '''additional data about this form'''
        
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email_address', 'image_url']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update an exist Profile object.'''
   
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.CharField(label="Birth Date", required=True)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email", required=True)
    image_url = forms.URLField(label='Image Url', required=True)

    class Meta:
        '''additional data about this form'''
        
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email_address', 'image_url']

class CreateStatusMessageForm(forms.ModelForm):
    '''Allow the user to input status message.'''

    timestamp = forms.TimeField(required=True)

    class Meta:
        '''additional data about this form'''
        
        model = StatusMessage
        fields = ['timestamp','message']



