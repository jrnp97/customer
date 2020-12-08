from django.urls import path
from django.urls import include

from customer.views import index

app_name = 'customer'
urlpatterns = [
    path('', index, name='index'),
    path('api/v1/', include('customer.api_v1.urls', namespace='api_v1')),
]
