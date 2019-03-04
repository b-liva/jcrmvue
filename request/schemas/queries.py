import graphene
from request.schemas.types import RequestNode, ReqSpecNode, ProformaNode


class HotPrs(graphene.ObjectType):
    kw = graphene.Int()
    rpm = graphene.Int()
    qty = graphene.Int()


class DailyKw(graphene.ObjectType):
    date = graphene.String()
    kw = graphene.Float()


class DailyProforma(graphene.ObjectType):
    date = graphene.String()
    count = graphene.Float()
    sum = graphene.Float()


class DailyPayment(graphene.ObjectType):
    date = graphene.String()
    sum = graphene.Float()


class SearchResult(graphene.Union):
    class Meta:
        types = (RequestNode, ReqSpecNode, ProformaNode)
