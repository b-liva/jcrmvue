import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from accounts.models import User
from customer.models import Customer
from customer.schema import CustomerNode
from request.forms.forms import RequestFrom, SpecForm, RequestFormGraphql, SpecFormGraphql
from request.forms.payment_forms import PaymentFrom
from request.forms.proforma_forms import ProformaForm, ProformaPriceForm
from request.models import Requests, ReqSpec, Xpref, PrefSpec, Payment
from graphql_relay.node.node import from_global_id


class RequestMutation(DjangoModelFormMutation):

    class Meta:
        form_class = RequestFormGraphql

    def mutate_and_get_payload(cls, root, **input):
        print(root.context.user)
        owner = User.objects.get(pk=root.context.user.pk)
        customerId = from_global_id(input['customer'])
        customerObj = Customer.objects.get(pk=customerId[1])
        input['customer'] = customerObj.pk
        if "date_fa" in input:
            input['date_fa'] = input['date_fa'].replace('/', '-')
        if "id" in input:
            req_id = input['id']
            req = Requests.objects.get(pk=req_id)
            form = RequestFormGraphql(input or None, instance=req)
            form.save()
            output = Requests.objects.get(pk=req_id)

        else:
            form = RequestFormGraphql(input or None)
            if form.is_valid():
                req_item = form.save(commit=False)
                req_item.owner = owner
                req_item.customer = customerObj
                req_item.save()
                form.save_m2m()
                output = Requests.objects.get(pk=req_item.pk)
            else:
                print(form.errors)
                form = RequestFormGraphql
                output = form

        return RequestMutation(output)


class SpecMutation(DjangoModelFormMutation):
    class Meta:
        form_class = SpecFormGraphql

    def mutate_and_get_payload(cls, root, **input):
        owner = User.objects.get(pk=root.context.user.pk)
        reqId = from_global_id(input['req_id'])
        req = Requests.objects.filter(is_active=True).get(pk=reqId[1])
        input['req_id'] = reqId[1]
        if "id" in input:
            spec_id = input['id']
            spec = ReqSpec.objects.get(pk=spec_id)
            form = SpecFormGraphql(input or None, instance=spec)
            form.save()
            # output = Requests.objects.get(pk=spec_id)
            output = spec
        else:
            form = SpecFormGraphql(input or None)
            if form.is_valid():
                spec = form.save(commit=False)
                spec.req_id = req
                spec.owner = owner
                spec.save()
                output = ReqSpec.objects.get(pk=spec.pk)
            else:
                print(form.errors)
                output = False

        return SpecMutation(output)


class ProformaMutation(DjangoModelFormMutation):

    class Meta:
        form_class = ProformaForm

    def mutate_and_get_payload(cls, root, **input):
        owner = User.objects.get(pk=1)
        req_pk = input['req_id']
        req = Requests.objects.filter(is_active=True).get(pk=req_pk)
        print(input)
        form = ProformaForm(input)
        if form.is_valid():
            proforma_item = form.save(commit=False)
            proforma_item.req_id = req
            proforma_item.owner = owner
            proforma_item.save()
        else:
            print(form.errors)
        return SpecMutation(form)


class ProformaPriceMutation(DjangoModelFormMutation):

    class Meta:
        form_class = ProformaPriceForm


class PaymentMutation(DjangoModelFormMutation):

    class Meta:
        form_class = PaymentFrom

    def mutate_and_get_payload(cls, root, **input):
        print(input)
        form = PaymentFrom(input)
        owner = User.objects.get(pk=1)
        proforma = Xpref.objects.get(pk=input['xpref_id'])
        if form.is_valid():
            payment_item = form.save(commit=False)
            print(payment_item)
            payment_item.owner = owner
            payment_item.customer = proforma.req_id.customer
            payment_item.save()
        else:
            print(form.errors)
        return PaymentMutation(form)
