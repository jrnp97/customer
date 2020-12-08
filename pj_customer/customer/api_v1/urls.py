
from django.urls import path

from rest_framework import permissions

from rest_framework.routers import SimpleRouter


from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from customer.api_v1.viewsets import CustomerViewSet

router = SimpleRouter()
router.register(prefix='customers', viewset=CustomerViewSet)

app_name = 'api_v1'
urlpatterns = router.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns.extend(
    [
        path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='doc'),
    ]
)
