// Local-only diagram rendering. Resolve dependencies locally or through explicit environment overrides.
import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import {createRequire} from 'node:module';
const root=path.resolve(process.argv[2]||'.');
const require=createRequire(import.meta.url);
const {chromium}=require(process.env.ISO20022_PLAYWRIGHT_MODULE || 'playwright');
let mermaidRoot=process.env.ISO20022_MERMAID_ROOT;
if(!mermaidRoot){
 try{mermaidRoot=path.dirname(require.resolve('mermaid/package.json'));}
 catch{mermaidRoot=path.join(root,'work/renderer/package');}
}
mermaidRoot=path.resolve(mermaidRoot);
const version=JSON.parse(await fs.readFile(path.join(mermaidRoot,'package.json'),'utf8')).version;
const dir=path.resolve(root,process.argv[3]||'work/workbook-diagrams');
const out=path.resolve(root,process.argv[4]||'shared/assets/src-000198/reconstructed-introduction');
await fs.mkdir(out,{recursive:true});
const server=http.createServer(async(req,res)=>{
 try{
  if(req.url==='/'){res.writeHead(200,{'Content-Type':'text/html'});res.end('<html><head><style>body{margin:16px;background:white}#drawing{display:inline-block}</style></head><body><div id="drawing"></div><script type="module">import mermaid from "/dist/mermaid.esm.min.mjs";window.mermaid=mermaid;mermaid.initialize({startOnLoad:false,securityLevel:"strict",theme:"default",flowchart:{htmlLabels:false},fontFamily:"Arial"});</script></body></html>');return;}
  const file=path.resolve(mermaidRoot,'.'+decodeURIComponent(req.url.split('?')[0]));
  if(!file.startsWith(mermaidRoot+path.sep))throw Error('outside renderer');
  const b=await fs.readFile(file);res.writeHead(200,{'Content-Type':file.endsWith('.mjs')||file.endsWith('.js')?'text/javascript':'application/octet-stream'});res.end(b);
 }catch(e){res.writeHead(404);res.end('not found');}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const browser=await chromium.launch({headless:true,...(process.env.ISO20022_BROWSER_EXECUTABLE ? {executablePath:process.env.ISO20022_BROWSER_EXECUTABLE} : {})});
const page=await browser.newPage({viewport:{width:1800,height:1400},deviceScaleFactor:1});
const report=[];
try{
 await page.goto('http://127.0.0.1:'+server.address().port+'/');await page.waitForFunction(()=>!!window.mermaid,{timeout:30000});
 for(const file of (await fs.readdir(dir)).filter(x=>x.endsWith('.mmd')).sort()){
  const code=await fs.readFile(path.join(dir,file),'utf8');const id=file.slice(0,-4);let result;
  try{
   const svg=await page.evaluate(async({code,id})=>{await mermaid.parse(code);const r=await mermaid.render('diagram'+id.replace(/[^a-zA-Z0-9]/g,''),code);document.getElementById('drawing').innerHTML=r.svg;const s=document.querySelector('#drawing svg');s.style.maxWidth='none';s.setAttribute('width',s.viewBox.baseVal.width);s.setAttribute('height',s.viewBox.baseVal.height);return s.outerHTML;},{code,id});
   await fs.writeFile(path.join(out,id+'.svg'),svg);const box=await page.locator('#drawing').boundingBox();await page.setViewportSize({width:Math.max(1800,Math.ceil(box.width)+40),height:Math.max(1400,Math.ceil(box.height)+40)});await page.evaluate(()=>window.scrollTo(0,0));await page.locator('#drawing').screenshot({path:path.join(out,id+'.png')});
   result={diagram:id,result:'pass',renderer:'Mermaid browser API + Chromium '+browser.version(),version,date:'2026-11-09',svg:path.relative(root,path.join(out,id+'.svg')).replaceAll('\\','/'),png:path.relative(root,path.join(out,id+'.png')).replaceAll('\\','/')};
  }catch(e){result={diagram:id,result:'fail',version,error:String(e)};}
  report.push(result);console.log(JSON.stringify(result));
 }
 await fs.writeFile(path.resolve(root,process.argv[5]||'work/workbook-diagram-render-report.json'),JSON.stringify(report,null,2));
}finally{await browser.close();server.close();}
