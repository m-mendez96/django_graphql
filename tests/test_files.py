import json
import pytest

from graphene.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile

from django_graphql.api.schema import schema


pytestmark = pytest.mark.django_db

def test_hi():
    client = Client(schema)
    query = '''query { hello }'''
    executed = client.execute(query)
    assert executed == {
        'data': {
            'hello': 'Hi!'
        }
    }

def test_file_upload(api_client, tmp_path):
    tmp_files = tmp_path / "files"
    tmp_files.mkdir()
    file = tmp_files / "test_file.txt"
    file.write_text("This is a test file.")
    with open(file, "r") as f:
        test_file = SimpleUploadedFile(
            name="test_file.txt", content=f.read().encode("utf-8")
        )
        response = api_client(
            '''
            mutation fileUpload($file: Upload!){ 
                fileUpload(file:$file){ 
                    success, 
                    file { 
                        id, 
                        file, 
                        createdAt
                    }
                }
            }
            ''',
            op_name='fileUpload',
            files={'file': test_file}
        )
        content = json.loads(response.content)
        assert content["data"]["fileUpload"]["success"] == True
        assert content["data"]["fileUpload"]["file"] != None
        assert content["data"]["fileUpload"]["file"]["id"] == '1'
