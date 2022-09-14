from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

# Local to instance settings.
DBHOST=os.environ['LOCAL_HOST']
DBNAME=os.environ['LOCAL_DATABASE']
DBUSER=os.environ['LOCAL_USERNAME']
DBPASS=os.environ['LOCAL_PASSWORD']

# Configure database connection for remote PostgreSQL instance.
if 'USE_REMOTE_POSTGRESQL' in os.environ:
    DBNAME=os.environ['AZURE_POSTGRESQL_DATABASE']
    DBHOST=os.environ['AZURE_POSTGRESQL_HOST']
    DBUSER=os.environ['AZURE_POSTGRESQL_USERNAME']
    DBPASS=os.environ['AZURE_POSTGRESQL_PASSWORD']

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    DBUSER,
    DBPASS,
    DBHOST,
    DBNAME
)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'
