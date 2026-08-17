from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='ManPro AI – Vision API', version='0.1.0')
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173'], allow_methods=['*'], allow_headers=['*'])

CAMERAS = [
    {'id':'CAM-001','name':'Road Junction','location':'Main Street • East','category':'Road','status':'online','fps':25,'ai_enabled':True},
    {'id':'CAM-002','name':'Highway View','location':'NH-44 • Northbound','category':'Highway','status':'online','fps':24,'ai_enabled':True},
    {'id':'CAM-003','name':'Home Gate','location':'Residence • Gate 1','category':'Home Gate','status':'online','fps':25,'ai_enabled':True},
    {'id':'CAM-004','name':'Parking Area','location':'Building A • Level 1','category':'Parking','status':'online','fps':23,'ai_enabled':True},
]
EVENTS = [
    {'id':'EVT-20260817-00041','camera_id':'CAM-003','camera_name':'Home Gate','event_type':'Restricted Area Intrusion','object_type':'person','tracking_id':'P014','confidence':.97,'severity':'critical','status':'new'},
    {'id':'EVT-20260817-00040','camera_id':'CAM-002','camera_name':'Highway View','event_type':'Vehicle Stopped','object_type':'car','tracking_id':'V032','confidence':.94,'severity':'warning','status':'new'},
]
@app.get('/health')
def health(): return {'status':'healthy','service':'manpro-ai-vision'}
@app.get('/api/cameras')
def cameras(): return CAMERAS
@app.post('/api/cameras', status_code=201)
def add_camera(camera: dict):
    item={'id':f'CAM-{len(CAMERAS)+1:03}','status':'online','fps':25,'ai_enabled':True,**camera}; CAMERAS.append(item); return item
@app.get('/api/events')
def events(): return EVENTS
@app.get('/api/events/{event_id}')
def event(event_id: str):
    for item in EVENTS:
        if item['id'] == event_id: return item
    return {'error':'Event not found'}
@app.get('/api/alerts')
def alerts(): return [item for item in EVENTS if item['severity'] in {'critical','warning'}]
@app.post('/api/alerts/{event_id}/acknowledge')
def acknowledge(event_id: str): return {'id':event_id,'status':'acknowledged'}
@app.get('/api/analytics/dashboard')
def analytics(): return {'cameras':{'total':24,'online':21,'offline':3},'detections':{'people_today':1284,'vehicles_today':3648,'events_today':2497},'alerts_active':6}
@app.get('/api/system/status')
def system_status(): return {'demo_mode':True,'ai_engine':'running','processing_device':'CPU','inference_fps':18.4,'active_streams':4}
@app.post('/api/ai/{action}')
def ai(action: str): return {'engine':'running' if action == 'start' else 'stopped'}
