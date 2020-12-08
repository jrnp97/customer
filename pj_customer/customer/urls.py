from django.urls import path
from django.urls import include

app_name = 'customer'
urlpatterns = [
    path('api/v1/', include('customer.api_v1.urls', namespace='api_v1')),
]
