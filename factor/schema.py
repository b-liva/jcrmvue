from graphene import Schema, ObjectType
import fund.schema
import request.schemas.schema
import customer.schema
import accounts.schema


class Query(
    request.schemas.schema.Query,
    fund.schema.Query,
    customer.schema.Query,
    accounts.schema.Query,
    ObjectType
):
    pass


class Mutation(
    request.schemas.schema.RequestAppMutations,
    ObjectType
):
    pass


schema = Schema(query=Query, mutation=Mutation)
# schema = Schema(query=Query)
