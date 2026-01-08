import React from 'react';
import WebcamMonitor from './components/WebcamMonitor.jsx';

export default function App() {
  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: 16 }}>
      <h1>AI Exam Proctoring (Prototype)</h1>
      <p>Webcam and browser state monitoring demo.</p>
      <WebcamMonitor wsUrl="ws://localhost:8000/ws/proctor" />
    </div>
  );
}
