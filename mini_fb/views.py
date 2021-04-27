from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
class ShowAllProfilesView(ListView):
    '''Display all Profiles.'''

    model = Profile                                       # retrieve Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    '''Display a profile.'''

    model = Profile                                       # retrieve Profile objects from the database
    template_name = "mini_fb/show_profile_page.html"      # delagate the display to this template
    context_object_name = "profile"                       # use this variable name in the template
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    '''Create a new profile and store it in the database.'''

    model = Profile # which model to create
    form_class = CreateProfileForm   # which form to use to create the Quote
    template_name = "mini_fb/create_profile_form.html"  # delegate the dispay to this template

class UpdateProfileView(UpdateView):
    '''Update an exist profile and store it in the database.'''

    model = Profile # which model to create
    form_class = UpdateProfileForm   # which form to use to create the Quote
    template_name = "mini_fb/update_profile_form.html"  # delegate the dispay to this template
    context_object_name = "ProfileUpdate"

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

class DeleteStatusMessageView(DeleteView):
    '''Delete an exist status message.'''

    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()
    # context_object_name = "profile"
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        context = super().get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['Profiles'] = st_msg

        return context
    
    def get_object(self):
        '''Return the object that should be deleted.'''
        # read the URL data values into variables
        status_pk = self.kwargs['status_pk']
        profile_pk = self.kwargs['profile_pk']
        # find the StatusMessage object, and return it
        st_msg_obj = StatusMessage.objects.get(pk=status_pk)

        return st_msg_obj
     
    def get_success_url(self):
        '''Return the URL to which we should be directed after the delete.'''
        
        profile_pk = self.kwargs['profile_pk']
        return reverse('show_profile_page', kwargs={'pk':profile_pk})
    
class ShowNewsFeedView(DetailView):
    ''' Show news feeds. '''

    model = Profile                                    # retrieve Profile objects from the database
    template_name = "mini_fb/show_news_feed.html"      # delagate the display to this template
    context_object_name = "profile"                    # use this variable name in the template

class ShowPossibleFriendsView(DetailView):
    ''' Show possible friends. '''

    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object_name = "prof"

def add_friend(request, profile_pk, friend_pk):
    '''The objective of this function is to process the add_friend request, to add a friend for a given profile.'''

    # find the Profile object which is adding the friend, and store it into a variable
    profile_obj_pk = Profile.objects.get(pk=profile_pk)
    # find the Profile object of the friend to add, and store it into another variable
    friend_obj_pk = Profile.objects.get(pk=friend_pk)
    # add that friend’s Profile into the profile.friends object (using the method add)
    profile_obj_pk.friends.add(friend_obj_pk)
    # save the profile object.
    profile_obj_pk.save()
    # return to the show profile page
    return redirect(reverse('show_profile_page', kwargs={'pk':profile_pk}))