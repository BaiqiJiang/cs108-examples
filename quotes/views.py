from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Quote, Person
import random
from .forms import CreateQuoteForm, UpdateQuoteForm
# Create your views here.

class HomePageView(ListView):
    '''Show a listing of Quotes.'''
    model = Quote # retrieve Quote objects from the database
    template_name = "quotes/home.html"
    context_object_name = "quotes"

class QuotePageView(DetailView):
    '''Display a single quote obeject.'''
    model = Quote                           # retrieve Quote objects from the database
    template_name = "quotes/quote.html"      # delagate the display to this template
    context_object_name = "quote"           # use this variable name in the template

class RandomPageView(DetailView):
    '''Display a single quote obeject.'''
    model = Quote                           # retrieve Quote objects from the database
    template_name = "quotes/quote.html"      # delagate the display to this template
    context_object_name = "quote"           # use this variable name in the template

    def get_object(self):
        ''' Select one quote at random for display in the quote.html template. '''

        # obtain all quotes the object manager
        quotes = Quote.objects.all()
        # select one at random
        q = random.choice(quotes)
        return q

class PersonPageView(DetailView):
    '''Display a single Person obeject.'''
    
    model = Person                           # retrieve Quote objects from the database
    template_name = "quotes/person.html"      # delagate the display to this template
    context_object_name = "person"           # use this variable name in the template

class CreateQuoteView(CreateView):
    '''Create a new Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = CreateQuoteForm    # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html"  # delegate the dispay to this template

class UpdateQuoteView(UpdateView):
    '''Update a Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = UpdateQuoteForm    # which form to use to create the Quote
    template_name = "quotes/update_quote_form.html"  # delegate the dispay to this template