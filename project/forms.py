# forms.py
# Author: Baiqi Jiang
# Description: Create different forms for different views. One of the most important part.
# Date: 2021.4

from django import forms
from .models import Phylum, Class, UserProfile

class CreateClassForm(forms.ModelForm):
    '''A form to create a new Class object.'''
    
    phylum = forms.ModelChoiceField(queryset=Phylum.objects.all())   # ModelChoiceField and queryset will let user to choose a object from the queryset
    update_user = forms.ModelChoiceField(queryset=UserProfile.objects.all())
    class_name = forms.CharField(label="Class Name", required=True)
    class_introduction = forms.CharField(label="Class Introduction", required=True, widget=forms.Textarea)
    class_image = forms.URLField(label="Class Image", required=False)
    update_time = forms.DateTimeField(label="Update Time", required=True)

    class Meta:
        '''additional data about this form'''
        
        model = Class
        fields = ['phylum', 'update_user', 'class_name', 'class_introduction', 'class_image', 'update_time']

class UpdateClassForm(forms.ModelForm):
    '''A form to update an exist Class object.'''

    update_user = forms.ModelChoiceField(queryset=UserProfile.objects.all())
    class_introduction = forms.CharField(label="Class Introduction", required=True, widget=forms.Textarea)
    class_image = forms.URLField(label="Class Image", required=False)
    update_time = forms.DateTimeField(label="Update Time", required=True)

    class Meta:
        '''additional data about this form'''
        
        model = Class
        fields = ['update_user', 'class_introduction', 'class_image', 'update_time']

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new Profile object.'''

    first_name = forms.CharField(label="First Name",  required=True)
    last_name = forms.CharField(label="Last Name",  required=True)
    grade = forms.CharField(label="Grade",  required=True)
    country = forms.CharField(label="Country",  required=True)
    birth_date = forms.DateField(label="Birthday",  required=True)
    reg_time = forms.DateTimeField(label="Registration Time",  required=True)
    email_address = forms.EmailField(label="Email Address",  required=True)
    portrait = forms.ImageField(label="Your Portrait (Optional)", required=False)

    class Meta:
        '''additional data about this form'''
        
        model = UserProfile
        fields = ['first_name', 'last_name', 'grade', 'country', 'birth_date', 'reg_time', 'email_address','portrait']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update an exist Profile object.'''

    grade = forms.CharField(label="Grade",  required=True)
    country = forms.CharField(label="Country",  required=True)
    email_address = forms.EmailField(label="Email Address",  required=True)
    portrait = forms.ImageField(label="Your Portrait (Optional)", required=False)

    class Meta:
        '''additional data about this form'''
        
        model = UserProfile
        fields = ['grade', 'country', 'email_address','portrait']

