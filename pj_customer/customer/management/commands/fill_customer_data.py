""" Module to define customer data importer csv command """
import os

from django.db import connection, IntegrityError

from django.db.models.aggregates import Count

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from customer.models import Customer

from customer.utils import get_address_info
from customer.utils import get_coordinates_from_address_info


class Command(BaseCommand):
    """ Class to define command """
    help = 'Command to import customer.csv file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument(
            '--not-coordinates',
            action='store_true',
            help='Upload customer data without fill lat and lng information',
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        if not os.path.exists(csv_file):
            raise CommandError(f'CSV file: {csv_file} not found.')
        with connection.cursor() as cursor:
            sql = f'TRUNCATE TABLE {Customer._meta.db_table}'
            cursor.execute(sql)
        insert_count = Customer.objects.from_csv(
            csv_file,
            ignore_conflicts=True,
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {insert_count} customers, lets fill coordinates.'))
        self.stdout.write(self.style.SUCCESS('Searching coordinates information'))
        if options['not_coordinates']:
            return
        customer = Customer.objects.values('city').annotate(count_=Count('id'))
        for city in customer:
            address = city['city']
            result = get_coordinates_from_address_info(
                address_info=get_address_info(
                    address=address,
                    silent=True,
                ),
                silent=True,
            )
            if not result:
                self.stdout.write(self.style.WARNING(f'Unable to get coordinates info for address {address}'))
                continue
            try:
                Customer.objects.filter(city__exact=address).update(
                    latitude=result['lat'],
                    longitude=result['lng'],
                )
            except (IntegrityError, KeyError):
                self.stdout.write(
                    self.style.WARNING(f'Unable to update coordinates info for address {address}, coordinate: {result}')
                )
                continue



