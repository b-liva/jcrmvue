import graphql
import graphene
from aniso8601 import parse_date
from graphene import Scalar
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
import jdatetime
from graphql.language import ast

from request.models import Requests, ReqSpec, Xpref, PrefSpec
from django_jalali.db import models as jmodels


class RequestType(DjangoObjectType):
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


class ProformaType(DjangoObjectType):
    proforma_sum = graphene.Float(source='proforma_sum')
    url = graphene.String(source='get_absolute_url')

    class Meta:
        model = Xpref
        interfaces = (graphene.Node,)

        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
            'number': ['exact'],
        }


class Query(graphene.ObjectType):
    order = graphene.Field(RequestType,
                          id=graphene.ID(),
                          number=graphene.Int(),
                          )
    # tasks = graphene.List(TaskType)
    orders = DjangoFilterConnectionField(RequestType)

    proforma = graphene.Field(ProformaType,
                         id=graphene.ID(),
                         req_id=graphene.ID(),
                         number=graphene.Int(),
                         summary=graphene.String(),
                         )
    # tasks = graphene.List(TaskType)
    proformas = DjangoFilterConnectionField(ProformaType)

    def resolve_orders(self, info):
        # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task')
        # if not can_see:
        #     return None
        # print(f"can see: {# can_see}")
        return Requests.objects.all()

    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')
        number = kwargs.get('number')

        if id is not None:
            order = Requests.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return order
        if number is not None:
            return Requests.objects.get(number=number)
        return None

    def resolve_proformas(self, info):
        # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task')
        # if not can_see:
        #     return None
        # print(f"can see: {# can_see}")
        return Xpref.objects.all()

    def resolve_proforma(self, info, **kwargs):
        id = kwargs.get('id')
        number = kwargs.get('number')

        if id is not None:
            proforma = Xpref.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return proforma
        if number is not None:
            return Xpref.objects.get(number=number)
        return None


schema = graphene.Schema(query=Query)


def has_perm_or_is_owner(user_obj, permissions, instance=None, colleague=None):
    if user_obj.is_superuser:
        return True
    if colleague is not None and colleague:
        if hasattr(instance, 'is_active'):
            return instance.is_active
        else:
            return colleague
    if instance is not None:
        print(user_obj)
        # print(instance.owner)
        # if user_obj == instance.owner:
        #     if hasattr(instance, 'is_active'):
        #         return instance.is_active
        #     else:
        #         return True
        if hasattr(instance, 'todo'):
            if user_obj == instance.todo.owner:
                return True
        elif hasattr(instance, 'req_id') and hasattr(instance.req_id, 'customer'):
            if user_obj == instance.req_id.customer.user:
                return True
        elif hasattr(instance, 'xpref_id') and hasattr(instance.xpref_id.req_id, 'customer'):
            if user_obj == instance.xpref_id.req_id.customer.user:
                return True
        if instance.__class__.__name__ == 'User':
            return user_obj == instance
    return user_obj.has_perm(permissions)
