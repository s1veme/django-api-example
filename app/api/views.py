from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	UpdateAPIView
)

from .serializers import ProductSerializer  

from app.models import Product


class ProductCreateAPIView(CreateAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()


class ProductListAPIView(ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()