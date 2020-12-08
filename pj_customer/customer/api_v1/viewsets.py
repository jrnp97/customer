from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin

from rest_framework.viewsets import GenericViewSet

from customer.api_v1.serializers import CustomerSerializer

from customer.models import Customer


class CustomerViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Customer.objects.order_by('id')
    serializer_class = CustomerSerializer
