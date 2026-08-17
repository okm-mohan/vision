# ManPro AI – Vision

Professional AI Video Intelligence & Surveillance Platform. This workspace implements a polished Phase 1 command-center UI, a functional demo API, and Phase 2 computer-vision extension points.

## Included

- React + TypeScript + Vite desktop-first surveillance dashboard
- Live multi-camera wall with generated CCTV-style feeds, AI labels, LIVE/REC states, and demo mode
- Event timeline, searchable AI event table, analytics activity chart, responsive navigation
- FastAPI demo service for cameras, events, alerts, analytics, system status, and AI controls
- YOLO detector and tracking interface prepared for Phase 2
- Safe placeholder media workflow; no camera or copyrighted footage required

## Run the dashboard

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

## Run the API

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs are available at `http://localhost:8000/docs`.

## Add media and AI detection

Place licensed footage in `sample_media/` (for example, `road.mp4`). To enable Phase 2 inference, install `opencv-python` and `ultralytics`, call `YOLODetector.start()`, then feed OpenCV frames into `detect()`. The API/UI remains usable in Demo Mode without media or a real camera.

## RTSP next step

Store RTSP addresses server-side only, never in frontend configuration. Add a camera via `POST /api/cameras`, then implement a backend stream worker that reads the RTSP feed and emits event/snapshot records.

## Architecture

```text
frontend/       React command center
backend/app/    FastAPI demo and API surface
ai_engine/      YOLO / tracking contracts
sample_media/   Licensed local MP4 files (optional)
snapshots/      Generated event images
event_clips/    Generated event video clips
```
