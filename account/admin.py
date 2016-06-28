from django.contrib import admin

# Register your models here.
from .models import Personne

class AccountModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "prenom"]
    class Meta:
        model = Personne

admin.site.register(Personne)