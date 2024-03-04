import sqlite3, config
import alpaca_trade_api as tradeapi

connection = sqlite3.connect(config.DB_FILE)

connection.row_factory = sqlite3.Row

cursor = connection.cursor()

api = tradeapi.REST(config.API_KEY,config.SECRET_KEY, base_url=config.BASE_URL)
assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, name) VALUES (?,?)" ,(asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print (e)

connection.commit()