import graphene
from graphene_django.types import DjangoObjectType
from request.models import Requests, ReqSpec, Xpref, PrefSpec, Payment


class RequestNode(DjangoObjectType):

    total_kw = graphene.Float(source='total_kw')
    pub_date_pretty = graphene.String(source='pub_date_pretty')
    persian_date = graphene.String(source='persian_date')
    url = graphene.String(source='get_absolute_url')

    class Meta:
        model = Requests
        interfaces = (graphene.Node,)

        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
            'number': ['exact'],
        }

    @classmethod
    def get_node(cls, info, id):
        print(f"this is get node id: {id}")
        try:
            return Requests.objects.get(pk=id)
        except Requests.DoesNotExist:
            return None


class ReqSpecNode(DjangoObjectType):

    class Meta:
        model = ReqSpec
        interfaces = (graphene.Node,)

        filter_fields = {
            'kw': ['exact', 'icontains', 'istartswith'],
            'rpm': ['exact'],
            'qty': ['exact'],
        }


class ProformaNode(DjangoObjectType):
    proforma_sum = graphene.Float(source='proforma_sum')
    url = graphene.String(source='get_absolute_url')

    class Meta:
        model = Xpref
        interfaces = (graphene.Node,)

        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
            'number': ['exact', 'icontains', 'istartswith'],
        }


class PaymentNode(DjangoObjectType):
    payment_sum = graphene.Float(source='payment_sum')
    url = graphene.String(source='get_absolute_url')

    class Meta:
        model = Payment
        interfaces = (graphene.Node,)

        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
            'number': ['exact'],
        }


class PrefSpecNode(DjangoObjectType):

    class Meta:
        model = PrefSpec
        interfaces = (graphene.Node,)

        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
        }
