import graphene
from graphene_django.filter import DjangoFilterConnectionField
from django.db import models

from request.schemas.types import (
    RequestNode,
    ReqSpecNode,
    ProformaNode,
    PaymentNode,
    PrefSpecNode
)
from request.schemas.queries import (
    HotPrs,
    DailyKw,
    DailyProforma,
    DailyPayment
)
from request.schemas.mutations import (
    RequestMutation,
    SpecMutation,
    ProformaMutation,
    ProformaPriceMutation,
    PaymentMutation,
)

from request.models import (
    Requests,
    ReqSpec,
    Xpref,
    PrefSpec,
    Payment
)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    def __init__(self, *args, **kwargs):
        super(Query, self).__init__(self, *args, **kwargs)
        # self.create_resolve_functions()

    # order = graphene.Field(RequestNode,
    #                       id=graphene.ID(),
    #                       number=graphene.Int(),
    #                       )
    """graphene.Node === graphene.relay.Node"""
    order = graphene.Node.Field(RequestNode,
                                number=graphene.Int(),
                                )
    # tasks = graphene.List(TaskType)
    orders = DjangoFilterConnectionField(RequestNode)
    Specs = DjangoFilterConnectionField(ReqSpecNode)

    proformaNode = graphene.Node.Field(ProformaNode)
    proforma = graphene.Field(ProformaNode,
                              req_id=graphene.ID(),
                              number=graphene.Int(),
                              summary=graphene.String(),
                              )

    payment = graphene.Node.Field(PaymentNode,
                                  id=graphene.ID(),
                                  xpref_id=graphene.ID(),
                                  number=graphene.Int(),
                                  summary=graphene.String(),
                                  )

    pref_spec = graphene.Node.Field(PrefSpecNode,
                                    id=graphene.ID(),
                                    xpref_id=graphene.ID(),
                                    kw=graphene.Float(),
                                    )
    # tasks = graphene.List(TaskType)
    proformas = DjangoFilterConnectionField(ProformaNode)
    payments = DjangoFilterConnectionField(PaymentNode)
    pref_specs = DjangoFilterConnectionField(PrefSpecNode)

    orders_count = graphene.Float()
    routine_count = graphene.Float()
    project_count = graphene.Float()
    services_count = graphene.Float()
    ex_count = graphene.Float()
    routine_qty = graphene.Float()
    project_qty = graphene.Float()
    services_qty = graphene.Float()
    ex_qty = graphene.Float()
    routine_kw = graphene.Float()
    services_kw = graphene.Float()
    project_kw = graphene.Float()
    ex_kw = graphene.Float()
    hot_prodocuts = graphene.List(HotPrs)
    daily_kw = graphene.List(DailyKw)
    daily_proforma = graphene.List(DailyProforma)
    daily_payment = graphene.List(DailyPayment)

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

    def resolve_pref_spec(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            pref_spec = PrefSpec.objects.get(pk=id)
            # can_see = has_perm_or_is_owner(info.context.user, 'task.add_task', task)
            # if not can_see:
            #     raise Exception('nothing to show.')
            #     return None
            return pref_spec
        return None

    # def create_resolve_functions(self):
    #     func_template = """def resolve_%s_count(self, info):
    #     count = find_count('%s')
    #     return count
    #     """
    #     d = {
    #         'routine': 'روتین',
    #         'project': 'پروژه',
    #         'services': 'تعمیرات',
    #         'ex': 'ضد انفجار',
    #     }
    #
    #     for key, value in d.items():
    #         print(func_template % (key, value))

    def resolve_routine_count(self, info):
        count = find_count('روتین')
        return count

    def resolve_project_count(self, info):
        count = find_count('پروژه')
        return count

    def resolve_services_count(self, info):
        count = find_count('تعمیرات')
        return count

    def resolve_ex_count(self, info):
        count = find_count('ضد انفجار')
        return count

    def resolve_routine_qty(self, info):
        qty = find_count('روتین')
        return qty

    def resolve_project_qty(self, info):
        qty = find_count('پروژه')
        return qty

    def resolve_services_qty(self, info):
        qty = find_count('تعمیرات')
        return qty

    def resolve_ex_qty(self, info):
        qty = find_count('ضد انفجار')
        return qty

    def resolve_routine_kw(self, info):
        kw = find_kw('روتین')
        return kw

    def resolve_project_kw(self, info):
        kw = find_kw('پروژه')
        return kw

    def resolve_services_kw(self, info):
        kw = find_kw('تعمیرات')
        return kw

    def resolve_ex_kw(self, info):
        kw = find_kw('ضد انفجار')
        return kw

    def resolve_hot_products(self, info, *args, **kwargs):
        hot_products = ReqSpec.objects \
            .exclude(type__title='تعمیرات') \
            .exclude(type__title='سایر') \
            .filter(is_active=True) \
            .filter(kw__gt=0) \
            .values('kw', 'rpm') \
            .annotate(reqspec_qty=models.Sum('qty')) \
            .order_by('reqspec_qty').reverse()
        print(hot_products['reqspec_qty'])
        return hot_products['reqspec_qty']

    def resolve_hot_prodocts_qty(self):
        hot_products = self.resolve_hot_products()
        total_qty = hot_products.aggregate(models.Sum('reqspec_qty'))
        return total_qty

    def resolve_hot_prodocuts(self, info):

        hot_products = ReqSpec.objects \
            .exclude(type__title='تعمیرات') \
            .exclude(type__title='سایر') \
            .filter(is_active=True) \
            .filter(kw__gt=0) \
            .values('kw', 'rpm') \
            .annotate(qty=models.Sum('qty')) \
            .order_by('qty').reverse()

        results = []  # Create a list of Dictionary objects to return

        # Now iterate through your dictionary to create objects for each item
        for x in hot_products:
            hot_pr = HotPrs(kw=x['kw'], rpm=x['rpm'], qty=x['qty'])
            results.append(hot_pr)

        return results

    def resolve_daily_kw(self, info):
        daily_kw = ReqSpec.objects.exclude(type__title='تعمیرات').filter(is_active=True).values(
            'req_id__date_fa').annotate(
            request_sum=models.Sum(models.F('kw') * models.F('qty'), output_field=models.FloatField())).order_by(
            'req_id__date_fa').reverse()

        result = []

        for x in daily_kw:
            daily = DailyKw(date=x['req_id__date_fa'], kw=x['request_sum'])
            result.append(daily)

        return result

    def resolve_daily_proforma(self, info):

        daily_prof = PrefSpec.objects.filter(is_active=True).values('xpref_id__date_fa').annotate(
            count=models.Count(
                Xpref.objects.values('date_fa').count()
            ),
            sum=models.Sum(1.09 * models.F('qty') * models.F('price'),
                           output_field=models.IntegerField()),
        ).order_by('xpref_id__date_fa').reverse()

        result = []

        for x in daily_prof:
            daily = DailyProforma(date=x['xpref_id__date_fa'], count=x['count'], sum=x['sum'])
            result.append(daily)

        return result

    def resolve_daily_payment(self, info):
        daily_payments = Payment.objects.filter(is_active=True).values('date_fa').annotate(
            amount=models.Sum(models.F('amount'))
        ).order_by('date_fa').reverse()

        result = []

        for x in daily_payments:
            daily = DailyPayment(date=x['date_fa'], sum=x['amount'])
            result.append(daily)

        return result

    def resolve_orders_count(self, info):
        # orders_count = Requests.objects.filter(is_active=True).aggregate(count=models.Count('id'))
        # return orders_count['count']
        count = Requests.objects.filter(is_active=True).count()
        return count


class RequestAppMutations(graphene.ObjectType):
    create_request = RequestMutation.Field()
    create_spec = SpecMutation.Field()
    create_Proforma = ProformaMutation.Field()
    set_proforma_price = ProformaPriceMutation.Field()
    create_payment = PaymentMutation.Field()


def find_count(project_type):
    count = Requests.objects.distinct().filter(reqspec__type__title=project_type, is_active=True).count()
    return count


def find_qty(project_type):
    qty = ReqSpec.objects.filter(type__title=project_type, req_id__is_active=True).aggregate(sum_qty=models.Sum('qty'))
    return qty['sum_qty']


def find_kw(project_type):
    routine = ReqSpec.objects.filter(req_id__is_active=True, type__title=project_type).aggregate(
        kw=models.Sum(models.F('kw') * models.F('qty'), output_field=models.FloatField())
    )
    return routine['kw']


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


schema = graphene.Schema(query=Query, mutation=RequestAppMutations)
# schema = graphene.Schema(query=Query)
