from django.contrib.auth.models import User
from .models import Product,Cart
from .serializers import ProductSerializer,CartSerializer,TokenSerializer,RegisterSerializer
from rest_framework import viewsets,generics,filters
from rest_framework.permissions import AllowAny,IsAuthenticated
from .filter import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("name")
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_class = ProductFilter
    search_fields = ['price','brand','rating','category','name','quantity','created_at']
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('-added')
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    def delete_all(self):
        return Cart.objects.all().delete()
