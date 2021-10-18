from rest_framework.routers import DefaultRouter
from .views import ClientsViewSet

router = DefaultRouter()

router.register(r'clients',ClientsViewSet,basename = 'clients')

urlpatterns = router.urls