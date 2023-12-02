from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarDealer
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
   
# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        dealer_list = CarDealer.objects
        context['dealer_list'] = dealer_list
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == 'GET':
        try:
            dealer = CarDealer.objects.get(pk=dealer_id)
            context['dealer'] = dealer
            # Use render() method to generate HTML page by combining                                                                                                                 
            # template and context                                                                                                                                                   
            return render(request, 'djangoapp/dealer_details.html', context)
        except CarDealer.DoesNotExist:
            # If course does not exist, throw a Http404 error                                                                                                                        
            raise Http404("No dealer matches the given id.") 

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    # If request method is POST                                                                                                                                                      
    if request.method == 'POST':
        # First try to read the course object                                                                                                                                        
        # If could be found, raise a 404 exception                                                                                                                                   
        dealer = get_object_or_404(Course, pk=dealer_id)
        # Increase the enrollment by 1                                                                                                                                               
        dealer.total_dealers += 1
        dealer.save()
        # Return a HTTP response redirecting user to course list view                                                                                                                
        return HttpResponseRedirect(reverse(viewname='djangoapp:get_dealerships'))