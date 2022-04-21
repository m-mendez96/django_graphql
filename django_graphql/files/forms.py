from django.forms import ModelForm

from django_graphql.files.models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ["file"]
