from django.contrib import admin

from .models import UserDetail,Message,RoseRecord

admin.site.register(UserDetail)
admin.site.register(Message)
admin.site.register(RoseRecord)