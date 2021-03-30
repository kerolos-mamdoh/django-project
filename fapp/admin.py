from django.contrib import admin
from .models import addproject,comment_project,donnate
# Register your models here.
admin.site.register(addproject)
admin.site.register(comment_project)
admin.site.register(donnate)