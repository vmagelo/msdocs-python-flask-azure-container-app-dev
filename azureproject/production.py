import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'flask-insecure-7ppocbnx@w71dcuinn*t^_mzal(t@o01v3fee27g%rg18fc5d@'

DEBUG = False
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

# Configure database connection for Azure PostgreSQL Flexible server instance.
# AZURE_POSTGRESQL_HOST is the full URL.
# AZURE_POSTGRESQL_USERNAME is just name without @server-name.
DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    os.environ['AZURE_POSTGRESQL_USERNAME'],
    os.environ['AZURE_POSTGRESQL_PASSWORD'],
    os.environ['AZURE_POSTGRESQL_HOST'],
    os.environ['AZURE_POSTGRESQL_DATABASE']
)
