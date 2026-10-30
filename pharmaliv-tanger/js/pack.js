// PharmaLiv — Motion Pack V2 (index showcase). Adapted from the VERTEX Motion Pack engine:
// ONE rAF loop, per-scene lerped progress, transform/opacity only. Never touches the order form.
(function(){
"use strict";
var C = window.CONFIG; if(!C) return;
var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
document.documentElement.classList.add(reduced ? "mp-static" : "mp-live");

var clamp = function(v,a,b){ return Math.max(a, Math.min(b, v)); };
var vh = function(){ return window.innerHeight; };
function progress(el){
  var r = el.getBoundingClientRect(), h = el.offsetHeight;
  if(h > vh()) return clamp(-r.top / (h - vh()), 0, 1);
  return clamp((vh() - r.top) / (vh() + h), 0, 1);
}
function near(el, m){
  var r = el.getBoundingClientRect();
  return r.bottom > -m && r.top < vh() + m;
}

/* ================= builders ================= */
var WA = function(msg){ return "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(msg || C.defaultMessageAr); };

/* TUNNEL posters — real site photos, 4 per wall */
var TUNNEL_PHOTOS = [
  { src:"img/owner-hero.webp",       alt:"Le fondateur de PharmaLiv en uniforme, sac de livraison à la main, dans une pharmacie — صاحب PharmaLiv بزي الشركة وحقيبة التوصيل داخل صيدلية" },
  { src:"img/owner-night.webp",      alt:"Livraison de nuit : le livreur PharmaLiv en casque devant une pharmacie éclairée — التوصيل بالليل: موصّل PharmaLiv بالخوذة قدام صيدلية مضيئة" },
  { src:"img/owner-partner-p.webp",  alt:"Réception d'une commande au comptoir d'une pharmacie — استلام طلب عند كونطوار الصيدلية" },
  { src:"img/owner-scooter.webp",    alt:"Le livreur PharmaLiv à scooter rue d'Italie à Tanger — موصّل PharmaLiv على دراجة نارية في شارع إيطاليا بطنجة" },
  { src:"img/owner-dispatch-p.webp", alt:"Le dispatch PharmaLiv devant la carte des quartiers de Tanger — مركز طلبات PharmaLiv قدام خريطة أحياء طنجة" },
  { src:"img/owner-handover.webp",   alt:"Remise d'une commande à domicile, à la porte de la cliente — تسليم طلب حتى لباب دار الزبونة" },
  { src:"img/owner-mother-p.webp",   alt:"Livraison à domicile avec le sac PharmaLiv Tanger — التوصيل للمنزل بحقيبة PharmaLiv Tanger" },
  { src:"img/owner-packing.webp",    alt:"Préparation d'une commande de médicaments en pharmacie — تجهيز طلب دواء داخل الصيدلية" },
  { src:"img/owner-hero-b.webp",     alt:"Portrait du fondateur en uniforme PharmaLiv — صورة صاحب الشركة بزي PharmaLiv" },
  { src:"img/owner-night-b.webp",    alt:"Service de nuit PharmaLiv : casque et caisse de livraison — خدمة الليل PharmaLiv: الخوذة وصندوق التوصيل" }
];
var posters = [];
var postersBox = document.getElementById("mpPosters");
if(postersBox){
  var perSide = [0,0];
  TUNNEL_PHOTOS.forEach(function(p, idx){
    var side = idx % 2 === 0 ? -1 : 1;
    var d = document.createElement("div");
    d.className = "mp-poster";
    var im = document.createElement("img");
    im.src = p.src; im.alt = p.alt; im.decoding = "async";
    if(idx > 1) im.loading = "lazy";
    d.appendChild(im); postersBox.appendChild(d);
    posters.push({ el:d, side:side, i:perSide[side < 0 ? 0 : 1]++ });
  });
}

/* ORBIT nodes — the 6 services, same icons/titles as the cards below */
var SERVICES = [
  { t:"توصيل الأدوية للمنزل", svg:'<path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>' },
  { t:"صيدلية الحراسة",       svg:'<path d="M12 3l7 3v5c0 5-3.2 8.4-7 10-3.8-1.6-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/>' },
  { t:"توصيل بالليل",         svg:'<path d="M20 13.5A8 8 0 1 1 10.5 4 6.5 6.5 0 0 0 20 13.5z"/>' },
  { t:"إرسال الوصفة بواتساب", svg:'<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h5M10 17h5"/>' },
  { t:"بارافارماسي وأم وطفل", svg:'<circle cx="12" cy="8" r="3.2"/><path d="M5 21c.8-3.6 3.6-5.4 7-5.4s6.2 1.8 7 5.4"/>' },
  { t:"كل أحياء طنجة",        svg:'<path d="M12 21s-7-5.5-7-11a7 7 0 1 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/>' }
];
var nodes = [];
var nodesBox = document.getElementById("mpOrbitNodes");
if(nodesBox){
  SERVICES.forEach(function(s){
    var d = document.createElement("div");
    d.className = "mp-node";
    d.innerHTML = '<span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + s.svg + '</svg></span><strong>' + s.t + '</strong>';
    nodesBox.appendChild(d); nodes.push(d);
  });
}

/* REEL FLUX panels — all site photos with honest illustrative captions */
var PANELS = [
  { src:"img/owner-scooter.webp",    cap:"الموصّل في الطريق",   alt:"Le livreur PharmaLiv à scooter rue d'Italie à Tanger — موصّل PharmaLiv على دراجة نارية في طنجة" },
  { src:"img/owner-partner-p.webp",  cap:"عند كونطوار الصيدلية", alt:"Réception d'une commande au comptoir d'une pharmacie — استلام طلب عند كونطوار الصيدلية" },
  { src:"img/owner-night.webp",      cap:"خدمة الليل",           alt:"Livraison de nuit devant une pharmacie de garde — التوصيل بالليل قدام صيدلية الحراسة" },
  { src:"img/owner-packing.webp",    cap:"رفوف الصيدلية",        alt:"Préparation d'une commande devant les rayonnages de la pharmacie — تجهيز طلب قدام رفوف الصيدلية" },
  { src:"img/owner-mother-p.webp",   cap:"حتى لباب الدار",        alt:"Livraison à domicile, sac PharmaLiv Tanger à la main — التوصيل حتى لباب الدار بحقيبة PharmaLiv" },
  { src:"img/owner-handover.webp",   cap:"صندوق التوصيل",        alt:"Remise du sac de livraison PharmaLiv à une cliente — تسليم حقيبة PharmaLiv للزبونة" },
  { src:"img/owner-dispatch-p.webp", cap:"طنجة",                 alt:"Le dispatch PharmaLiv devant la carte de Tanger — مركز الطلبات قدام خريطة طنجة" },
  { src:"img/owner-hero.webp",       cap:"في الصيدلية",          alt:"Le fondateur de PharmaLiv en uniforme dans une pharmacie — صاحب PharmaLiv بزي الشركة داخل صيدلية" },
  { src:"img/owner-packing-b.webp",  cap:"تحضير الطلب",          alt:"Le fondateur range un médicament dans le sac de livraison — صاحب الشركة كيحط دواء في حقيبة التوصيل" },
  { src:"img/owner-scooter-b.webp",  cap:"قدام الصيدلية",        alt:"Le livreur PharmaLiv devant une pharmacie 24/24 à Tanger — موصّل PharmaLiv قدام صيدلية 24/24 في طنجة" },
  { src:"img/owner-partner-p2.webp", cap:"تسليم بالوصفة",        alt:"La pharmacienne remet le sac de la commande au livreur — الصيدلية كتسلم حقيبة الطلب للموصّل" },
  { src:"img/owner-night-b.webp",    cap:"من صيدلية الحراسة",    alt:"Le livreur de nuit PharmaLiv et sa caisse de livraison — موصّل الليل PharmaLiv وصندوق التوصيل" }
];
var panels = [];
var track = document.getElementById("mpTrack");
if(track){
  PANELS.forEach(function(p){
    var f = document.createElement("figure");
    f.className = "mp-panel";
    f.innerHTML = '<img src="' + p.src + '" alt="' + p.alt + '" loading="lazy" decoding="async"><figcaption>' + p.cap + '</figcaption>';
    track.appendChild(f); panels.push(f);
  });
}

/* CASCADE zone cards — built from CONFIG, same click behaviour as app.js zone cards */
var zcards = [];
var zbox = document.getElementById("mpZcards");
if(zbox){
  C.zones.forEach(function(z, i){
    var a = document.createElement("a");
    a.className = "mp-zcard"; a.href = "zones-livraison-tanger.html";
    a.innerHTML = '<span class="zone-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-5.5-7-11a7 7 0 1 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg></span><span><strong>' + z.ar + '</strong><small dir="ltr">' + z.fr + '</small></span>';
    (function(zone){
      a.addEventListener("click", function(ev){
        ev.preventDefault();
        window.open(WA("السلام، أريد طلب توصيل دواء إلى حي " + zone.ar + " (" + zone.fr + ") في طنجة."), "_blank");
      });
    })(z);
    a.style.left = (2.5 + i * (window.innerWidth < 761 ? 5.2 : 7.7)) + "%";
    a.style.top = (3 + i * 7.55) + "%";
    a.style.zIndex = String(10 + i);
    zbox.appendChild(a); zcards.push(a);
  });
}

/* SCATTER blocks */
var scatters = Array.prototype.map.call(document.querySelectorAll(".mp-sc"), function(el){
  return { el:el, sp:parseFloat(el.getAttribute("data-speed") || "1.2"), rot:parseFloat(el.getAttribute("data-rot") || "0") };
});

/* WAVY paths */
var waveB = document.getElementById("mpWaveB"), waveF = document.getElementById("mpWaveF");
function waveD(base, amp, phase){
  var pts = [], N = 12, i, x, y;
  for(i = 0; i <= N; i++){
    x = i * (100 / N);
    y = base + Math.sin(x * 0.11 + phase) * amp + Math.sin(x * 0.045 - phase * 0.7) * amp * 0.6;
    pts.push("L" + x.toFixed(1) + "," + y.toFixed(1));
  }
  return "M0," + base.toFixed(1) + " " + pts.join(" ") + " L100,100 L0,100 Z";
}

/* FLUX drag */
var lens = document.getElementById("mpLens");
var dragX = 0, dragging = false, lastX = 0;
if(lens && !reduced){
  lens.addEventListener("pointerdown", function(e){
    dragging = true; lastX = e.clientX;
    try{ lens.setPointerCapture(e.pointerId); }catch(_){}
  });
  lens.addEventListener("pointermove", function(e){
    if(!dragging) return;
    dragX += e.clientX - lastX; lastX = e.clientX;
  });
  ["pointerup","pointercancel"].forEach(function(ev){
    lens.addEventListener(ev, function(){ dragging = false; });
  });
}

/* ================= scenes ================= */
var tunnelEl = document.getElementById("mpTunnel");
var orbitWrap = document.getElementById("mpOrbit");
var orbitStage = orbitWrap ? orbitWrap.querySelector(".mp-orbit-stage") : null;
var stepsEl = document.querySelector(".mp-steps");
var fluxEl = document.getElementById("mpFlux");
var nightEl = document.querySelector(".dark-band");
var cascadeEl = document.getElementById("mpCascade");

var scenes = [];
function addScene(el, render){ if(el) scenes.push({ el:el, render:render, cur:0, tgt:0 }); }

if(!reduced) addScene(tunnelEl, function(p){
  var xo = window.innerWidth < 761 ? 30 : 45;
  for(var k = 0; k < posters.length; k++){
    var t = posters[k];
    var z = -t.i * 300 - (t.side > 0 ? 150 : 0) + p * 2150;
    var op = Math.min(clamp((z + 1750) / 450, 0, 1), clamp((330 - z) / 260, 0, 1));
    var yo = window.innerWidth < 761 ? 0 : (t.i % 2 ? -8 : 8);
    t.el.style.opacity = op.toFixed(3);
    t.el.style.transform = "translate(-50%,-50%) translate3d(" + (t.side * xo) + "vmin," + yo + "vmin," + z.toFixed(0) + "px) rotateY(" + (t.side * -62) + "deg)";
  }
});

addScene(orbitWrap, function(p, t){
  if(!orbitStage || !nodes.length) return;
  var w = orbitStage.clientWidth, mobile = w < 761;
  var rx = mobile ? w * 0.38 : Math.min(w * 0.37, 440);
  var ry = Math.min(rx * (mobile ? 0.55 : 0.66), orbitStage.clientHeight * 0.30);
  var rot = reduced ? 0.9 : (mobile ? t * 0.07 + p * 1.2 : p * 2.2 + t * 0.035);
  var N = nodes.length;
  for(var i = 0; i < N; i++){
    var a = (i / N) * Math.PI * 2 + rot;
    var depth = (Math.sin(a) + 1) / 2;
    var s = reduced ? 0.8 : (mobile ? 0.82 : 0.45 + depth * 0.75);
    var el = nodes[i];
    el.style.zIndex = String(Math.round(depth * 30) + 1);
    el.style.opacity = reduced ? "0.97" : (mobile ? "0.97" : (0.35 + depth * 0.65).toFixed(3));
    el.style.transform = "translate(-50%,-50%) translate(" + (Math.cos(a) * rx).toFixed(1) + "px," + (Math.sin(a) * ry).toFixed(1) + "px) scale(" + s.toFixed(3) + ")";
  }
});

if(!reduced) addScene(stepsEl, function(p){
  if(window.innerWidth < 1360) {
    for(var j = 0; j < scatters.length; j++) scatters[j].el.style.transform = "";
    return;
  }
  for(var i = 0; i < scatters.length; i++){
    var b = scatters[i];
    var dy = (0.5 - p) * b.sp * 90;
    b.el.style.transform = "translate3d(0," + dy.toFixed(1) + "px,0) rotate(" + b.rot + "deg)";
  }
});

var fluxMax = 0;
function fluxMeasure(){ if(track && lens) fluxMax = Math.max(0, track.scrollWidth - lens.clientWidth); }
if(!reduced) addScene(fluxEl, function(p){
  if(!track || !lens) return;
  if(!fluxMax) fluxMeasure();
  var shift = clamp(p * fluxMax - dragX, 0, fluxMax);
  track.style.transform = "translate3d(" + (-shift).toFixed(1) + "px,0,0)";
  var lr = lens.getBoundingClientRect(), cx = lr.left + lr.width / 2;
  for(var i = 0; i < panels.length; i++){
    var r = panels[i].getBoundingClientRect(), c = r.left + r.width / 2;
    var d = clamp(1 - Math.abs(c - cx) / (lr.width * 0.62), 0, 1);
    panels[i].style.transform = "scale(" + (1 + d * 0.05).toFixed(3) + ")";
  }
});

if(!reduced) addScene(nightEl, function(p, t){
  if(!waveB || !waveF) return;
  var ph = p * 5.5 + t * 0.8;
  waveB.setAttribute("d", waveD(56, 3.4, ph + 1.7));
  waveF.setAttribute("d", waveD(66, 3.4, ph));
});

if(!reduced) addScene(cascadeEl, function(p){
  var gx = (0.5 - p) * 13, gy = (0.5 - p) * 9;
  for(var i = 0; i < zcards.length; i++){
    var extra = (0.5 - p) * i * 2.4;
    zcards[i].style.transform = "translate(" + (gx + extra).toFixed(1) + "vmin," + (gy + extra * 0.72).toFixed(1) + "vmin) rotate(" + (-5 + p * 3.5 + i * 0.3).toFixed(2) + "deg)";
  }
});

/* ================= signature pill ================= */
var pillSections = Array.prototype.map.call(document.querySelectorAll("[data-mp-name]"), function(el){
  return { el:el, name:el.getAttribute("data-mp-name"), scene:el.hasAttribute("data-mp-scene") };
});
var ctlName = document.getElementById("mpCtlName"),
    ctlFill = document.getElementById("mpCtlFill"),
    ctlPct = document.getElementById("mpCtlPct");
var lastName = "", lastPct = -1;
function pill(){
  if(!ctlName) return;
  var mid = vh() * 0.45, active = null, i, r;
  for(i = 0; i < pillSections.length; i++){
    r = pillSections[i].el.getBoundingClientRect();
    if(r.top <= mid && r.bottom > mid){ active = pillSections[i]; break; }
  }
  if(!active) active = pillSections[0];
  if(!active) return;
  var pc;
  if(active.scene){
    var sc = null;
    for(i = 0; i < scenes.length; i++) if(scenes[i].el === active.el) sc = scenes[i];
    pc = Math.round((sc ? sc.cur : progress(active.el)) * 100);
  } else {
    var dh = document.documentElement.scrollHeight - vh();
    pc = Math.round(clamp(window.scrollY / Math.max(dh, 1), 0, 1) * 100);
  }
  if(active.name !== lastName){ ctlName.textContent = active.name; lastName = active.name; }
  if(pc !== lastPct){ ctlPct.textContent = pc + "%"; ctlFill.style.width = pc + "%"; lastPct = pc; }
}

/* ================= the loop ================= */
var t0 = performance.now();
function frame(now){
  var t = reduced ? 0 : (now - t0) / 1000;
  for(var i = 0; i < scenes.length; i++){
    var s = scenes[i];
    s.tgt = progress(s.el);
    s.cur += (s.tgt - s.cur) * (reduced ? 1 : 0.085);
    if(near(s.el, vh() * 0.6)) s.render(s.cur, t);
  }
  pill();
  requestAnimationFrame(frame);
}
window.addEventListener("resize", function(){ fluxMax = 0; }, { passive:true });
fluxMeasure();
requestAnimationFrame(frame);
})();
