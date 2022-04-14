from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question, Response

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Response)
