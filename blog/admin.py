from django.contrib import admin

from blog.models import *
admin.site.register(Articles)
admin.site.register(Category)