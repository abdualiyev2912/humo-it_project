from typing import Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from main.models import *

class PortfolioMainView(View):
    def get(self, request):
        return render(request, 'index.html', {
            "developers": Developer.objects.order_by('-experience')[:6],
            "portfolios": Portfolio.objects.all()[:3],
            "news": New.objects.all()[:3],
            "comments": Comment.objects.order_by("-created_at")[:3],
        })
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Sizning so'rovingi jo'natildi!")
            return redirect('main')  
        else:
            messages.error(request, "Iltimos, maydonlarni to'ldiring!")
            return render(request, 'index.html', {
                "developers": Developer.objects.order_by('-experience')[:6],
                "portfolios": Portfolio.objects.all()[:3],
                "news": New.objects.all()[:3],
                "comments": Comment.objects.order_by("-created_at")[:3],
            })
