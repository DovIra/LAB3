DECLARE
    TYPE t_wind_dir IS VARRAY(5) OF VARCHAR(3);
    v_location varchar(50);
    v_date date;
    v_wind_dir t_wind_dir;
BEGIN
    v_location := 'Kiyv';
    v_wind_dir := v_wind_dir('ESE','NE','SSW','SE','WNW');

    insert into LOCATIONS(LOCATION_NAME) values ( v_location );

    FOR i IN 1 .. v_wind_dir.count
    LOOP
        v_date := TO_DATE(TO_CHAR(SYSDATE-i, 'YYYY-mm-dd'), 'YYYY-mm-dd');
        insert into WEATHER_DAILY(weather_date, location_code, RAINFALL, EVAPORATION, SUNSHINE)
        values (
                v_date,
                v_location,
                round(dbms_random.value(0, 20)*10,2),
                round(dbms_random.value(0, 20)*10,2),
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

