from django.contrib import admin
from .models import ContactMessage
# Register your models here.


class ContactTable(admin.ModelAdmin):
    list_display = ('id','name','email','subject','message')

admin.site.register(ContactMessage,ContactTable)

