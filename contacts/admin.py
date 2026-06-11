from django.contrib import admin
from .models import Contact
from .models import ContactImage

admin.site.register(Contact)
admin.site.register(ContactImage)