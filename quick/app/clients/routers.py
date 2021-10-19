from rest_framework.routers import DefaultRouter
from .views import ClientsViewSet, UserViewSet

router = DefaultRouter()

router.register(r'clients',ClientsViewSet,basename = 'clients')
router.register(r'user',UserViewSet,basename = 'user')

urlpatterns = router.urls