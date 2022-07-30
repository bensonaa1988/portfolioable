from django.contrib import admin
from .models import Portfolio
from .models import Property

# 
class PropertyInline(admin.TabularInline):
    model = Property

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        PropertyInline,
    ]

admin.site.register(Portfolio)
admin.site.register(Property)