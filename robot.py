from trading_ig import IGService
from trading_ig.config import config

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig_service.create_session()

account_info = ig_service.switch_account(config.acc_number, False) # not necessary
print(account_info)

open_positions = ig_service.fetch_open_positions()
print("open_positions:\n%s" % open_positions)

print("")

epic = 'CS.D.EURUSD.MINI.IP'
resolution = 'D'
num_points = 10
response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, resolution, num_points)
df_ask = response['prices']['ask']
print("ask prices:\n%s" % df_ask)

from datetime import datetime, timedelta
import requests_cache
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=timedelta(hours=1))
# set expire_after=None if you don't want cache expiration
# set expire_after=0 if you don't want to cache queries

