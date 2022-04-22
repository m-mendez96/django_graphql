import pytest

from graphene_file_upload.django.testing import file_graphql_query


@pytest.fixture
def api_client(client):
    def func(*args, **kwargs):
        return file_graphql_query(*args, **kwargs, client=client)

    return func