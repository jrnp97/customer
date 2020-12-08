#!/usr/bin/env bash

WORK_DIR=/src/

if python $WORK_DIR/manage.py test; then
  echo 'Test Passed!!'
else
	echo 'Tests Failed'
	exit 1
fi

if python $WORK_DIR/manage.py migrate --no-input; then
  echo 'Migrations executed!!'
else
	echo 'Error migration'
	exit 1
fi

echo 'Filling database with customer data....'
if python $WORK_DIR/manage.py fill_customer_data $WORK_DIR/data/customers.csv; then
  echo 'Customer data on database!!'
else
  echo 'Error importing customer data on database :('
  exit 1
fi

python $WORK_DIR/manage.py runserver 0.0.0.0:8000
