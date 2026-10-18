/* VERTEX WEB — admin content overrides (vx-admin panel). Non-blocking; baked-in content stays as fallback. */
(function(){
  "use strict";
  var SRC = window.VX_CONTENT_URL || "https://vertex-admin.onrender.com/content.json";
  var ORIG = {"packs": {"landing": {"name": "صفحة هبوط", "price": 900}, "vitrine": {"name": "موقع تعريفي", "price": 1900}, "store": {"name": "متجر إلكتروني", "price": 4900}, "flagship": {"name": "موقع سينمائي بنظام طلبات", "price": 8000}}, "whatsapp": "212693981822", "faq": {"f1": {"q": "شحال كيدير الوقت باش يوجد الموقع؟", "a": "من 7 حتى 14 يوماً حسب النوع: صفحة الهبوط 7 أيام، الموقع التعريفي 10 أيام، والمتجر الإلكتروني 14 يوماً."}, "f2": {"q": "واش كتخدمو مع مشاريع خارج طنجة؟", "a": "نعم — كنخدمو مع مشاريع في المغرب كامل وعن بعد: التواصل والمتابعة كيكونو عبر واتساب ومكالمات، والتسليم بنفس الطريقة المنظمة."}, "f3": {"q": "واش تقدرو تعاودو تصميم موقع موجود؟", "a": "نعم — خدمة «تحسين موقع موجود» كتشمل إعادة تصميم عصرية كاملة، تحسين السرعة وتجربة الهاتف، وتحسين الظهور في Google."}, "f4": {"q": "واش كتوفرو المحتوى والصور؟", "a": "كنعاونوك في تنظيم المحتوى واختيار الصور المناسبة، وكنوجّهو بالضبط شنو نحتاجو منك (نصوص، صور، أثمنة) باش الموقع يوجد بسرعة وبلا تعطيل."}, "f5": {"q": "واش الموقع بالعربية والفرنسية؟", "a": "بجوج — كنصايبو الموقع باللغة اللي كتناسب زبنائك: العربية، الفرنسية، ولا نسختين مع بعض."}, "f6": {"q": "واش المتجر كيدعم واتساب والدفع الإلكتروني؟", "a": "نعم — الطلب عبر واتساب هو الأساس في متاجرنا حيت هو اللي خدام مزيان في المغرب، وكنربطو حتى وسائل الدفع الإلكتروني المتاحة إضافة للدفع عند الاستلام."}, "f7": {"q": "شكون كيخلص الدومين والاستضافة؟", "a": "الاستضافة الأساسية مشمولة في الثمن. الدومين (اسم النطاق) كيكون على العميل وكيبقى ملكو: حوالي 100–150 درهم في السنة، وكنعاونوك في اختيارو وربطو."}, "f8": {"q": "واش نقدر نسير الموقع بنفسي من بعد الإطلاق؟", "a": "نعم — كتحصل على تكوين على الاستعمال عند التسليم، وزيد 30 يوم دعم مجاني: إصلاحات، تعديلات بسيطة، وأي سؤال عندك."}, "f9": {"q": "كيفاش كنخلص؟", "a": "بكل بساطة: 50% عند بداية العمل و50% بعد التسليم — بلا ما تخلص الباقي حتى تشوف الموقع حي ويعجبك."}, "f10": {"q": "كيفاش كنبداو مشروع؟", "a": "عمر استمارة «طلب عرض ثمن» أو صيفط لينا في واتساب فكرة المشروع — وغادي نجاوبوك في نفس اليوم بأسئلة دقيقة ثم عرض ثمن واضح ومكتوب، بلا التزام."}, "f11": {"q": "واش الدومين والموقع كيبقاو ديالي؟", "a": "إيه، بالكامل. الدومين كيتسجّل باسمك وعلى حسابك (حوالي 100-150 درهم/سنة)، وبعد تسديد ثمن المشروع كاملاً ملفات موقعك ومحتواه كيبقاو ملكاً ليك — تقدر تنقلهم لأي استضافة أخرى في أي وقت."}, "f12": {"q": "ما عنديش النصوص والصور واجدين، شنو نعمل؟", "a": "نقدرو نبداو باللي عندك، وحساب مدة التسليم كيبدا من نهار يكتمل المحتوى. إلا بغيتينا نعتنيو بكتابة المحتوى أو التصوير، هادي خدمات إضافية كنحسبوها باتفاق منفصل قبل ما نبداو."}}, "texts": {"workTitle": "أعمال حقيقية، شغالة دابا", "svcTitle": "خدماتنا — اختار وحدة", "priceTitle": "أسعار واضحة، بلا مفاجآت", "procTitle": "طريقة العمل", "numTitle": "أرقام موحّدة، بلا مبالغة", "aboutTitle": "استوديو من طنجة، بمعايير العالم", "avisTitle": "شنو قالوا علينا؟", "faqTitle": "الأسئلة الشائعة", "contactTitle": "طلب عرض ثمن مجاني", "workSub": "مشاريع منشورة ونماذج كاملة — مرّر باش تسافر بيناتهم، والمعرض الكامل فيه 42 عملاً.", "svcSub": "مرّر أو ضغط على أي خدمة باش تشوف التفاصيل والمثال الحي ديالها."}, "projNames": {"demo-immoluxe": "Tanja Luxe — عقار فاخر", "demo-photo": "Atelier Lumière — استوديو تصوير", "demo-burger": "Smash House — برغر وفاست فود", "demo-parfum": "دار العطور — عطور فاخرة", "demo-sport": "Tanger Sport — متجر رياضة", "demo-gym": "نادي القمة — قاعة رياضية", "demo-barber": "LAME D'OR — Barber Club", "demo-marlowe": "MARLOWE — Atelier GT Classique", "demo-sabra": "SABRA — Jus de Figue de Barbarie", "demo-chroma": "CHROMA — Mode Couleur", "demo-solenne": "SOLENNE — Haute Horlogerie", "demo-polaire": "POLAIRE — Lunettes de Ski", "demo-ondine": "ONDINE — Joaillerie", "demo-noctis": "NOCTIS — Bagues Grenat", "demo-torra": "TORRA — Torréfacteur & Café", "demo-doner": "THE DÖNER — Restaurant Expérience", "demo-bacha": "مطعم الباشا — الشيف أيوب بنعمر", "demo-nour": "NOUR COCHES — كراء السيارات بطنجة", "demo-stride": "STRIDE — Boutique Sport 3D", "demo-residence": "AZUR Résidences — Programme Neuf", "demo-cinema": "VERTEX WEB — Cinematic Portfolio", "demo-atlas": "ATLAS ENERGY — Immersive 2026", "demo-resto": "Le Jasmin", "capimmo-tanger": "Cap Immo Tanger", "tradeproacademy": "TradePro Academy", "localboost-ai-site": "LocalBoost AI", "tanger-safe-buy": "Tanger Safe Buy", "chef-patisserie-tanger": "باتيسري سيهام — Chef Pâtisserie Tanger", "demo-mode": "Atlas Mode", "demo-cafe": "مقهى الأصالة", "demo-location": "Tangier Drive", "demo-dentaire": "Clinique Dentaire Sourire", "demo-spa": "واحة الجمال", "demo-patisserie": "حلويات النخبة", "demo-riad": "Riad Jasmin", "demo-fetes": "قاعة الياسمين للأفراح", "mksb-demo": "MKSB Voyage", "bermijou-demo": "Bermijou Shop", "nojom-demo": "Studio Nojom", "safouane-demo": "Centre Safouane — مركز لغات", "studio31-demo": "Studio 31 — Salon de beauté", "iki-demo": "Groupe IKI — Instituts Ibn Khaldoun"}, "projDescs": {"demo-immoluxe": "وكالة عقار فاخر بستايل «Human-Made Luxury»: فيديوهات حقيقية بملء الشاشة وفيلم كيتحكم فيه السكرول.", "demo-photo": "موقع استوديو تصوير احترافي بالفرنسية — معرض أعمال حقيقي وباقات واضحة وحجز فوري.", "demo-burger": "موقع فاست فود بطاقة شبابية ومنيو كامل — الزبون يطلب في دقيقة عبر واتساب.", "demo-parfum": "بوتيك عطور فاخرة بتصميم ذهبي وكريمي أنيق — تجربة شراء راقية بسلة خدامة.", "demo-sport": "متجر معدات رياضية بتصميم طاقي برتقالي — منتجات وتصنيفات وطلب فوري.", "demo-gym": "موقع قاعة رياضية فاخر بتصميم غامق وطاقة عالية — برامج ومدربون وتسجيل فوري.", "demo-barber": "موقع نادي حلاقة رجالية فاخر بطنجة — ثيم غامق وذهبي بتصميم UI UX Pro Max.", "demo-marlowe": "موقع ورشة ترميم سيارات كلاسيكية بفيلم سكرول سينمائي كيتبع السيارة من الغطا حتى الطريق.", "demo-sabra": "موقع عصير الصبار بهيرو كيقرّب ويرجع بالسكرول بحال كيتنفس، ومحتوى كيقنع الزبون يشري.", "demo-chroma": "متجر أزياء بالألوان الجريئة: كاروسيل ثلاثي الأبعاد ولوكبوك كيتحرك مع السكرول.", "demo-solenne": "دار ساعات بفيلم سكرول من 60 إطار كيتبع كل حركة ديال الماكينة.", "demo-polaire": "علامة نظارات تزلج بفيلم سكرول من القمة حتى العدسة.", "demo-ondine": "دار مجوهرات بحركة كاميرا واحدة كتغوص من الماء حتى الخاتم.", "demo-noctis": "دار خواتم غارنيت بهيرو مثبّت كيقرّب اليد حتى كتملا الشاشة.", "demo-torra": "محمصة ومقهى بطنجة: القهوة كتتحرك في كل قسم من الموقع.", "demo-doner": "موقع مطعم دونر كامل بستايل المواصفات التقنية: سبعة أقسام سينمائية بالسكرول من المشواة حتى الطلب — بحال الفيديو تماماً.", "demo-bacha": "موقع لزبون حقيقي: مطعم الباشا ديال الشيف أيوب بنعمر في البرانص 2 بطنجة (+51 ألف متابع على إنستغرام) — صورتو في الواجهة بـ3D، كتالوغ كامل من قائمتو الحقيقية، والطلب كيوصل مباشرة لواتساب المطعم.", "demo-nour": "نموذج موقع لوكالة نور كوتشيس في الجيراري 1 بطنجة (+105 آلاف متابع على إنستغرام): الأسطول الحقيقي ديالهم — من Clio 5 حتى Tucson 2026 — ولّى كيتشاف وكيتحجز من بلاصة وحدة، بلا ما يبقى الزبون يعيّط غير باش يعرف شنو متوفر.", "demo-stride": "متجر رياضي بطنجة كيبيع بالفيديو: المنتجات كتدور وتطفو بثلاثي الأبعاد وسط التيليفون، والطلب كيتمم بواتساب والدفع عند الاستلام.", "demo-residence": "موقع مشروع سكني جديد بفكرة وحدة: فيلم واحد طويل كيتبنى بالسكرول — من الرافعة والورش حتى تسليم المفاتيح.", "demo-cinema": "بورتفوليو ستوديو إبداعي بستايل أفلام 2026: تجربة سينمائية كاملة كتتلعب بالسكرول — سبعة مشاهد من الافتتاح حتى النداء الأخير.", "demo-atlas": "موقع منتج بستايل «Websites in 2026»: فيلم كامل كيتحكم فيه السكرول — بحال المواقع العالمية اللي كتربح الجوائز.", "demo-resto": "موقع مطعم مغربي كامل بالفرنسية — نموذج جاهز لأي مطعم.", "capimmo-tanger": "سوق عقارات متكامل لوكالة بطنجة، يتجدد يومياً بإعلانات متحقق منها.", "tradeproacademy": "منصة دورات تداول كاملة بدومين خاص وقاعدة بيانات حقيقية.", "localboost-ai-site": "موقع تسويقي لخدمة ذكاء اصطناعي مع إضافة ووردبريس مرافقة.", "tanger-safe-buy": "صفحة هبوط لمشروع «عقار المغرب بلا نصب» موجهة للجالية المغربية بالخارج.", "chef-patisserie-tanger": "متجر حلويات كامل لشيف بطنجة: التشيز كيك نجم الواجهة، كتالوج بصور حقيقية، والطلب كيوصل مباشرة لواتساب الشيف.", "demo-mode": "متجر إلكتروني متكامل لعلامة ملابس — نموذج كامل ببيانات وأزرار خدامة.", "demo-cafe": "موقع مقهى مختص متكامل — قائمة كاملة وطلب عبر واتساب.", "demo-location": "موقع وكالة كراء سيارات بالفرنسية — أسطول وحجز بالتواريخ.", "demo-dentaire": "موقع عيادة أسنان بالفرنسية — خدمات وطلب موعد فوري.", "demo-spa": "موقع صالون نسائي وسبا متكامل — خدمات وباقات وحجز.", "demo-patisserie": "موقع محل حلويات متكامل — منتجات وطلب فوري وكعكات أعراس.", "demo-riad": "موقع رياض في المدينة القديمة بالفرنسية — غرف وحجز.", "demo-fetes": "موقع قاعة أفراح فاخرة — باقات وطلب توفر حسب التاريخ.", "mksb-demo": "نموذج صايب ببيانات وكالة أسفار حقيقية بطنجة طلبت عرضاً.", "bermijou-demo": "نموذج متجر ملابس رياضية صايب لزبون بمنتجاته الحقيقية.", "nojom-demo": "نموذج صايب لاستوديو تصوير حقيقي بطنجة طلب يشوف الأمثلة.", "safouane-demo": "نموذج موقع مقترح لمركز لغات وتكوين بطنجة — مسار الألمانية والشهادات والتسجيل عبر واتساب.", "studio31-demo": "نموذج موقع ثلاثي الأبعاد مقترح لصالون ستوديو 31 بسوكو ألتو — الخدمات والمعرض وحجز عبر واتساب وقسم خاص بسمعة Google والتقييمات.", "iki-demo": "نموذج موقع مؤسساتي مقترح لمجموعة معاهد ابن خلدون بطنجة — الدبلومات من التقني حتى الماستر الأوروبي ونموذج توجيه وتسجيل عبر واتساب."}, "homeNames": {"capimmo-tanger": "Cap Immo Tanger", "tradeproacademy": "TradePro Academy", "chef-patisserie-tanger": "باتيسري سيهام", "demo-burger": "Smash House — Expérience 3D", "demo-resto": "Le Jasmin", "demo-mode": "Atlas Mode"}, "homeDescs": {"capimmo-tanger": "سوق عقارات يتجدد يومياً — بحث وفلاتر وتواصل واتساب لكل عقار.", "tradeproacademy": "منصة دورات كاملة — حسابات طلاب، دفع، وشهادات.", "chef-patisserie-tanger": "متجر حلويات كامل — كتالوج بصور حقيقية وطلب بضغطة وحدة في واتساب، مع تجربة 3D وفيلم بالسكرول.", "demo-burger": "واجهة تحريرية سينمائية: شاشات وبطاقات في فضاء ثلاثي الأبعاد.", "demo-resto": "موقع مطعم كامل بتجربة 3D — منيو وحجز طاولة عبر واتساب.", "demo-mode": "متجر ملابس متكامل — سلة شراء وطلب عبر واتساب."}};
  function pidOf(u){ try { var x = new URL(u, location.href); var seg = x.pathname.split("/").filter(Boolean); var b = seg.length ? seg[seg.length - 1] : (x.hostname.split(".")[0] || ""); return b.replace(/\.html$/, ""); } catch (e) { return ""; } }
  function fmt(n){ return Number(n).toLocaleString("en-US"); }
  function setCardText(card, name, desc, origName, origDesc){
    if (name && origName && name !== origName) { var h = card.querySelector("h3"); if (h) h.textContent = name; }
    if (desc && origDesc !== undefined && desc !== origDesc) { var p = card.querySelector(".cin p, p"); if (p) p.textContent = desc; }
  }
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
    if (C.texts) {
      Object.keys(C.texts).forEach(function(k){
        var v = C.texts[k];
        if (!v || v === ORIG.texts[k]) return;
        document.querySelectorAll('[data-i18n="' + k + '"]').forEach(function(elm){ elm.textContent = v; });
      });
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
    if (C.homeProjects) {
      var track = document.getElementById("htrack");
      if (track) {
        var hOrder = {}, hHidden = {}, hByPid = {};
        C.homeProjects.forEach(function(p, i){ hOrder[p.pid] = i; hHidden[p.pid] = !!p.hidden; hByPid[p.pid] = p; });
        var hCards = [].slice.call(track.querySelectorAll("article.wcard"));
        var hList = [];
        hCards.forEach(function(card){
          var link = card.querySelector("a[href]");
          if (!link) return;
          var pid = pidOf(link.getAttribute("href") || "");
          if (!(pid in hOrder)) return;
          var hp = hByPid[pid];
          card.style.display = hHidden[pid] ? "none" : "";
          setCardText(card, hp.name, hp.desc, ORIG.homeNames[pid], ORIG.homeDescs[pid]);
          hList.push({ card: card, ord: hOrder[pid] });
        });
        hList.sort(function(a, b){ return a.ord - b.ord; }).forEach(function(x){ track.appendChild(x.card); });
      }
    }
    if (C.projects) {
      var order = {}, hidden = {}, byPid = {};
      C.projects.forEach(function(p, i){ order[p.pid] = i; hidden[p.pid] = !!p.hidden; byPid[p.pid] = p; });
      var cards = [].slice.call(document.querySelectorAll("a.wcard, article.wcard"));
      var groups = {};
      cards.forEach(function(card){
        if (card.closest && card.closest("#htrack")) return;
        var link = card.tagName === "A" ? card : card.querySelector("a[href]");
        if (!link) return;
        var pid = pidOf(link.getAttribute("href") || "");
        if (!(pid in order)) return;
        var cp = byPid[pid];
        card.style.display = hidden[pid] ? "none" : "";
        setCardText(card, cp.name, cp.desc, ORIG.projNames[pid], ORIG.projDescs[pid]);
        var par = card.parentNode;
        var key = par.id || par.className;
        if (!groups[key]) groups[key] = { par: par, list: [] };
        groups[key].list.push({ card: card, ord: order[pid] });
      });
      Object.keys(groups).forEach(function(k){ var g = groups[k]; g.list.sort(function(a, b){ return a.ord - b.ord; }).forEach(function(x){ g.par.appendChild(x.card); }); });
    }
  }
  function replaceIn(root, map){
    if (!root || !document.createTreeWalker) return;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: function(n){
      var p = n.parentElement;
      if (!p) return NodeFilter.FILTER_REJECT;
      var tag = p.tagName;
      if (tag === "SCRIPT" || tag === "STYLE" || tag === "TEXTAREA" || tag === "NOSCRIPT") return NodeFilter.FILTER_REJECT;
      if (p.closest && p.closest("[data-vx-skip]")) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }});
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function(n){
      var raw = n.nodeValue, trimmed = raw.trim();
      if (trimmed && map[trimmed] !== undefined) n.nodeValue = raw.replace(trimmed, map[trimmed]);
    });
  }
  var demoBusy = false, demoTimer = null, demoArmed = false;
  function applyDemo(C){
    if (!C || !C.demos) return;
    var pid = pidOf(location.pathname);
    var map = C.demos[pid];
    if (!map || !Object.keys(map).length || !document.body) return;
    replaceIn(document.body, map);
    if (!demoArmed) {
      demoArmed = true;
      new MutationObserver(function(){
        if (demoBusy) return;
        clearTimeout(demoTimer);
        demoTimer = setTimeout(function(){ demoBusy = true; replaceIn(document.body, map); setTimeout(function(){ demoBusy = false; }, 60); }, 600);
      }).observe(document.body, { subtree: true, childList: true, characterData: true });
    }
  }
  var last = null, t = null;
  function load(){
    var ctrl = ("AbortController" in window) ? new AbortController() : null;
    var to = ctrl ? setTimeout(function(){ ctrl.abort(); }, 3500) : null;
    fetch(SRC, { cache: "no-store", signal: ctrl ? ctrl.signal : undefined })
      .then(function(r){ return r.json(); })
      .then(function(C){ if (to) clearTimeout(to); last = C; apply(C); applyDemo(C); })
      .catch(function(){});
  }
  new MutationObserver(function(){ if (!last) return; clearTimeout(t); t = setTimeout(function(){ apply(last); applyDemo(last); }, 450); }).observe(document.documentElement, { attributes: true, attributeFilter: ["lang", "dir", "class"] });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", load); else load();
})();
