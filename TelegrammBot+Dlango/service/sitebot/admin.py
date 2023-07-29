from django.contrib import admin
from .models import ListCommand, TgUser, MessageUser

admin.site.register(ListCommand)
admin.site.register(TgUser)
admin.site.register(MessageUser)