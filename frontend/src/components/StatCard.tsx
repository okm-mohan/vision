import { LucideIcon } from 'lucide-react';
export function StatCard({label,value,sub,icon:Icon,tone='cyan'}:{label:string;value:string;sub:string;icon:LucideIcon;tone?:string}) { return <div className="stat-card"><div><p>{label}</p><h2>{value}</h2><small className={tone}>{sub}</small></div><span className={`stat-icon ${tone}`}><Icon size={21}/></span></div> }
