import cx_Oracle
import csv

con = cx_Oracle.connect('test/passtest@//localhost:1521/xe')
cursor = con.cursor()

cursor.execute("delete from WEATHER_HOURLY")
cursor.execute("delete from WEATHER_DAILY")
cursor.execute("delete from LOCATIONS")
cursor.execute("delete from WIND_DIRECTION")

locations = []
wind_dirs = []


reader = csv.DictReader(open('weatherAUS.csv'), delimiter=',')

for row in reader:
    count += 1
   

    date = row['Date']
    location = row['Location']
    rainfall = 0 if row['Rainfall'] == 'NA' else row['Rainfall']
    evaporation = None if row['Evaporation'] == 'NA' else row['Evaporation']
    sunshine = None if row['Sunshine'] == 'NA' else row['Sunshine']
    windGustDir = row['WindGustDir']
    windGustSpeed = None if row['WindGustSpeed'] == 'NA' else row['WindGustSpeed']
    rainfall_tomorrow = row['RISK_MM']



    if location not in locations:
        locations.append(location)
        query = "INSERT INTO LOCATIONS(LOCATION_NAME) VALUES ( :location)"
        cursor.execute(query, location=location)

    if windGustDir not in wind_dirs:
        wind_dirs.append(windGustDir)
        query = "INSERT INTO WIND_DIRECTION(WIND_DIRECTION) VALUES ( :wind_direction)"
        cursor.execute(query, wind_direction=windGustDir)

    query = "insert into WEATHER_DAILY(WEATHER_DATE, LOCATION_CODE, RAINFALL, EVAPORATION, SUNSHINE, WIND_GUST_DIR, WIND_GUST_SPEED, RAINFALL_TOMORROW) values(TO_DATE(:weather_date, 'YYYY-mm-dd'), :location_code, :rainfall, :evaporation, :sunshine, :wind_dir, :wind_speed, :rainfall_tomorrow)"
    cursor.execute(query, weather_date=date, location_code=location, rainfall=rainfall, evaporation=evaporation, sunshine=sunshine, wind_dir=windGustDir, wind_speed=windGustSpeed, rainfall_tomorrow=rainfall_tomorrow)

    
    time = 9
    wind_dir = row['WindDir9am']
    wind_speed = None if row['WindSpeed9am'] == 'NA' else row['WindSpeed9am']
    humidity = None if row['Humidity9am'] == 'NA' else row['Humidity9am']
    pressure = None if row['Pressure9am'] == 'NA' else row['Pressure9am']
    cloud = None if row['Cloud9am'] == 'NA' else row['Cloud9am']
    temperature = None if row['Temp9am'] == 'NA' else row['Temp9am']

    if wind_dir not in wind_dirs:
        wind_dirs.append(wind_dir)
        query = "INSERT INTO WIND_DIRECTION(WIND_DIRECTION) VALUES ( :wind_direction)"
        cursor.execute(query, wind_direction=wind_dir)

    query = "insert into WEATHER_HOURLY(WEATHER_DATE, LOCATION_CODE, TIME, WIND_DIR, WIND_SPEED, HUMIDITY, PRESSURE, CLOUD, TEMPERATURE) values(TO_DATE(:weather_date, 'YYYY-mm-dd'), :location_code, :time, :wind_dir, :wind_speed, :humidity, :pressure, :cloud, :temperature)"
    cursor.execute(query, weather_date=date, location_code=location, time=time, wind_dir=wind_dir, wind_speed=wind_speed, humidity=humidity, pressure=pressure, cloud=cloud, temperature=temperature)

    
    time = 15
    wind_dir = row['WindDir3pm']
    wind_speed = None if row['WindSpeed3pm'] == 'NA' else row['WindSpeed3pm']
    humidity = None if row['Humidity3pm'] == 'NA' else row['Humidity3pm']
    pressure = None if row['Pressure3pm'] == 'NA' else row['Pressure3pm']
    cloud = None if row['Cloud3pm'] == 'NA' else row['Cloud3pm']
    temperature = None if row['Temp3pm'] == 'NA' else row['Temp3pm']

    if wind_dir not in wind_dirs:
        wind_dirs.append(wind_dir)
        query = "INSERT INTO WIND_DIRECTION(WIND_DIRECTION) VALUES ( :wind_direction)"
        cursor.execute(query, wind_direction=wind_dir)

    query = "insert into WEATHER_HOURLY(WEATHER_DATE, LOCATION_CODE, TIME, WIND_DIR, WIND_SPEED, HUMIDITY, PRESSURE, CLOUD, TEMPERATURE) values(TO_DATE(:weather_date, 'YYYY-mm-dd'), :location_code, :time, :wind_dir, :wind_speed, :humidity, :pressure, :cloud, :temperature)"
    cursor.execute(query, weather_date=date, location_code=location, time=time, wind_dir=wind_dir, wind_speed=wind_speed, humidity=humidity, pressure=pressure, cloud=cloud, temperature=temperature)


cursor.close()
con.commit()
con.close()
