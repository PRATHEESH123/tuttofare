"""loun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# 3rd party
from rest_framework.routers import DefaultRouter

# djoser
from djoser.urls.base import router as djoser_router

# app
from products.views import (
    CategoryViewSet,
    ProductViewSet,
    ProductReviewViewSet,
    CollectionViewSet,
    WishlistProductsViewSet,
    BrandViewSet,
    TagViewSet,
)

from banners.views import BannerViewSet
from orders.views import CartViewSet, OrderViewSet, AddressViewSet

# TODO check why only the viewset added is showing in the router
router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('review', ProductReviewViewSet)
router.register('tags', TagViewSet)
router.register('collections', CollectionViewSet)
router.register('brands', BrandViewSet)
router.register('wishlist', WishlistProductsViewSet, basename='wishlist')
router.register('cart', CartViewSet, basename='cart')
router.register('banners', BannerViewSet)
router.register('orders', OrderViewSet, basename='orders')
router.register('addresses', AddressViewSet, basename='addresses')

router.registry.extend(djoser_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls.authtoken')),
    path('api/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
