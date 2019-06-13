from django.contrib import admin
from back.api.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('user', 'instuser', 'email', 'coin')
    list_display = ['instuser', 'email']
    search_fields = ('instuser', 'email')

# Register your models here.
