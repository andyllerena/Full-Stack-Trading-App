
import config
import sqlite3
import alpaca_trade_api as tradeapi

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.BASE_URL)

barsets = api.get_bars('AAPL', '1D').df
print(barsets)

# # Process the data
# for index, row in barsets.iterrows():
#     print(f"Processing timestamp {index}")

#     # Accessing individual values in the row
#     timestamp = index
#     open_value = row['open']
#     high_value = row['high']
#     low_value = row['low']
#     close_value = row['close']
#     volume_value = row['volume']

#     # Now you can use these values as needed in your processing
#     print(timestamp, open_value, high_value, low_value, close_value, volume_value)
