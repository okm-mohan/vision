import { Maximize2, MoreHorizontal, Radio, Volume2, Camera as CameraIcon } from 'lucide-react';
import type { Camera } from '../data/demo';

export function CameraFeed({camera, large=false}: {camera:Camera; large?:boolean}) {
  return <article className={`camera-feed ${camera.tone} ${large?'large':''}`}><video className="cctv-video" autoPlay loop muted playsInline preload="auto" onCanPlay={(event) => { event.currentTarget.play().catch(() => undefined); }} src={`/sample_media/${camera.tone}.mp4`} />
    <div className="feed-sky"/><div className="feed-road"><i/><i/><i/><i/></div><div className="building b1"/><div className="building b2"/>
    <div className="bbox person"><span>Person #P014&nbsp; 96%</span></div><div className="bbox vehicle"><span>{camera.tone==='highway'?'Truck':'Car'} #V032&nbsp; 94%</span></div>
    <div className="feed-top"><div><b>{camera.id}</b><small>{camera.name} · {camera.location}</small></div><div className="live"><Radio size={13}/> LIVE</div></div>
    <div className="feed-bottom"><div><span className={camera.status==='online'?'dot on':'dot off'}/>{camera.status.toUpperCase()} <em>• AI ACTIVE</em></div><small>FPS: {camera.fps || '—'} &nbsp; {camera.objects} objects</small></div>
    <div className="feed-actions"><button title="Snapshot"><CameraIcon size={15}/></button><button title="Audio"><Volume2 size={15}/></button><button title="Fullscreen"><Maximize2 size={15}/></button><button title="More"><MoreHorizontal size={15}/></button></div>
  </article>
}
