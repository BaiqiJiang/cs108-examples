from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.
class ShowAllProfilesView(ListView):
    '''Display all Profiles.'''

    model = Profile # retrieve Profile objects from the database
    template_name = "profiles/show_all_profiles.html"
    context_object_name = "profiles"