from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    ListAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from product.models import (
    Product,
    ProductImage
)

from product.serializers import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductReadOnlySerializer,  
    ProductImageCreateSerializer,
    ProductImageReadSerializer
)


class ProductCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductReadOnlySerializer


class ProductUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer



class ProductImageCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer

class ProductImageDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer
    def perform_destroy(self, instance): 
        if instance.product.owner != self.request.user:
            return Response({"message": "You are not owner"},status=403)
        else:
            instance.delete()
            return Response(status=204)

class ProductSearchByTagView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        serializer = ProductReadOnlySerializer(Product.objects.filter(tags__icontains=request.query_params.get('tag', "")), many=True)
        return Response(serializer.data)