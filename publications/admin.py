from django.contrib import admin
from .models import Publication, Comment
"""  
admin.py - файл отвечающий за работу с админ-панелью
"""
admin.site.register(Publication) # регистрация модельки в админ-панели
admin.site.register(Comment)
