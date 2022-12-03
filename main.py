import pandas as pd
import numpy as np
import pydeck as pdk
import streamlit as st
# streamlit run C:/Users/James/Desktop/HKD/main.py

header = st.container()
dataset = st.container()


with header:
    st.header("DataNI")

with dataset:
    st.header("Cost of living")

    st.subheader("Number of Business opened/closed")
    df = pd.DataFrame({

      'date': ['2016', '2017', '2018', '2019', '2020'],
      'Closed-Down': [4080, 4470, 4380, 5385, 4900],
      'Opened': [5935, 6850, 5900, 6625, 6375]
    })

    st.line_chart(df.rename(columns={'date': 'index'}).set_index('index'))

    st.subheader("Total business' per sector")

    data3 = pd.DataFrame({

      'date': ['2016', '2017', '2018', '2019', '2020', '2021'],
      'Food Sector': [3715, 3865, 4000, 4145, 4225, 4270],
      'Agricultural Sector': [17685, 17845, 18285, 18520, 18330, 18215],
      'Entertainment Sector': [4400, 4400, 4505, 4640, 4730, 4715],
      'Business Sector': [2400, 2465, 2645, 2745, 2930, 3135]
    })
    st.area_chart(data3.rename(columns={'date': 'index'}).set_index('index'))

    st.subheader("Spending increase in households during christmas period")

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [54.60, -5.92],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=54.60,
        longitude=-5.92,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=1000,
        ),
    ],
))

st.header("GDP and Productivity")
st.subheader("GDP nominal (overall) & Smoothed Nominal £'s")

data4 = pd.DataFrame({

  'date': ['2016', '2017', '2018', '2019', '2020'],
  "GDP (000,000's)": [45151, 46793, 48264, 50279, 48478],
  "Smoothed Nominal £s": [47223, 48511, 49522, 50149, 50396]
})
st.bar_chart(data4.rename(columns={'date': 'index'}).set_index('index'))


