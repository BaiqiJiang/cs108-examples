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