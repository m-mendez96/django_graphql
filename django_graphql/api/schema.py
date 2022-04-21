import graphene

from django_graphql.api.files.schema import FileQueries


class Queries(FileQueries):
    hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(Queries)
