from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, View
from portfolios.models import Portfolio

class PortfolioMainView(View):
    def get(self, request):
        return render(request, 'index.html', {})
