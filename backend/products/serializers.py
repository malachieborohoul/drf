from rest_framework import serializers

from .models import Product
# P
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields =[
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self,obj):
        print(obj)
        return obj.get_discount()