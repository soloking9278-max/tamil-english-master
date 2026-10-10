const CACHE_NAME = "tem-general-10000-v2";
const APP_SHELL = ["./", "./index.html", "./manifest.json", "./icon.svg"];
self.addEventListener("install", event => { event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(APP_SHELL))); self.skipWaiting(); });
self.addEventListener("activate", event => { event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);
  if (event.request.method !== "GET" || url.origin !== self.location.origin) return;
  const asset = url.pathname.endsWith("/examples.json") ? "./examples.json" : url.pathname.endsWith("/daily.json") ? "./daily.json" : null;
  if (asset) {
    event.respondWith(fetch(event.request, {cache:"no-store"}).then(response => { if (response.ok) caches.open(CACHE_NAME).then(c => c.put(asset, response.clone())); return response; }).catch(() => caches.match(asset)));
    return;
  }
  event.respondWith(caches.match(event.request).then(hit => hit || fetch(event.request).then(response => { caches.open(CACHE_NAME).then(c => c.put(event.request, response.clone())); return response; }).catch(() => caches.match("./index.html"))));
});