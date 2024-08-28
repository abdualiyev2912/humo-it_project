from django.contrib import admin
from portfolios.models import Portfolio, PortfolioImage, Developer, Contact, Comment

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    inlines = [PortfolioImageInline]
    


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'experience')
    search_fields = ('name', 'skills')

