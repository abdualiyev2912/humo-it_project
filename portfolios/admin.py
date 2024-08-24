from django.contrib import admin
from portfolios.models import Portfolio, PortfolioImage

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]

admin.site.register(Portfolio, PortfolioAdmin)