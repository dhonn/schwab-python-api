from datetime import datetime
from datetime import timedelta
from td.client import TDClient

# Create a new session
TDSession = TDClient(
    app_key='<APP_KEY>',
    app_secret='<APP_SECRET>',
    redirect_uri='<REDIRECT_URI>',
    credentials_path='<CREDENTIALS_PATH>',
    auth_flow='flask'
)

# Login to the session
TDSession.login()
