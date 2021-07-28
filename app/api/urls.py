from django.urls import path

from .views import (
	ProductCreateAPIView,
	ProductListAPIView,
	ProductRetrieveAPIView,
	ProductDestroyAPIView,
	ProductUpdateAPIView,
)


urlpatterns = [
	path('product-create/', ProductCreateAPIView.as_view()),
	path('product-list/', ProductListAPIView.as_view()),
	path('product-detail/<int:pk>',  ProductRetrieveAPIView.as_view()),
	path('product-delete/<int:pk>', ProductDestroyAPIView.as_view()),
	path('product-update/<int:pk>', ProductUpdateAPIView.as_view())
]