const CACHE_NAME = "tem-general-diverse-v2";
const APP_SHELL = ["./", "./index.html", "./manifest.json", "./icon.svg"];
self.addEventListener("install", event => {
 event.waitUntil(caches.open(CACHE_NAME).then(cache=>cache.addAll(APP_SHELL)));
 self.skipWaiting();
});
self.addEventListener("activate", event => {
 event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE_NAME).map(k=>caches.delete(k)))));
 self.clients.claim();
});
self.addEventListener("fetch", event => {
 const url = new URL(event.request.url);
 if (event.request.method!=="GET" || url.origin!==self.location.origin) return;
 if (url.pathname.endsWith("/daily.json")) {
  event.respondWith(fetch(event.request,{cache:"no-store"}).then(resp=>{
   const cp=resp.clone();caches.open(CACHE_NAME).then(c=>c.put("./daily.json",cp));return resp;
  }).catch(()=>caches.match("./daily.json")));
  return;
 }
 if (url.pathname.endsWith("/examples.json")) {
  event.respondWith(caches.match("./examples.json").then(hit=>hit||fetch(event.request).then(resp=>{
   caches.open(CACHE_NAME).then(c=>c.put("./examples.json",resp.clone()));return resp;
  })));
  return;
 }
 event.respondWith(caches.match(event.request).then(hit=>hit||fetch(event.request).then(resp=>{
  caches.open(CACHE_NAME).then(c=>c.put(event.request,resp.clone()));return resp;
 }).catch(()=>caches.match("./index.html"))));
});