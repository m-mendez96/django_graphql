from graphene.test import Client

from django_graphql.api.schema import schema


def test_hi():
    client = Client(schema)
    query = '''query { hello }'''
    executed = client.execute(query)
    assert executed == {
        'data': {
            'hello': 'Hi!'
        }
    }