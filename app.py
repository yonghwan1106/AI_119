import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title('지역별 119 신고 밀집도 히트맵')

# 가상의 데이터 생성 (실제로는 데이터베이스나 API에서 가져와야 함)
def generate_data():
    center_lat, center_lng = 37.5665, 126.9780  # 서울 중심 좌표
    num_points = 1000
    
    data = pd.DataFrame({
        'lat': np.random.normal(center_lat, 0.05, num_points),
        'lon': np.random.normal(center_lng, 0.05, num_points),
        'intensity': np.random.random(num_points)
    })
    
    return data

# 시간 범위 선택
time_range = st.selectbox('시간 범위 선택', ['최근 24시간', '최근 7일', '최근 30일'])

# 데이터 생성
data = generate_data()

# 히트맵 생성
layer = pdk.Layer(
    "HeatmapLayer",
    data,
    opacity=0.9,
    get_position=["lon", "lat"],
    get_weight="intensity",
)

view_state = pdk.ViewState(
    latitude=37.5665,
    longitude=126.9780,
    zoom=10,
    pitch=0,
)

# 지도 렌더링
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/light-v9",
))

st.write(f"선택된 시간 범위: {time_range}")
