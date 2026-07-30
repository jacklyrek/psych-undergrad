// Service worker — offline support.
//
// The reason this exists: the study loop should work on the Tube, in a basement, on a plane. All the
// content is static and already on the device after the first visit, so there's no good reason for a
// dead signal to stop a review session. Attempts graded offline queue in localStorage (see store.js)
// and upload when there's a network again.
//
// Strategy is stale-while-revalidate for everything: serve from cache instantly, refresh in the
// background, so the next launch has whatever was last deployed. That suits this app because a
// redeploy is a content rebuild rather than an urgent bug fix, and because on a phone the 3 MB
// content bundle must never be re-downloaded just to open the app.
//
// All paths are relative — GitHub Pages serves this from /psych-undergrad/, not the domain root.

// Bumping this name is what purges everything the previous version cached — `activate` deletes any
// cache whose name isn't this one. Bump it whenever the caching behaviour below changes.
const CACHE = 'psych-wiki-v2';

// GitHub Pages serves every file with `Cache-Control: max-age=600`, and a plain fetch() inside a
// service worker still goes through the browser's HTTP cache. That combination is what made deploys
// invisible: the worker would dutifully "revalidate" its cache and be handed back the same ten-
// minute-old bytes it already had. `no-cache` forces a conditional request to the origin — an ETag
// round-trip, so a 304 costs almost nothing — which means the worker always sees what is actually
// deployed. Requests by URL rather than by Request object because a 'navigate' Request cannot be
// reconstructed with a different cache mode.
function fetchFresh(request) {
  return fetch(request.url, { cache: 'no-cache', credentials: 'same-origin' });
}

const SHELL = [
  './',
  'index.html',
  'style.css',
  'app.js',
  'sm2.js',
  'store.js',
  'supabase.js',
  'session.js',
  'analytics.js',
  'config.js',
  'manifest.webmanifest',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/apple-touch-icon.png',
  'icons/favicon-32.png',
];

// content/*.json is deliberately NOT precached. The page fetches items.json and readings.json at
// boot anyway, and the fetch handler below caches whatever goes through it — precaching them here as
// well would mean downloading 3 MB twice on a first visit over cellular.

// The version check has to see the network or it can't do its job: cache.match() keys on URL and
// would happily answer with the very bundle we're asking whether to replace.
const ALWAYS_NETWORK = ['content/version.json'];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    // Individually, not addAll: one 404 (a content bundle not built yet) shouldn't fail the whole
    // install and leave the app with no offline support at all.
    await Promise.all(SHELL.map(async (path) => {
      try {
        const res = await fetch(new Request(path, { cache: 'reload' }));
        if (res.ok) await cache.put(path, res);
      } catch { /* precache is best-effort; the fetch handler fills gaps later */ }
    }));
    self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.filter((n) => n !== CACHE).map((n) => caches.delete(n)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  // Supabase is cross-origin and must never be cached — it's the live source of truth, and a stale
  // response would mean studying against yesterday's queue.
  if (url.origin !== self.location.origin) return;

  // Hash routing means every navigation is really the same document.
  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const fresh = await fetchFresh(request);
        if (fresh.ok) cache.put('index.html', fresh.clone());
        return fresh;
      } catch {
        return (await cache.match('index.html')) || (await cache.match('./'))
          || new Response('Offline, and the app shell was never cached.',
                          { status: 503, headers: { 'Content-Type': 'text/plain' } });
      }
    })());
    return;
  }

  if (ALWAYS_NETWORK.some((path) => url.pathname.endsWith(path))) {
    event.respondWith(fetchFresh(request).catch(async () =>
      (await caches.open(CACHE)).match(request)
      || new Response('{}', { status: 503, headers: { 'Content-Type': 'application/json' } })));
    return;
  }

  const opened = caches.open(CACHE);
  const revalidate = fetchFresh(request).then(async (res) => {
    if (res.ok) (await opened).put(request, res.clone());
    return res;
  });
  // Synchronously, while the event is still dispatching — calling waitUntil after an await is only
  // conditionally legal and throws once the event is no longer active.
  event.waitUntil(revalidate.catch(() => {}));

  event.respondWith((async () => {
    // Serve the cached copy immediately if there is one; the refresh above lands for next time.
    const cached = await (await opened).match(request);
    return cached || revalidate;
  })());
});
