import os
import csv
import tempfile

from django.test import TransactionTestCase

from django.core.management import call_command

from customer.models import Customer


# Create your tests here.


class TestImportCommand(TransactionTestCase):
    # Class to define Test case to test, customer file importer django-command

    def create_csv_file(self, dummy_data=None):
        if not dummy_data:
            dummy_data = self.dummy_data
        with open(self.test_file, 'w') as file_:
            writer = csv.writer(file_)
            writer.writerow(self.file_header)
            for data in dummy_data:
                writer.writerow(data)

    def setUp(self) -> None:
        self.test_file = os.path.join(tempfile.gettempdir(), 'test_file.csv')
        self.file_header = [
            'id',
            'first_name',
            'last_name',
            'email',
            'gender',
            'company',
            'city',
            'title',
        ]
        self.dummy_data = [
            [
                '1',
                'Laura',
                'Richards',
                'lrichards0@reverbnation.com',
                'Female',
                'Meezzy',
                'Warner, NH',
                'Biostatistician III'
            ],
            [
                '2',
                'Margaret',
                'Mendoza',
                'mmendoza1@sina.com.cn',
                'Female',
                'Skipfire',
                'East Natchitoches, PA',
                'VP Marketing'
            ],
        ]

    def tearDown(self) -> None:
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_importation_fill_database(self):
        self.create_csv_file()
        call_command('fill_customer_data', '--not-coordinates', self.test_file)
        self.assertEqual(Customer.objects.count(), 2)

    def test_import_the_same_file_two_times(self):
        self.create_csv_file()
        call_command('fill_customer_data', '--not-coordinates', self.test_file)
        call_command('fill_customer_data', '--not-coordinates', self.test_file)
        self.assertEqual(Customer.objects.count(), 2)

    def test_update_data(self):
        self.create_csv_file()
        call_command('fill_customer_data', '--not-coordinates', self.test_file)
        dummy_data = [
            [

                '1',
                'Maria',
                'Holmes',
                'mmholmes@reverbnation.com',
                'Female',
                'Meezzy',
                'Warner, NH',
                'Biostatistician III'
            ],
            [
                '2',
                'Margaret',
                'Mendoza',
                'mmendoza1@sina.com.cn',
                'Female',
                'Skipfire',
                'East Natchitoches, PA',
                'VP Marketing'
            ],
            [
                '3',
                'Laura',
                'Richards',
                'lrichards0@reverbnation.com',
                'Female',
                'Meezzy',
                'Warner, NH',
                'Biostatistician III'
            ],
        ]
        self.create_csv_file(dummy_data=dummy_data)
        call_command('fill_customer_data', '--not-coordinates', self.test_file)
        self.assertEqual(Customer.objects.count(), 3)
        customer = Customer.objects.get(id=1)
        self.assertEqual(customer.first_name, 'Maria')

    def test_latitude_and_longitude_data_generation(self):
        dummy_data = [
            [

                '1',
                'Maria',
                'Holmes',
                'mmholmes@reverbnation.com',
                'Female',
                'Meezzy',
                'Warner, NH',
                'Biostatistician III'
            ],
        ]
        self.create_csv_file(dummy_data=dummy_data)
        call_command('fill_customer_data', self.test_file)
        expected_latitude = 43.2556568
        expected_longitude = -71.8334145
        customer = Customer.objects.get(id=1)
        self.assertEqual(
            customer.latitude,
            expected_latitude,
        )
        self.assertEqual(
            customer.longitude,
            expected_longitude,
        )
