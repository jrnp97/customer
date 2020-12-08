from rest_framework.routers import SimpleRouter

from customer.api_v1.viewsets import CustomerViewSet

router = SimpleRouter()
router.register(prefix='customers', viewset=CustomerViewSet)

app_name = 'api_v1'
urlpatterns = router.urls
