# views.py
# Author: Baiqi Jiang
# Description: Create different views for web displaying.
# Date: 2021.4

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Phylum, Class, UserProfile
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CreateClassForm, UpdateClassForm, CreateProfileForm, UpdateProfileForm
# Create your views here.

class ShowAllPhylaView(ListView):
    '''Display all phyla.'''

    model = Phylum                                      # retrieve Phylum objects from the database
    template_name = "project/show_all_phyla.html"       # delagate the display to this template
    context_object_name = "phyla"                       # use this variable name in the template

class ShowPhylumView(DetailView):
    '''Display a phylum.'''

    model = Phylum     
    template_name = "project/show_phylum.html"
    context_object_name = "phylum"

class HomePageView(ListView):
    '''Show a home page.'''

    model = Phylum                                       # In fact, I do not use a model in home.html     
    template_name = "project/home.html"                  # But in order to create a view, I need to retrieve model objects
    context_object_name = "Phy"                          # Model and context object name can be ignored here, they do nothing 

class ShowClassView(DetailView):
    '''Display a class.'''

    model = Class
    template_name = "project/show_class.html"
    context_object_name = "class"

    def get_object(self):
        '''Return the object that should be displayed.'''
        
        # read the URL data values into variables
        phylum_pk = self.kwargs['phylum_pk']
        class_pk = self.kwargs['class_pk']
        # find the Class object, and return it
        class_obj = Class.objects.get(pk=class_pk)

        return class_obj

class ShowAllClassesView(ListView):
    '''Display all classes.'''

    model = Class
    template_name = "project/show_all_classes.html"
    context_object_name = "Class"

class HelpPageView(ListView):
    '''Show a help page.'''
    
    model = Class                                           # In fact, I do not use a model in help.html                                         
    template_name = "project/help.html"                     # But in order to create a view, I need to retrieve model objects
    context_object_name = "Cl."                             # Model and context object name can be ignored here, they do nothing 

class CreateClassView(CreateView):
    '''Create a new class and store it in the database.'''

    model = Class                                           # which model to create
    form_class = CreateClassForm                            # which form to use to create the Class
    template_name = "project/create_class_form.html"        # delegate the dispay to this template

class UpdateClassView(UpdateView):
    '''Update an exist class and store it in the database.'''

    model = Class 
    form_class = UpdateClassForm   
    template_name = "project/update_class_form.html"  
    context_object_name = "ClassUpdate"
    
    def get_object(self):
        '''Return the object that should be displayed.'''
        
        # read the URL data values into variables
        phylum_pk = self.kwargs['phylum_pk']
        class_pk = self.kwargs['class_pk']
        # find the Class object, and return it
        class_obj = Class.objects.get(pk=class_pk)

        return class_obj

class DeleteClassView(DeleteView):
    '''Delete an exist class.'''

    template_name = "project/delete_class_form.html"
    queryset = Class.objects.all()                          # Use queryset to get all class objects
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Class record to display for this page view
        context = super().get_context_data(**kwargs)
        # get objects that we need
        cla_ss = Class.objects.get(pk=self.kwargs['class_pk'])
        # store those objects to a dictionary, and return it
        context['Class'] = cla_ss

        return context
    
    def get_object(self):
        '''Return the object that should be displayed.'''
        
        # read the URL data values into variables
        profile_pk = self.kwargs['phylum_pk']
        class_pk = self.kwargs['class_pk']
        # find the Class object, and return it
        class_obj = Class.objects.get(pk=class_pk)

        return class_obj
     
    def get_success_url(self):
        '''Return the URL to which we should be directed after the delete.'''
        
        phylum_pk = self.kwargs['phylum_pk']
        return reverse('show_phylum', kwargs={'pk':phylum_pk})

class ShowAllProfileView(ListView):
    '''Display all users.'''

    model = UserProfile
    template_name = "project/show_all_profile.html"
    context_object_name = "profile"

class ShowProfileView(DetailView):
    '''Display a profile.'''

    model = UserProfile
    template_name = "project/show_profile.html"
    context_object_name = "profile"

class CreateProfileView(CreateView):
    '''Create a new profile and store it in the database.'''

    model = UserProfile
    form_class = CreateProfileForm   
    template_name = "project/create_profile_form.html"  

class UpdateProfileView(UpdateView):
    '''Update an exist profile and store it in the database.'''

    model = UserProfile
    form_class = UpdateProfileForm   
    template_name = "project/update_profile_form.html"
    context_object_name = "ProfileUpdate"
    
    def get_object(self):
        '''Return the object that should be displayed.'''
        
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        # find the UserProfile object, and return it
        profile_obj = UserProfile.objects.get(pk=profile_pk)

        return profile_obj

class DeleteProfileView(DeleteView):
    '''Delete an exist profile.'''

    template_name = "project/delete_profile_form.html"
    queryset = UserProfile.objects.all()
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        context = super().get_context_data(**kwargs)
        pro_file = UserProfile.objects.get(pk=self.kwargs['profile_pk'])
        context['profile'] = pro_file

        return context
    
    def get_object(self):
        '''Return the object that should be displayed.'''
        
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        # find the UserProfile object, and return it
        profile_obj = UserProfile.objects.get(pk=profile_pk)

        return profile_obj

    def get_success_url(self):
        '''Return the URL to which we should be directed after the delete.'''
        
        return reverse('show_all_profiles')

class ShowTermsOfUsePageView(ListView):
    '''Show a terms of use page.'''
    
    model = Class                                   # In fact, I do not use a model in terms_of_use.html
    template_name = "project/terms_of_use.html"     # But in order to create a view, I need to retrieve model objects 
    context_object_name = "Cla."                    # Model and context object name can be ignored here, they do nothing 

class WriteCommentsView(ListView):
    '''Let the user to write comments and rate my website.'''
    
    model = Class                                   # In fact, I do not use a model in comments.html
    template_name = "project/comments.html"         # But in order to create a view, I need to retrieve model objects 
    context_object_name = "Cla."                    # Model and context object name can be ignored here, they do nothing 