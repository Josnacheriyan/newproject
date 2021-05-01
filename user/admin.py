from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AddEvent)
admin.site.register(ImageUpload)
admin.site.register(Loging)