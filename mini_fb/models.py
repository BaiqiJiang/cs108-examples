from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Model the data attributes of Facebook users'''

    # data attributes
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of these data attributes.'''

        return f'{self.first_name}' + ' ' + f'{self.last_name}' + ', ' + f'{self.city}' + ', ' + f'{self.email_address}'
    
    def get_status_messages(self):
        '''Obtain status messages for this Profile.'''

        # use the object manager to filter Status by this users's pk:
        return StatusMessage.objects.filter(profile=self)


class StatusMessage(models.Model):
    '''Model the data attributes of Facebook status message.'''

    timestamp = models.TimeField(blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of these data attributes.'''

        return f'{self.timestamp}' + ' ' + f'"{self.message}"' + ' ' + f'{self.profile}'
