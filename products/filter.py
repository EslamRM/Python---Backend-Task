from django_filters import FilterSet,RangeFilter,NumberFilter
from .models import Product


# class ProductFilter(FilterSet):
#     # filter by min_price and max_price
#     price = RangeFilter()
#     # filter by min_quantity and max_quantity
#     quantity = RangeFilter()

#     class Meta:
#         model = Product
#         fields = ['price','brand','rating','category','name','quantity','created_at']

class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_quantity = NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = NumberFilter(field_name="quantity", lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['category','name','min_price','max_price','min_quantity','max_quantity','brand','rating','created_at']
        