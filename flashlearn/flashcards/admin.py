from django.contrib import admin

from .models import *

admin.site.register(Card)
admin.site.register(Document)
admin.site.register(Scan)
admin.site.register(UserDocument)
