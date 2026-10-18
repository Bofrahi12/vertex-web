/* VERTEX WEB — admin content overrides (vx-admin panel). Non-blocking; baked-in content stays as fallback. */
(function(){
  "use strict";
  var SRC = window.VX_CONTENT_URL || "https://vertex-admin.onrender.com/content.json";
  var ORIG = {"packs": {"landing": {"name": "صفحة هبوط", "price": 900}, "vitrine": {"name": "موقع تعريفي", "price": 1900}, "store": {"name": "متجر إلكتروني", "price": 4900}, "flagship": {"name": "موقع سينمائي بنظام طلبات", "price": 8000}}, "whatsapp": "212693981822", "faq": {"f1": {"q": "شحال كيدير الوقت باش يوجد الموقع؟", "a": "من 7 حتى 14 يوماً حسب النوع: صفحة الهبوط 7 أيام، الموقع التعريفي 10 أيام، والمتجر الإلكتروني 14 يوماً."}, "f2": {"q": "واش كتخدمو مع مشاريع خارج طنجة؟", "a": "نعم — كنخدمو مع مشاريع في المغرب كامل وعن بعد: التواصل والمتابعة كيكونو عبر واتساب ومكالمات، والتسليم بنفس الطريقة المنظمة."}, "f3": {"q": "واش تقدرو تعاودو تصميم موقع موجود؟", "a": "نعم — خدمة «تحسين موقع موجود» كتشمل إعادة تصميم عصرية كاملة، تحسين السرعة وتجربة الهاتف، وتحسين الظهور في Google."}, "f4": {"q": "واش كتوفرو المحتوى والصور؟", "a": "كنعاونوك في تنظيم المحتوى واختيار الصور المناسبة، وكنوجّهو بالضبط شنو نحتاجو منك (نصوص، صور، أثمنة) باش الموقع يوجد بسرعة وبلا تعطيل."}, "f5": {"q": "واش الموقع بالعربية والفرنسية؟", "a": "بجوج — كنصايبو الموقع باللغة اللي كتناسب زبنائك: العربية، الفرنسية، ولا نسختين مع بعض."}, "f6": {"q": "واش المتجر كيدعم واتساب والدفع الإلكتروني؟", "a": "نعم — الطلب عبر واتساب هو الأساس في متاجرنا حيت هو اللي خدام مزيان في المغرب، وكنربطو حتى وسائل الدفع الإلكتروني المتاحة إضافة للدفع عند الاستلام."}, "f7": {"q": "شكون كيخلص الدومين والاستضافة؟", "a": "الاستضافة الأساسية مشمولة في الثمن. الدومين (اسم النطاق) كيكون على العميل وكيبقى ملكو: حوالي 100–150 درهم في السنة، وكنعاونوك في اختيارو وربطو."}, "f8": {"q": "واش نقدر نسير الموقع بنفسي من بعد الإطلاق؟", "a": "نعم — كتحصل على تكوين على الاستعمال عند التسليم، وزيد 30 يوم دعم مجاني: إصلاحات، تعديلات بسيطة، وأي سؤال عندك."}, "f9": {"q": "كيفاش كنخلص؟", "a": "بكل بساطة: 50% عند بداية العمل و50% بعد التسليم — بلا ما تخلص الباقي حتى تشوف الموقع حي ويعجبك."}, "f10": {"q": "كيفاش كنبداو مشروع؟", "a": "عمر استمارة «طلب عرض ثمن» أو صيفط لينا في واتساب فكرة المشروع — وغادي نجاوبوك في نفس اليوم بأسئلة دقيقة ثم عرض ثمن واضح ومكتوب، بلا التزام."}, "f11": {"q": "واش الدومين والموقع كيبقاو ديالي؟", "a": "إيه، بالكامل. الدومين كيتسجّل باسمك وعلى حسابك (حوالي 100-150 درهم/سنة)، وبعد تسديد ثمن المشروع كاملاً ملفات موقعك ومحتواه كيبقاو ملكاً ليك — تقدر تنقلهم لأي استضافة أخرى في أي وقت."}, "f12": {"q": "ما عنديش النصوص والصور واجدين، شنو نعمل؟", "a": "نقدرو نبداو باللي عندك، وحساب مدة التسليم كيبدا من نهار يكتمل المحتوى. إلا بغيتينا نعتنيو بكتابة المحتوى أو التصوير، هادي خدمات إضافية كنحسبوها باتفاق منفصل قبل ما نبداو."}}};
  function pidOf(u){ try { var x = new URL(u, location.href); var seg = x.pathname.split("/").filter(Boolean); var b = seg.length ? seg[seg.length - 1] : (x.hostname.split(".")[0] || ""); return b.replace(/\.html$/, ""); } catch (e) { return ""; } }
  function fmt(n){ return Number(n).toLocaleString("en-US"); }
  function apply(C){
    if (!C) return;
    (C.packs || []).forEach(function(p){
      var card = document.querySelector('[data-pack="' + p.id + '"]');
      if (!card) return;
      var amt = card.querySelector(".amount");
      if (amt && amt.firstChild) amt.firstChild.nodeValue = fmt(p.price) + " ";
      var o = ORIG.packs[p.id];
      if (o && p.name && p.name !== o.name) { var h3 = card.querySelector("h3"); if (h3) h3.textContent = p.name; }
    });
    var fl = document.querySelector(".fac-end-line");
    if (fl && C.packs && C.packs.length >= 4) {
      var changed = C.packs.some(function(p){ var o = ORIG.packs[p.id]; return o && p.price !== o.price; });
      if (changed) {
        var pr = C.packs.map(function(p){ return fmt(p.price); });
        var cur = fl.textContent;
        if (cur.indexOf("atterrissage") > -1) fl.textContent = "Page d'atterrissage à " + pr[0] + " dirhams · Site vitrine à " + pr[1] + " dirhams · Boutique en ligne à " + pr[2] + " dirhams · Site cinématographique à " + pr[3] + " dirhams";
        else if (cur.indexOf("Landing") > -1) fl.textContent = "Landing page for " + pr[0] + " MAD · Business website for " + pr[1] + " MAD · Online store for " + pr[2] + " MAD · Cinematic website for " + pr[3] + " MAD";
        else fl.textContent = "صفحة هبوط بـ " + pr[0] + " درهم · موقع تعريفي بـ " + pr[1] + " درهم · متجر إلكتروني بـ " + pr[2] + " درهم · موقع سينمائي بـ " + pr[3] + " درهم";
      }
    }
    if (C.whatsapp && C.whatsapp !== ORIG.whatsapp) {
      document.querySelectorAll('a[href*="wa.me/"]').forEach(function(a){ a.href = a.href.replace(/wa\.me\/\d+/, "wa.me/" + C.whatsapp); });
    }
    if (C.faq) {
      var items = {};
      document.querySelectorAll(".faq-item[data-fid]").forEach(function(it){ items[it.getAttribute("data-fid")] = it; });
      var parent = null;
      C.faq.forEach(function(f){
        var it = items[f.id]; if (!it) return;
        parent = parent || it.parentNode;
        var o = ORIG.faq[f.id];
        if (f.hidden) it.style.display = "none";
        else {
          it.style.display = "";
          if (o && f.q !== o.q) { var q = it.querySelector(".faq-q"); if (q && q.firstChild) q.firstChild.nodeValue = f.q + " "; }
          if (o && f.a !== o.a) { var a = it.querySelector(".faq-a p"); if (a) a.textContent = f.a; }
        }
        if (parent) parent.appendChild(it);
      });
    }
    if (C.projects) {
      var order = {}, hidden = {};
      C.projects.forEach(function(p, i){ order[p.pid] = i; hidden[p.pid] = !!p.hidden; });
      var cards = [].slice.call(document.querySelectorAll("a.wcard, article.wcard"));
      var groups = {};
      cards.forEach(function(card){
        var link = card.tagName === "A" ? card : card.querySelector("a[href]");
        if (!link) return;
        var pid = pidOf(link.getAttribute("href") || "");
        if (!(pid in order)) return;
        card.style.display = hidden[pid] ? "none" : "";
        var par = card.parentNode;
        var key = par.id || par.className;
        if (!groups[key]) groups[key] = { par: par, list: [] };
        groups[key].list.push({ card: card, ord: order[pid] });
      });
      Object.keys(groups).forEach(function(k){ var g = groups[k]; g.list.sort(function(a, b){ return a.ord - b.ord; }).forEach(function(x){ g.par.appendChild(x.card); }); });
    }
  }
  var last = null, t = null;
  function load(){
    var ctrl = ("AbortController" in window) ? new AbortController() : null;
    var to = ctrl ? setTimeout(function(){ ctrl.abort(); }, 3500) : null;
    fetch(SRC, { cache: "no-store", signal: ctrl ? ctrl.signal : undefined })
      .then(function(r){ return r.json(); })
      .then(function(C){ if (to) clearTimeout(to); last = C; apply(C); })
      .catch(function(){});
  }
  new MutationObserver(function(){ if (!last) return; clearTimeout(t); t = setTimeout(function(){ apply(last); }, 450); }).observe(document.documentElement, { attributes: true, attributeFilter: ["lang", "dir", "class"] });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", load); else load();
})();
