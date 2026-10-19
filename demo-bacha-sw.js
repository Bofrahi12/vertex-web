const C = 'bacha-v34';
const CORE = ['demo-bacha.html', 'demo-bacha/chef-medallion.webp', 'demo-bacha/favicon.svg', 'manifest.webmanifest'];
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  if (e.request.mode === 'navigate' || u.pathname.endsWith('demo-bacha.html')) {
    e.respondWith(fetch(e.request).then(r => { const cl = r.clone(); caches.open(C).then(c => c.put('demo-bacha.html', cl)); return r; }).catch(() => caches.match('demo-bacha.html')));
  } else {
    e.respondWith(caches.match(e.request).then(m => m || fetch(e.request).then(r => { const cl = r.clone(); caches.open(C).then(c => c.put(e.request, cl)); return r; })));
  }
});
