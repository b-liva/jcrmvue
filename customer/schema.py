import graphql
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from customer.models import Customer

class CustomerType(DjangoObjectType):

    class Meta:
        model = Customer
        interfaces = (graphene.Node,)

        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }


class Query(graphene.ObjectType):
    customer = graphene.Field(CustomerType,
                          id=graphene.ID(),
                          name=graphene.String(),
                          code=graphene.Int(),
                          )
    customers = DjangoFilterConnectionField(CustomerType)

    def resolve_customers(self, info):
        # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task')
        # if not can_see:
        #     return None
        # print(f"can see: {# can_see}")
        return Customer.objects.all()

    def resolve_customer(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            customer = Customer.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return customer
        if name is not None:
            return Customer.objects.get(name=name)
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
