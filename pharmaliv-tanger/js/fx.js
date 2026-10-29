// PharmaLiv FX — 3D depth layer. Transform/opacity only (FAQ height on click excepted).
// No effect ever touches the order form. Everything is gated on reduced-motion / pointer type.
(function(){
  "use strict";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(pointer: fine)").matches;

  /* Active nav state (cluster pages) */
  var page = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.main a").forEach(function(a){
    if(a.getAttribute("href") === page){ a.classList.add("active"); a.setAttribute("aria-current","page"); }
  });

  /* Share button (footer) — native share, WhatsApp fallback */
  document.querySelectorAll("[data-share]").forEach(function(b){
    b.addEventListener("click", function(){
      var data = { title: document.title,
                   text: "PharmaLiv Tanger — توصيل الدواء في طنجة 24/24",
                   url: location.href };
      if(navigator.share){ navigator.share(data).catch(function(){}); }
      else { window.open("https://wa.me/?text=" + encodeURIComponent(data.text + " " + data.url), "_blank"); }
    });
  });

  /* Back-to-top chip (injected, site-wide) */
  var top = document.createElement("button");
  top.className = "to-top"; top.type = "button";
  top.setAttribute("aria-label", "العودة إلى الأعلى");
  top.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
  document.body.appendChild(top);
  top.addEventListener("click", function(){ window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" }); });

  /* FAQ — smooth accordion (wrap body, animate height on toggle) */
  document.querySelectorAll("details.faq").forEach(function(d){
    var s = d.querySelector("summary"); if(!s) return;
    var body = document.createElement("div"); body.className = "faq-body";
    Array.prototype.slice.call(d.children).forEach(function(c){ if(c !== s) body.appendChild(c); });
    d.appendChild(body);
    var anim = null;
    s.addEventListener("click", function(e){
      e.preventDefault();
      if(anim){ anim.cancel(); anim = null; }
      if(reduced){ d.open = !d.open; return; }
      if(d.open){
        anim = body.animate([{ height: body.offsetHeight + "px" }, { height: "0px" }], { duration: 240, easing: "ease-in-out" });
        anim.onfinish = function(){ d.open = false; anim = null; };
      } else {
        d.open = true;
        anim = body.animate([{ height: "0px" }, { height: body.scrollHeight + "px" }], { duration: 300, easing: "ease-in-out" });
        anim.onfinish = function(){ anim = null; };
      }
    });
  });

  /* Scroll-driven: to-top visibility + night-band photo parallax (rAF-throttled) */
  var nightImgs = Array.prototype.slice.call(document.querySelectorAll(".dark-band figure.photo img"));
  var ticking = false;
  function onScroll(){
    ticking = false;
    top.classList.toggle("show", window.scrollY > 600);
    if(reduced) return;
    nightImgs.forEach(function(img){
      var r = img.parentElement.getBoundingClientRect();
      if(r.bottom < 0 || r.top > window.innerHeight) return;
      var d = (r.top + r.height / 2 - window.innerHeight / 2) / window.innerHeight;
      img.style.transform = "scale(1.14) translateY(" + (d * -16).toFixed(1) + "px)";
    });
  }
  window.addEventListener("scroll", function(){
    if(!ticking){ ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  if(reduced || !fine) return; /* tilt + hero parallax: desktop fine pointer only */

  /* Card tilt — services, steps, zones, cluster sibling cards. Max ~6deg. */
  document.querySelectorAll(".card, .step, .zone-card, .sib").forEach(function(el){
    el.classList.add("tilt");
    var raf = null, ev = null;
    el.addEventListener("pointermove", function(e){
      if(e.pointerType !== "mouse") return;
      ev = e;
      if(raf) return;
      raf = requestAnimationFrame(function(){
        raf = null;
        var r = el.getBoundingClientRect();
        var x = (ev.clientX - r.left) / r.width - .5;
        var y = (ev.clientY - r.top) / r.height - .5;
        el.classList.add("tilting");
        el.style.transform = "perspective(900px) rotateX(" + (-y * 6).toFixed(2) + "deg) rotateY(" + (x * 6).toFixed(2) + "deg)";
      });
    });
    el.addEventListener("pointerleave", function(){
      if(raf){ cancelAnimationFrame(raf); raf = null; }
      el.classList.remove("tilting");
      el.style.transform = "";
    });
  });

  /* Hero 3D stage — pointer parallax around the CSS base rotation */
  var stage = document.querySelector("[data-stage3d]");
  if(stage){
    var inner = stage.querySelector(".stage3d-inner");
    var hero = stage.closest(".hero") || stage;
    var BX = 5, BY = -6, tx = BX, ty = BY, cx = BX, cy = BY, loop = null;
    function frame(){
      cx += (tx - cx) * .08; cy += (ty - cy) * .08;
      inner.style.transform = "rotateX(" + cx.toFixed(2) + "deg) rotateY(" + cy.toFixed(2) + "deg)";
      if(Math.abs(tx - cx) > .02 || Math.abs(ty - cy) > .02){ loop = requestAnimationFrame(frame); }
      else { loop = null; }
    }
    function kick(){ if(!loop) loop = requestAnimationFrame(frame); }
    hero.addEventListener("pointermove", function(e){
      if(e.pointerType !== "mouse") return;
      var r = hero.getBoundingClientRect();
      ty = BY + ((e.clientX - r.left) / r.width - .5) * 5;
      tx = BX - ((e.clientY - r.top) / r.height - .5) * 4;
      kick();
    });
    hero.addEventListener("pointerleave", function(){ tx = BX; ty = BY; kick(); });
  }
})();
