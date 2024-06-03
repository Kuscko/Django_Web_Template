########################################################################################
# THIS FILE IS A TEMPLATE, DO NOT DIRECTLY MODIFY THIS FILE!!!                         #
# DUPLICATE THIS FILE AND RENAME IT TO 'environment.py' THEN FILL IN THE MISSING INFO! #
########################################################################################

# Generate a secret key
# enter in console:

# .\manage.py shell
# from django.core.management.utils import get_random_secret_key
# print(get_random_secret_key())

# Secret key
SECRET_KEY='r(o59$n)v&%4ut7h6n9odh#uff9gd@=es)9p7+re-h@xaf0z8b'

# Debug mode
DEBUG=True

# Allowed hosts
ALLOWED_HOSTS=['localhost', '127.0.0.1']

# Database settings
DATABASE_NAME='' # Name of your database
DATABASE_USER='' # Username for your database
DATABASE_PASSWORD='' # Password for your database
DATABASE_HOST='' # Name of the service defined in docker-compose.yml
DATABASE_PORT='' # Default port for PostgreSQL

# Other Django settings...

