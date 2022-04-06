from django.contrib import admin
from .models import User, Question, Response

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Response)
