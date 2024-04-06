from configparser import ConfigParser
from datetime import datetime
from datetime import timedelta
from td.client import TDClient

# Grab configuration values.
config = ConfigParser()
config.read('config/config.ini')

APP_KEY = config.get('main', 'APP_KEY')
APP_SECRET = config.get('main', 'APP_SECRET')
REDIRECT_URI = config.get('main', 'REDIRECT_URI')
CREDENTIALS_PATH = config.get('main', 'JSON_PATH')
ACCOUNT_NUMBER = config.get('main', 'ACCOUNT_NUMBER')

# Create a new session
TDSession = TDClient(
    app_key=APP_KEY,
    app_secret=APP_SECRET,
    redirect_uri=REDIRECT_URI,
    credentials_path=CREDENTIALS_PATH,
    auth_flow='flask'
)

# Login to the session
TDSession.login()
