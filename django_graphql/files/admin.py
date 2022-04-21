from django.contrib import admin

from django_graphql.files.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass