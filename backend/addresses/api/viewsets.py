from addresses.models import Address
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
