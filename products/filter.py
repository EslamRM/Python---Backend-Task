from django_filters import FilterSet,RangeFilter,NumberFilter
from .models import Product


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_quantity = NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = NumberFilter(field_name="quantity", lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['category','name','min_price','max_price','min_quantity','max_quantity','brand','rating','created_at']
        