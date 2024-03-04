import config
import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect(config.DB_FILE)

connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    SELECT id, symbol, name FROM stock         
""")

rows = cursor.fetchall()

symbols = [row['symbol'] for row in rows]
stock_dict = {}
for row in rows:
    symbol = row['symbol']
    symbols.append(symbol)
    stock_dict[symbol] = row['id']
# print(symbols)

# Create an instance of the Alpaca class
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.BASE_URL)

# Define the date range
start_date = "2023-01-01T00:00:00-00:00"
end_date = "2024-03-03T00:00:00-00:00"

chunk_size = 200

for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i + chunk_size]
    
    # Fetch historical data for the current symbol chunk
    barsets = api.get_bars(symbol_chunk, '1D', start_date, end_date)
    
    for symbol in symbol_chunk:
        print(f"Processing symbol {symbol}")

        # Get the stock_id from the stock_dict
        stock_id = stock_dict[symbol]
        
        # Iterate through rows of historical data for the current symbol
        for index, row in barsets[symbol].iterrows():
            timestamp = index
            open_value = row['open']
            high_value = row['high']
            low_value = row['low']
            close_value = row['close']
            volume_value = row['volume']

            # Insert data into the stock_price table
            cursor.execute("""
                INSERT INTO stock_price (stock_id, date, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (stock_id, timestamp, open_value, high_value, low_value, close_value, volume_value))

# Commit changes to the database
connection.commit()


