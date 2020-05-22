import cx_Oracle
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard

chart_studio.tools.set_credentials_file(username='DovIra', api_key='AIcPohsRGYxxuwUHTxlN')
con = cx_Oracle.connect('test/passtest@//localhost:1521/xe')
cursor = con.cursor()

# ----query1------
query_1 = """select uu.LOCATION_NAME, uu.sum_rainfall
from(
    select
    LOCATIONS.LOCATION_NAME, sum(RAINFALL) as sum_rainfall
  from WEATHER_DAILY
  join LOCATIONS on LOCATIONS.LOCATION_NAME = WEATHER_DAILY.location_code
  group by LOCATION_CODE
  order by sum(RAINFALL) desc
) uu
where rownum <= 5"""

cursor.execute(query_1)
val_query1 = list()
lab_query1 = list()

for location_name, sum_rainfall in cursor:
    val_query1.append(sum_rainfall)
    lab_query1.append(location_name)

# ----end query1-----

# ----query2------
query_2 = """select LOCATIONS.LOCATION_NAME, sum(RAINFALL) as sum_rainfall
from WEATHER_DAILY
join LOCATIONS on LOCATIONS.LOCATION_NAME = WEATHER_DAILY.location_code
group by LOCATION_CODE
order by 2 desc
FETCH FIRST 20 ROWS ONLY
"""

cursor.execute(query_2)

val_query2 = list()
lab_query2 = list()

for location_name, sum_rainfall in cursor:
    val_query2.append(sum_rainfall)
    lab_query2.append(location_name)

# ----end query2-----

# ----query3------

query_3 = """select
       to_char(WEATHERDATE,'Month'),
       extract(month from WEATHERDATE),
       ROUND(avg((MINTEMP+MAXTEMP)/2),2) as avg_temperature
from WEATHER_DETAILS
where extract(year from WEATHERDATE) = 2017
group by to_char(WEATHERDATE,'Month'), extract(month from WEATHERDATE)
order by extract(month from WEATHERDATE)
"""

cursor.execute(query_3)

val_query3 = list()
lab_query3 = list()

for month_name, month_number, avg_temperature in cursor:
    val_query3.append(avg_temperature)
    lab_query3.append(month_name)

# ----end query3-----

bar = go.Bar(
    x=lab_query1,
    y=val_query1
)
graph_query1 = py.plot([bar], auto_open=False, filename='task 1')

pie = go.Pie(
    labels=lab_query2,
    values=val_query2
)
graph_query2 = py.plot([pie], auto_open=False, filename='task 2')

scatter = go.Scatter(
    x=lab_query3,
    y=val_query3
)
graph_query3 = py.plot([scatter], auto_open=False, filename='task 3')

cursor.close()
con.close()

# dashboard creation ---------------------------------------------------

D_board = dashboard.Dashboard()
first = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'DovIra:' + graph_query1.split('/')[4],
    'title': '1 запит-перші 5 локацій з мах числом опадів'
}
second = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'DovIra:' + graph_query2.split('/')[4],
    'title': '2 запит-перші 20 міст з найбільшою кількістю опадів у %, по Австралії',

}
thirth = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'DovIra:' + graph_query3.split('/')[4],
    'title': '3 запит-динаміка середньої температури у 2017 році по місяцям'
}

D_board.insert(first)
D_board.insert(second, 'below', 1)
D_board.insert(thirth, 'right', 2)

py.dashboard_ops.upload(D_board, 'lab_3_Ira_Dovgal')
