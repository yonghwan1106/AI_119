import streamlit as st

import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Map, HeatmapLayer } from 'react-leaflet-heatmap-layer';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// 이 부분은 실제 환경에서 leaflet의 기본 마커 아이콘 문제를 해결하기 위한 코드입니다.
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-shadow.png',
});

const EmergencyCallHeatmap = () => {
  const [heatmapData, setHeatmapData] = useState([]);
  const [timeRange, setTimeRange] = useState('24h'); // '24h', '7d', '30d'

  useEffect(() => {
    // 실제 구현에서는 API를 통해 데이터를 가져옵니다.
    const fetchHeatmapData = () => {
      // 서울시 중심 좌표 주변으로 랜덤한 위치에 포인트 생성
      const centerLat = 37.5665;
      const centerLng = 126.9780;
      const points = Array.from({ length: 1000 }, () => [
        centerLat + (Math.random() - 0.5) * 0.2,
        centerLng + (Math.random() - 0.5) * 0.2,
        Math.random() // 강도 (0-1 사이의 값)
      ]);
      setHeatmapData(points);
    };

    fetchHeatmapData();
  }, [timeRange]);

  return (
    <Card className="w-full h-[600px]">
      <CardHeader>
        <CardTitle className="flex items-center justify-between">
          <span>지역별 119 신고 밀집도 히트맵</span>
          <div>
            <select 
              value={timeRange} 
              onChange={(e) => setTimeRange(e.target.value)}
              className="p-2 border rounded"
            >
              <option value="24h">최근 24시간</option>
              <option value="7d">최근 7일</option>
              <option value="30d">최근 30일</option>
            </select>
          </div>
        </CardTitle>
      </CardHeader>
      <CardContent className="p-0 h-[calc(100%-4rem)]">
        <MapContainer center={[37.5665, 126.9780]} zoom={11} style={{ height: '100%', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          <HeatmapLayer
            points={heatmapData}
            longitudeExtractor={m => m[1]}
            latitudeExtractor={m => m[0]}
            intensityExtractor={m => m[2]}
            radius={20}
            max={1.0}
            minOpacity={0.1}
          />
        </MapContainer>
      </CardContent>
    </Card>
  );
};

export default EmergencyCallHeatmap;
