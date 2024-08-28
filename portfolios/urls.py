from django.urls import path
from portfolios.views import PortfolioMainView

urlpatterns = [
    path('', PortfolioMainView.as_view(), name='main'),
]
