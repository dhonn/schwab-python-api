import pprint
from td.client import TDClient
from configparser import ConfigParser

# Grab configuration values.
config = ConfigParser()
config.read('config/config.ini')

APP_KEY = config.get('main', 'APP_KEY')
APP_SECRET = config.get('main', 'APP_SECRET')
REDIRECT_URI = config.get('main', 'REDIRECT_URI')
JSON_PATH = config.get('main', 'JSON_PATH')
ACCOUNT_NUMBER = config.get('main', 'ACCOUNT_NUMBER')

# Create a new session
td_session = TDClient(
    app_key=APP_KEY,
    app_secret=APP_SECRET,
    redirect_uri=REDIRECT_URI,
    credentials_path=JSON_PATH,
    account_number=ACCOUNT_NUMBER
)

# Login to the session
td_session.login()

# Define the Order.
order_template = buy_limit_enter = {
    "orderType": "LIMIT",
    "session": "NORMAL",
    "duration": "DAY",
    "price": 10.0,
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": "BUY",
            "quantity": 1,
            "instrument": {
                "symbol": "AAL",
                "assetType": "EQUITY"
            }
        }
    ]
}

# Place the Order.
order_response = td_session.place_order(
    account=ACCOUNT_NUMBER,
    order=order_template
)

# Print the Response.
pprint.pprint(order_response)