# models.py
# Author: Baiqi Jiang
# Description: Create different models for using. One of the most important part.
# Date: 2021.4

from django.db import models
from django.urls import reverse

# Create your models here.

class Phylum(models.Model):
    '''Represent a phylum in Biology.'''

    # data attributes

    phylum_name = models.TextField(blank=True)
    phylum_introduction = models.TextField(blank=True)
    phylum_image = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of these data attributes.'''

        return f'{self.phylum_name}'

    def get_classes(self):
        '''Find classes that belong to this phylum.'''

        return Class.objects.filter(phylum=self)
    
    
    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_phylum', kwargs={'pk':self.pk})

class UserProfile(models.Model):
    '''Represent a user profile.'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    grade = models.TextField(blank=True)
    country = models.TextField(blank=True)
    birth_date = models.DateField(blank=True)
    reg_time = models.DateTimeField(default="")
    email_address = models.EmailField(blank=True)
    portrait = models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of these data attributes.'''
        
        return f'{self.first_name}' + ' ' + f'{self.last_name}' + f'{self.portrait}'

    def get_user_contrib_classes(self):
        '''Return the most recent classes edited by a user, and ordered those by time.'''

        return Class.objects.filter(update_user=self).order_by("-update_time")  # order_by("-update_time)" is used to order classes by their update time
    
    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_profile', kwargs={'pk':self.pk})
    
class Class(models.Model):
    '''Represent a class belongs to a phylum in Biology.'''
    
    phylum = models.ForeignKey(Phylum, on_delete=models.CASCADE, null=True)
    update_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="", null=True)
    class_name = models.TextField(blank=True)
    class_introduction = models.TextField(blank=True)
    class_image = models.URLField(blank=True)
    update_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        '''Return a string representation of these data attributes.'''

        return 'class ' + f'{self.class_name}' + ',' + 'belongs to phylum ' + f'{self.phylum}' + ',' + ' updated on ' + f'{self.update_time}' + ', by ' + f'{self.update_user}'
    
    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_phylum', kwargs={'pk':self.phylum.pk})
    

