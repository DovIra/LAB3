import cx_Oracle
import csv

con = cx_Oracle.connect('test/passtest@//localhost:1521/xe')
cursor = con.cursor()

tables = ["LOCATIONS", "WIND_DIRECTION", "WEATHER_DAILY", "WEATHER_HOURLY"]

for table in tables:
    with open(f'{table}.csv', 'w', newline='') as file:
        query = f'SELECT * FROM {table}'
        writing = csv.writer(file, delimiter=',')
        cursor.execute(query)
        row = cursor.fetchone()
        while row:
            writing.writerow(row)
            row = cursor.fetchone()
cursor.close()
con.close()
