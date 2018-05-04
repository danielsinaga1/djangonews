from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.

def home(request):
    return render_to_response("signup.html",
                              locals(), context_instance= RequestContext(request))