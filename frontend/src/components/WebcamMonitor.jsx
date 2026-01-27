import React, { useEffect, useRef, useState } from 'react';

/**
 * Webcam + browser state monitor.
 *
 * - Requests webcam via getUserMedia and shows a muted preview.
 * - Connects to a backend WebSocket to send browser events.
 * - Observes tab visibility changes and fullscreen entry/exit.
 * - Captures frames and sends to backend for face detection.
 */
export default function WebcamMonitor({ wsUrl }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const wsRef = useRef(null);
  const [connected, setConnected] = useState(false);
  const [faceStatus, setFaceStatus] = useState('UNKNOWN');
  const [gaze, setGaze] = useState('unknown');

  // Request webcam access
  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
        if (videoRef.current && active) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error('Failed to getUserMedia', err);
      }
    })();
    return () => {
      active = false;
      const stream = videoRef.current?.srcObject;
      if (stream && stream.getTracks) {
        stream.getTracks().forEach((t) => t.stop());
      }
    };
  }, []);

  // WebSocket connection
  useEffect(() => {
    const ws = new WebSocket(wsUrl);
    wsRef.current = ws;
    ws.onopen = () => {
      setConnected(true);
      ws.send(JSON.stringify({ type: 'client_connected', ts: Date.now() }));
    };
    ws.onclose = () => setConnected(false);
    ws.onerror = () => setConnected(false);
    return () => ws.close();
  }, [wsUrl]);

  // Browser/tab/FS events
  useEffect(() => {
    const send = (payload) => {
      if (wsRef.current && wsRef.current.readyState === 1) {
        wsRef.current.send(JSON.stringify(payload));
      }
    };

    const onVisibility = () => {
      send({ type: document.visibilityState === 'hidden' ? 'visibilityhidden' : 'visibilityvisible', ts: Date.now() });
    };
    const onFullscreen = () => {
      const fs = document.fullscreenElement != null;
      send({ type: fs ? 'fullscreen_enter' : 'fullscreen_exit', ts: Date.now() });
    };
    const onBlur = () => send({ type: 'window_blur', ts: Date.now() });
    const onFocus = () => send({ type: 'window_focus', ts: Date.now() });

    document.addEventListener('visibilitychange', onVisibility);
    document.addEventListener('fullscreenchange', onFullscreen);
    window.addEventListener('blur', onBlur);
    window.addEventListener('focus', onFocus);
    return () => {
      document.removeEventListener('visibilitychange', onVisibility);
      document.removeEventListener('fullscreenchange', onFullscreen);
      window.removeEventListener('blur', onBlur);
      window.removeEventListener('focus', onFocus);
    };
  }, []);

  // Face detection
  useEffect(() => {
    const interval = setInterval(async () => {
      if (videoRef.current && canvasRef.current) {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        canvas.width = videoRef.current.videoWidth;
        canvas.height = videoRef.current.videoHeight;
        ctx.drawImage(videoRef.current, 0, 0);

        // Convert to base64
        const imageData = canvas.toDataURL('image/jpeg', 0.8).split(',')[1];

        try {
          const response = await fetch('http://localhost:8000/detect_face', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image: imageData }),
          });
          const result = await response.json();
          setFaceStatus(result.status);
          setGaze(result.gaze);
          // Send face status via WebSocket
          if (wsRef.current && wsRef.current.readyState === 1) {
            wsRef.current.send(JSON.stringify({ type: 'face_status', status: result.status, face_count: result.face_count, gaze: result.gaze, ts: Date.now() }));
          }
        } catch (err) {
          console.error('Face detection failed', err);
        }
      }
    }, 1000); // Every second

    return () => clearInterval(interval);
  }, []);

  const enterFullscreen = async () => {
    try {
      await document.documentElement.requestFullscreen();
    } catch (e) {
      console.error('Fullscreen request failed', e);
    }
  };

  const exitFullscreen = async () => {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
    } catch (e) {
      console.error('Fullscreen exit failed', e);
    }
  };

  return (
    <div style={{ display: 'grid', gap: 12 }}>
      <div>
        <strong>WS:</strong> {connected ? 'connected' : 'disconnected'}
      </div>
      <div>
        <strong>Face Status:</strong> {faceStatus}
      </div>
      <div>
        <strong>Gaze:</strong> {gaze}
      </div>
      <video ref={videoRef} autoPlay playsInline muted style={{ width: 480, background: '#111' }} />
      <canvas ref={canvasRef} style={{ display: 'none' }} />
      <div style={{ display: 'flex', gap: 8 }}>
        <button onClick={enterFullscreen}>Start Monitoring (Enter Fullscreen)</button>
        <button onClick={exitFullscreen}>Stop Monitoring (Exit Fullscreen)</button>
      </div>
    </div>
  );
}
