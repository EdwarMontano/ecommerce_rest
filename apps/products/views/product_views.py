from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListAPIView):
    """List all Product"""

    serializer_class = ProductSerializer