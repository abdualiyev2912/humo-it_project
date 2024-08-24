from django.urls import path
from portfolios.views import PortfolioListView, PortfolioDetailView, PortfolioMainView

urlpatterns = [
    path('', PortfolioMainView.as_view(), name='main'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio-list'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]
