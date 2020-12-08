""" Module to define customer data importer csv command """
import os

from django.db import connection
from django.db import transaction

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from customer.models import Customer


class Command(BaseCommand):
    """ Class to define command """
    help = 'Command to import customer.csv file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

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


