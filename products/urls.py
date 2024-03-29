from django.urls import path,include
from .views import LoginView,RegisterView,ProductViewSet,CartViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
# products api
router.register(r'products',ProductViewSet,basename="products")
# cart api
router.register(r'cart',CartViewSet,basename="cart")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='token_access'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]