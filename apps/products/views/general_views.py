from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import (
    CategoryProductSerializer,
    IndicatorSerializer,
    MeasureUnitSerializer,
)


class MeasureUnitListAPIView(GeneralListAPIView):
    """List all MeasureUnit"""

    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListAPIView):
    """List all Indicator"""

    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GeneralListAPIView):
    """List all CategoryProduct"""

    serializer_class = CategoryProductSerializer
