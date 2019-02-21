from graphene import Schema, ObjectType
import fund.schema
import request.schemas.schema
import customer.schema


class Query(
    request.schemas.schema.Query,
    fund.schema.Query,
    customer.schema.Query,
    ObjectType
):
    pass


schema = Schema(query=Query)
