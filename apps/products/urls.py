from apps.products.views.general_views import (
    CategoryProductListAPIView,
    IndicatorListAPIView,
    MeasureUnitListAPIView,
)
from django.urls import path
from apps.products.views.product_views import ProductListAPIView

urlpatterns = [
    path("measure_unit/", MeasureUnitListAPIView.as_view(), name="measure_unit-list"),
    path("indicator/", IndicatorListAPIView.as_view(), name="indicator-list"),
    path(
        "category_product/",
        CategoryProductListAPIView.as_view(),
        name="category_product-list",
    ),
    path("product/", ProductListAPIView.as_view(), name="product")
]
