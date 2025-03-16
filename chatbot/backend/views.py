from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def backend(request, slug=None):
    return HttpResponse("<p>From backend</p>")

import json
from .responses import bot_response

def get_chat_response(request, slug=None):
    data = request.GET
    message = data.get("message")
    
    print(data)
    print(message)
    
    response = {
        'message': bot_response(message)
    }

    return HttpResponse(json.dumps(response))

def get_first_response(request, slug=None):
    response = {
        "message": "Hello there!"
    }
    return HttpResponse(json.dumps(response))