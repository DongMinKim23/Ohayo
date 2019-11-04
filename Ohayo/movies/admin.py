from django.contrib import admin
from .models import Keyword,Movie,Image
# Register your models here.
admin.site.register(Keyword)
admin.site.register(Movie)
admin.site.register(Image)