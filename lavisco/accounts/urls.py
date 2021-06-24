from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('shipping', views.ShippingViewSet, basename='shipping')
router.register('sellers', views.SellerViewSet, basename='sellers')
router.register('customers', views.CustomerViewSet, basename='customers')
router.register('content', views.StaticContentViewSet, basename='content')
router.register('', views.UserViewSet, basename='user')

urlpatterns = router.urls
