import graphene

from django_graphql.api.files.schema import FileQueries, FileMutations


class Queries(FileQueries):
    hello = graphene.String(default_value="Hi!")

class Mutations(FileMutations):
    pass

schema = graphene.Schema(Queries, Mutations)
