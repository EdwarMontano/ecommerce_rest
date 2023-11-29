from apps.products.models import Product
from rest_framework import serializers

from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    # metodo 1 - view data foreign key
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    # metodo 2 - view data foreign key - StringRelatedField
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()
    class Meta:
        model = Product
        exclude = ("state", "created_date", "modified_date", "deleted_date")

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description,
        }
