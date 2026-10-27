var C = 'yamal-v62';
self.addEventListener('install', function(e){ self.skipWaiting(); });
self.addEventListener('activate', function(e){
  e.waitUntil(caches.keys().then(function(ks){
    return Promise.all(ks.map(function(k){ return k === C ? null : caches.delete(k); }));
  }).then(function(){ return clients.claim(); }));
});
self.addEventListener('fetch', function(e){
  var u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  if (/\.(webp|jpg|png|woff2|svg)$/.test(u.pathname)) {
    e.respondWith(caches.open(C).then(function(c){ return c.match(e.request).then(function(h){ return h || fetch(e.request).then(function(r){ if (r && r.status === 200) c.put(e.request, r.clone()); return r; }); }); }));
  } else {
    e.respondWith(fetch(e.request).then(function(r){ if (r && r.status === 200) { var cl = r.clone(); caches.open(C).then(function(c){ c.put(e.request, cl); }); } return r; }).catch(function(){ return caches.match(e.request); }));
  }
});
