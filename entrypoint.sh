#!/usr/bin/env bash

WORK_DIR=/src/

python $WORK_DIR/manage.py test

if [$? -eq -1]; then
	echo 'Tests Failed';
fi

python $WORK_DIR/manage.py migrate --no-input

if [$? -eq -1]; then
	echo 'Error migration';
fi

python $WORK_DIR/manage.py runserver 0.0.0.0:8000
