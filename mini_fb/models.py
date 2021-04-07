from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    '''Model the data attributes of Facebook users'''

    # data attributes
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    birth_date = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        '''Return a string representation of these data attributes.'''

        return f'{self.first_name}' + ' ' + f'{self.last_name}' + ', ' + f'{self.city}' + ', ' f'{self.birth_date}'+ ', ' + f'{self.email_address}'
    def get_status_messages(self):
        '''Obtain status messages for this Profile.'''

        # use the object manager to filter Status by this users's pk:
        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        # "profile/<int:pk>"
        return reverse('show_profile_page', kwargs={'pk':self.pk})
    
    def get_friends(self):
        '''  Return all friends for this Profile. '''
        
        return self.friends.all()
    
    def get_news_feed(self):
        ''' Obtain and return the news feed items. '''

        peeps = self.friends.all()
        news = StatusMessage.objects.filter(profile__in=peeps).order_by("-timestamp")
        return news
    
    def get_friend_suggestions(self):
        '''Obtain and return a QuerySet of all Profile that could be added as friends.'''

        possible_friends = Profile.objects.exclude(pk__in=self.get_friends())
        return possible_friends

class StatusMessage(models.Model):
    '''Model the data attributes of Facebook status message.'''

    timestamp = models.TimeField(blank=True)
    message = models.TextField(blank=True)
    image_file = models.ImageField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of these data attributes.'''

        return f'{self.timestamp}' + ' ' + f'"{self.message}"' + ' ' + f'{self.profile}' + ' ' + f'{self.image_file}'
