from django.contrib import admin

from .models import UserDetail,Message,RoseRecord,YellowRoseRecord

admin.site.register(UserDetail)
admin.site.register(Message)
admin.site.register(RoseRecord)
admin.site.register(YellowRoseRecord)