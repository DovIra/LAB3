DECLARE
    v_wind_dir VARCHAR(3);
    v_location varchar(50);
    v_date date;
BEGIN

    v_location := 'Kiyv';
    v_wind_dir := DBMS_RANDOM.string('x',3);
    insert into LOCATIONS(LOCATION_NAME) values ( v_location );
    insert into WIND_DIRECTION( WIND_DIRECTION ) values ( v_wind_dir );


    FOR i IN 1 .. 5
    LOOP

        v_date := TO_DATE(TO_CHAR(SYSDATE-i, 'YYYY-mm-dd'), 'YYYY-mm-dd');
        insert into WEATHER_DAILY(weather_date, location_code, RAINFALL, EVAPORATION, SUNSHINE, WIND_GUST_DIR, WIND_GUST_SPEED, RAINFALL_TOMORROW)
        values (
                v_date,
                v_location,
                round(dbms_random.value(0, 20)*10,2),
                round(dbms_random.value(0, 20)*10,2),
                round(dbms_random.value(0, 20)*10,2),
                v_wind_dir,
                round(dbms_random.value(0, 20)),
                 round(dbms_random.value(0, 20)*10,2)
                );

        insert into WEATHER_HOURLY(WEATHER_DATE, LOCATION_CODE, TIME, WIND_DIR, WIND_SPEED, HUMIDITY,
                                   PRESSURE, CLOUD, TEMPERATURE)
        values(
            v_date,
               v_location, 9, v_wind_dir,
           round(dbms_random.value(0, 20)),
           round(dbms_random.value(0, 100)),
           round(dbms_random.value(900, 1050), 1),
            round(dbms_random.value(0, 9)),
               round(dbms_random.value(10, 15), 2)
          );
        insert into WEATHER_HOURLY(WEATHER_DATE, LOCATION_CODE, TIME, WIND_DIR, WIND_SPEED, HUMIDITY,
                                   PRESSURE, CLOUD, TEMPERATURE)
        values(
            v_date,
               v_location, 15, v_wind_dir,
           round(dbms_random.value(0, 20)),
           round(dbms_random.value(0, 100)),
           round(dbms_random.value(900, 1050), 1),
            round(dbms_random.value(0, 9)),
               round(dbms_random.value(15, 21), 2)
          );

    END LOOP;
    commit;

END;

