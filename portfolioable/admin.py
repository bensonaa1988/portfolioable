from django.contrib import admin
from .models import Portfolio
from .models import Property

admin.site.register(Portfolio)
admin.site.register(Property)