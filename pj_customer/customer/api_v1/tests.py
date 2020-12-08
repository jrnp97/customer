import json

from django.test import TestCase

from rest_framework import status

from customer.models import Customer


class CustomerAPITest(TestCase):
    API_ENDPOINT = '/customer/api/v1/'
    CUSTOMER_LIST_URI = 'customers/'
    CUSTOMER_DETAIL_URI = 'customers/{id}/'

    def setUp(self) -> None:
        self.data = [
            {
                'id': 1,
                'first_name': 'Laura',
                'last_name': 'Richards',
                'email': 'lrichards0@reverbnation.com',
                'gender': 'Female',
                'company': 'Meezzy',
                'city': 'Warner, NH',
                'title': 'Biostatistician III',
            },
            {
                'id': 2,
                'first_name': 'Margaret',
                'last_name': 'Mendoza',
                'email': 'mmendoza1@sina.com.cn',
                'gender': 'Female',
                'company': 'Skipfire',
                'city': 'East Natchitoches, PA',
                'title': 'VP Marketing',
            }
        ]
        for instance_data in self.data:
            Customer.objects.create(**instance_data)

    def tearDown(self) -> None:
        Customer.objects.all().delete()

    def test_list_endpoint(self):
        endpoint = f'{self.API_ENDPOINT}{self.CUSTOMER_LIST_URI}'
        response = self.client.get(
            path=endpoint,
        )
        response_body = json.dumps(self.data)
        self.assertContains(
            response=response,
            text=response_body,
            status_code=status.HTTP_200_OK,
        )

    def test_detail_endpoint(self):
        endpoint = f'{self.API_ENDPOINT}{self.CUSTOMER_DETAIL_URI}'
        response = self.client.get(
            path=endpoint.format(id=1),
        )
        response_body = json.dumps(self.data[0])
        self.assertContains(
            response=response,
            text=response_body,
            status_code=status.HTTP_200_OK,
        )
