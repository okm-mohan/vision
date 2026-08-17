export type Camera = { id:string; name:string; location:string; status:'online'|'offline'; fps:number; objects:number; tone:string };
export type Event = { id:string; type:string; camera:string; time:string; confidence:number; severity:'critical'|'warning'|'info'|'normal'; object:string };

export const cameras: Camera[] = [
  {id:'CAM-001',name:'Road Junction',location:'Main Street • East',status:'online',fps:25,objects:11,tone:'road'},
  {id:'CAM-002',name:'Highway View',location:'NH-44 • Northbound',status:'online',fps:24,objects:18,tone:'highway'},
  {id:'CAM-003',name:'Home Gate',location:'Residence • Gate 1',status:'online',fps:25,objects:2,tone:'gate'},
  {id:'CAM-004',name:'Parking Area',location:'Building A • Level 1',status:'online',fps:23,objects:9,tone:'parking'},
  {id:'CAM-005',name:'Warehouse Dock',location:'Sector 8 • Bay 3',status:'offline',fps:0,objects:0,tone:'warehouse'},
  {id:'CAM-006',name:'Office Entrance',location:'HQ • Lobby',status:'online',fps:25,objects:4,tone:'office'},
];
export const events: Event[] = [
  {id:'EVT-20260817-00041',type:'Restricted Area Intrusion',camera:'Home Gate',time:'18:42:15',confidence:97,severity:'critical',object:'Person #P014'},
  {id:'EVT-20260817-00040',type:'Vehicle Stopped',camera:'Highway View',time:'18:41:54',confidence:94,severity:'warning',object:'Car #V032'},
  {id:'EVT-20260817-00039',type:'Motion Detected',camera:'Parking Area',time:'18:40:11',confidence:89,severity:'info',object:'Motion zone'},
  {id:'EVT-20260817-00038',type:'Person Detected',camera:'Road Junction',time:'18:39:02',confidence:96,severity:'normal',object:'Person #P019'},
];
