import graphql
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from accounts.models import User


class UserType(DjangoObjectType):

    class Meta:
        model = User
        interfaces = (graphene.Node,)

        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains', 'istartswith'],
            'sales_exp': ['exact'],
            'is_customer': ['exact'],
        }


class Query(graphene.ObjectType):
    user = graphene.Field(UserType,
                              id=graphene.ID(),
                              username=graphene.String(),
                              last_name=graphene.String(),
                              )
    users = DjangoFilterConnectionField(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        last_name = kwargs.get('last_name')

        if id is not None:
            user = User.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return user
        if name is not None:
            user = User.objects.get(name=name)

            return user
        if last_name is not None:
            user = User.objects.get(last_name=last_name)
            return user
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
