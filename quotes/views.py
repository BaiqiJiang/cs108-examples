from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote
import random

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