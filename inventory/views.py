from django.shortcuts import render,get_object_or_404,get_list_or_404
from rest_framework import viewsets, serializers, permissions
# for search functionality
from rest_framework.filters import SearchFilter
# for filtering functionality
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from .filters import ItemFilter

from .models import Item
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

# search functionality
    # filter_backends = [SearchFilter]
    # search_fields = ['name',"category"]

# filtering functionality
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter
    # filterset_fields = ['name','category','price','quantity']


    # this is to associate item with the user who registered it
    def perform_create(self, serializer):
        # validation
        if serializer.validated_data['quantity'] < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        if serializer.validated_data['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative")
        if serializer.validated_data['name'] == "":
            raise serializers.ValidationError("Name cannot be empty")
        
        serializer.save(registered_by=self.request.user)
        print(serializer.validated_data)
        return super().perform_create(serializer)
    
    @action(detail=True,methods=['get'])
    def quantity(self,request,pk=None):
        item = get_object_or_404(Item, pk=pk)
        return Response({"quantity": item.quantity})

