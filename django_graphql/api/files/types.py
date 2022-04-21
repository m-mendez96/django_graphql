import graphene

from graphene_django import DjangoObjectType

from django_graphql.files.models import File


class FileType(DjangoObjectType):
    class Meta:
        model = File
        description = "Represents a file."
        only_fields = ("id", "file", "created_at")
        