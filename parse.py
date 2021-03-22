import os
import pandas as pd
import plotly as py
import plotly.graph_objs as go

# cols = ['Elapsed (s)', 'PLA (%)', 'Altitude (m)', 'Delta ISA',
#         'Airspeed (Mn)', 'Power (kW)', 'Thrust (daN)', 'NH (rpm)', 'NH (%)',
#         'NH Setpoint (rpm)', 'NL (rpm)', 'NL (%)', 'NL Setpoint (rpm)',
#         'EGT (K)', 'Fuel flow (kg/h)', 'Fuel pump rating (rpm)',
#         'Fuel pressure (bars)', 'Oil pump rating (rpm)', 'Oil pressure (bars)',
#         'Glowplug', 'Main electrovalve', 'Start electrovalve',
#         'Engine sensor P2 (kPa)', 'Engine sensor P3 (kPa)', 'P2 (kPa)',
#         'T2 (K)', 'W2 (kg/s)', 'V2 (m/s)', 'P3 (kPa)', 'T3 (K)', 'W3 (kg/s)',
#         'V3 (m/s)', 'P4 (kPa)', 'T4 (K)', 'W4 (kg/s)', 'V4 (m/s)', 'P5 (kPa)',
#         'T5 (K)', 'W5 (kg/s)', 'V5 (m/s)', 'P8 (kPa)', 'T8 (K)', 'W8 (kg/s)',
#         'V8 (m/s)', 'P18 (kPa)', 'T18 (K)', 'W18 (kg/s)', 'V18 (m/s)',
#         'P21 (kPa)', 'T21 (K)', 'W21 (kg/s)', 'V21 (m/s)', 'P25 (kPa)',
#         'T25 (K)', 'W25 (kg/s)', 'V25 (m/s)', 'P41 (kPa)', 'T41 (K)',
#         'W41 (kg/s)', 'V41 (m/s)', 'P44 (kPa)', 'T44 (K)', 'W44 (kg/s)',
#         'V44 (m/s)', 'P45 (kPa)', 'T45 (K)', 'W45 (kg/s)', 'V45 (m/s)',
#         'Va4 (m/s)', 'Va41 (m/s)', 'Vu41 (m/s)', 'Wu41 (m/s)', 'Va44 (m/s)',
#         'Vu44 (m/s)', 'Wu44 (m/s)', 'Va45 (m/s)', 'Vu45 (m/s)', 'Wu45 (m/s)',
#         'Va5 (m/s)', 'Vu5 (m/s)', 'Wu5 (m/s)', 'Va25 (m/s)', 'Vu25 (m/s)',
#         'Wu25 (m/s)', 'Va27 (m/s)', 'Vu27 (m/s)', 'Wu27 (m/s)', 'Va3 (m/s)']  # 需要在图里显示哪些数据 就将其填在下面的列表里

cols = ['Elapsed (s)', 'PLA (%)', 'Altitude (m)', 'Delta ISA', 'Airspeed (Mn)', 'Power (kW)', 'Thrust (daN)', 'NH (rpm)',
        'NH (%)', 'NH Setpoint (rpm)', 'NL (rpm)', 'NL (%)', 'NL Setpoint (rpm)', 'EGT (K)', 'Fuel flow (kg/h)',
        'Fuel pump rating (rpm)', 'Fuel pressure (bars)', 'Oil pump rating (rpm)', 'Oil pressure (bars)']

# file_path = r'2021-03-12T16;39;33_Trace.xlsx'
file_path = input('请输入文件名：')
name = os.path.splitext(os.path.split(file_path)[1])[0]
xl = pd.read_excel(file_path)

res = []
for col in cols:
    res.append(go.Scatter(x=xl['Time'], y=xl[col].values.tolist(), name=col))

layout = go.Layout(barmode='group')

fig = go.Figure(data=res, layout=layout)

py.offline.plot(fig, filename=f"{name}.html")
