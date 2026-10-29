// Shared behaviour — everything reads name / WhatsApp / phone / zones from CONFIG (js/config.js).
(function(){
  const C = window.CONFIG; if(!C) return;
  const wa = (msg)=> "https://wa.me/"+C.whatsapp+"?text="+encodeURIComponent(msg||C.defaultMessageAr);
  document.querySelectorAll("[data-name]").forEach(e=>e.textContent=C.name);
  document.querySelectorAll("[data-phone]").forEach(e=>e.textContent=C.phoneDisplay);
  document.querySelectorAll("[data-tel]").forEach(e=>e.setAttribute("href",C.phoneHref));
  document.querySelectorAll("[data-wa]").forEach(e=>e.setAttribute("href",wa(e.getAttribute("data-wa-msg"))));
  // zones select
  document.querySelectorAll("[data-zones-select]").forEach(sel=>{
    C.zones.forEach(z=>{const o=document.createElement("option");o.value=z.fr+" — "+z.ar;o.textContent=z.ar+" · "+z.fr;sel.appendChild(o);});
  });
  // zones grids
  document.querySelectorAll("[data-zones-grid]").forEach(g=>{
    C.zones.forEach(z=>{
      const a=document.createElement("a"); a.className="zone-card"; a.href="zones-livraison-tanger.html";
      a.setAttribute("data-wa-zone",z.ar);
      a.innerHTML='<span class="zone-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-5.5-7-11a7 7 0 1 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg></span><span><strong>'+z.ar+'</strong><small dir="ltr">'+z.fr+'</small></span>';
      a.addEventListener("click",ev=>{ev.preventDefault(); window.open(wa("السلام، أريد طلب توصيل دواء إلى حي "+z.ar+" ("+z.fr+") في طنجة."),"_blank");});
      g.appendChild(a);
    });
  });
  // Hero live order form (R13 / R14)
  const form=document.getElementById("orderForm");
  if(form){
    const out=document.getElementById("waPreview");
    const build=()=>{
      const med=(form.medicine.value||"").trim(), notes=(form.notes.value||"").trim(),
            zone=form.zone.value||"", rx=form.querySelector('input[name="rx"]:checked');
      let lines=["السلام، أريد طلب توصيل دواء في طنجة."];
      if(med) lines.push("الدواء: "+med);
      if(notes) lines.push("ملاحظات: "+notes);
      if(zone) lines.push("الحي: "+zone);
      if(rx) lines.push(rx.value==="yes" ? "عندي وصفة طبية — سأرسل صورتها هنا في واتساب." : "هذا الدواء لا يحتاج وصفة طبية.");
      return wa(lines.join("\n"));
    };
    const refresh=()=>{ if(out) out.setAttribute("href",build()); };
    form.addEventListener("input",refresh); form.addEventListener("change",refresh); refresh();
    form.addEventListener("submit",e=>{e.preventDefault(); window.open(build(),"_blank");});
    if(out) out.addEventListener("click",e=>{e.preventDefault(); window.open(build(),"_blank");});
  }
  // Reveal on scroll
  const io=("IntersectionObserver" in window)? new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add("in"); io.unobserve(en.target);}}),{threshold:.12}):null;
  document.querySelectorAll(".reveal").forEach(el=>{ if(io) io.observe(el); else el.classList.add("in"); });
  const y=document.getElementById("year"); if(y) y.textContent=new Date().getFullYear();
})();
