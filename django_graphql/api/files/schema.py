import graphene

from django_graphql.api.files.types import FileType
from django_graphql.files.models import File


class FileQueries(graphene.ObjectType):
    file = graphene.Field(FileType, id = graphene.ID(required=True), description="Retrive a file.")
    all_files = graphene.List(FileType, description="List all files.")

    def resolve_file(self, info, id):
        return File.objects.get(id=id)

    def resolve_all_files(self, info):
        return File.objects.all()
