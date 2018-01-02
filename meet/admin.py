from django.contrib import admin
from meet.models import Meet
from meet.models import Meetmember

# Register your models here.

admin.site.register(Meet)
admin.site.register(Meetmember)
