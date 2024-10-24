from django.contrib import admin

# Aqui registramos os models.

from django.contrib import admin
from .models import User

admin.site.register(User)
