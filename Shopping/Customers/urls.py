from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, OrderViewSet, ReviewViewSet

from django.urls import path
from .views import register_user, user_login, user_logout


urlpatterns = [
   path('register/', register_user, name='register'),
   path('login/', user_login, name='login'),
   path('logout/', user_logout, name='logout'),

]

router = DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)

#urlpatterns = router.urls
