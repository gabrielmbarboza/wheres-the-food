from addresses.models import Address
from rest_framework.serializers import ModelSerializer


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'neighborhood', 'city',
                  'state', 'fed_unit', 'zipcode', 'lat', 'lon']
