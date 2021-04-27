# admin.py
# Author: Baiqi Jiang
# Description: Register models into the django admin
# Date: 2021.4

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Phylum)
admin.site.register(Class)
admin.site.register(UserProfile)