import sqlite3,config

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

cursor.execute("""
    Drop TABLE stock_price
""")

cursor.execute("""
    Drop TABLE stock
""")

connection.commit()