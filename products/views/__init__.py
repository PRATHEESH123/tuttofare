from .categories import CategoryViewSet
from .collections import CollectionViewSet
from .products import ProductViewSet
from .reviews import ProductReviewViewSet
from .wishlist import WishlistProductsViewSet

__all__ = (
    CategoryViewSet,
    CollectionViewSet,
    ProductViewSet,
    ProductReviewViewSet,
    WishlistProductsViewSet,
)