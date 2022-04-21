from contextlib import nullcontext
import graphene

from graphene_file_upload.scalars import Upload

from django_graphql.files.forms import FileForm
from django_graphql.api.files.types import FileType


class FileUpload(graphene.Mutation):
    success = graphene.Boolean()
    file = graphene.Field(FileType)

    class Arguments:
        file = Upload(required=True)

    def mutate(self, info, file, **kwargs):
        if file != None:
            data = {"file": file}
            file_form = FileForm(None, data)
            if not file_form.is_valid():
                return FileUpload(success=False)
            else:
                __file = file_form.save()
                return FileUpload(success=True, file=__file)
        return FileUpload(success=False)
