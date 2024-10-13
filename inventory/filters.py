import django_filters
from .models import Item

# this is to filter the items based on the price, quantity and category
class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'price': ['lt', 'gt'],
            'quantity':['lt','gt'],
            'category':['icontains'],
            
        }
