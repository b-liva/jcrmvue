import graphql
import graphene
from aniso8601 import parse_date
from graphene import Scalar
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
import jdatetime
from graphql.language import ast

from fund.models import Fund, Expense
from django_jalali.db import models as jmodels


class JDate(Scalar):
    """
    custom: The `Date` scalar type represents a Date
    value as specified by
    [iso8601](https://en.wikipedia.org/wiki/ISO_8601).
    """

    @staticmethod
    def serialize(date):
        print('satarted here...')
        print(f"type is : {type(date)}")
        if isinstance(date, jdatetime.datetime):
            date = date.date()
        assert isinstance(
            date, jdatetime.date
        ), 'Received not compatible...... some date "{}"'.format(repr(date))
        return date.isoformat()

    @classmethod
    def parse_literal(cls, node):
        if isinstance(node, ast.StringValue):
            return cls.parse_value(node.value)

    @staticmethod
    def parse_value(value):
        try:
            return parse_date(value)
        except ValueError:
            return None


class FundType(DjangoObjectType):

    class Meta:
        model = Fund
        interfaces = (graphene.Node,)

        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'summary': ['exact'],
        }


class ExpenseType(DjangoObjectType):

    class Meta:
        model = Expense
        interfaces = (graphene.Node,)

        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'summary': ['exact'],
        }


class Query(graphene.ObjectType):
    fund = graphene.Field(FundType,
                          id=graphene.ID(),
                          title=graphene.String(),
                          pub_date=graphene.DateTime(),
                          )
    # tasks = graphene.List(TaskType)
    funds = DjangoFilterConnectionField(FundType)

    exp = graphene.Field(ExpenseType,
                         id=graphene.ID(),
                         title=graphene.String(),
                         summary=graphene.String(),
                         )
    # tasks = graphene.List(TaskType)
    exps = DjangoFilterConnectionField(ExpenseType)

    def resolve_funds(self, info):
        # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task')
        # if not can_see:
        #     return None
        # print(f"can see: {# can_see}")
        return Fund.objects.all()

    def resolve_fund(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            fund = Fund.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return fund
        if title is not None:
            return Fund.objects.get(title=title)
        return None

    def resolve_exps(self, info):
        # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task')
        # if not can_see:
        #     return None
        # print(f"can see: {# can_see}")
        return Expense.objects.all()

    def resolve_exp(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            exp = Expense.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return exp
        if title is not None:
            return Expense.objects.get(title=title)
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
