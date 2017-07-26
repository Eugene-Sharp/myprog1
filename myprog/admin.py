from django.contrib import admin
from myprog.models import Tweet
from myprog.models import HashTag
#Register your models here,
admin.site.register(Tweet)
admin.site.register(HashTag)