from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.urls import reverse
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def home(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request=request , template_name='index.html')
    
    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        message = f"Name🫡: {name}, \n Email📩: {email}, \n Message🔤: {message}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }
        
        requests.post(url, json=payload)
        return render(request=request , template_name="index.html")
    
def components(request: HttpRequest) -> HttpResponse:
    return render(request=request , template_name="components.html")