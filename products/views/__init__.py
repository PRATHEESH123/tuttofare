from .categories import CategoryViewSet
from .collections import CollectionViewSet
from .products import ProductViewSet
from .reviews import ProductReviewViewSet
from .wishlist import WishlistProductsViewSet
from .brands import BrandViewSet
from .tags import TagViewSet

__all__ = (
    CategoryViewSet,
    CollectionViewSet,
    ProductViewSet,
    ProductReviewViewSet,
    WishlistProductsViewSet,
    BrandViewSet,
    TagViewSet,
)
