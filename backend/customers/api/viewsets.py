from customers.models import Customer
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from .serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
