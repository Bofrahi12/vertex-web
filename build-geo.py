#!/usr/bin/env python3
# VERTEX WEB — GEO layer generator (2026-10-19)
# Answer-first service/sector pages + FAQPage/Service schema, in the Loan Goat style:
# one page per service and per sector, structured data AI engines can quote.
import json, urllib.parse, os

BASE = "https://vertex-web-tanger.onrender.com"
WA = "212693981822"
OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """
:root{--bg:#0a0a0f;--panel:#12121a;--line:#262633;--txt:#f2f0e9;--mut:#a7a5ad;--gold:#c9a24b;--gold2:#e8c97a}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:'Segoe UI',Tahoma,Arial,sans-serif;line-height:1.9}
a{color:var(--gold2)}
.wrap{max-width:880px;margin:0 auto;padding:0 20px 70px}
header{border-bottom:1px solid var(--line);padding:16px 0;margin-bottom:34px}
header .wrap{padding-bottom:0;display:flex;justify-content:space-between;align-items:center}
.logo{font-weight:800;font-size:20px;color:var(--txt);text-decoration:none}.logo span{color:var(--gold)}
.btn{display:inline-block;background:var(--gold);color:#14100a;font-weight:800;padding:12px 26px;border-radius:10px;text-decoration:none}
.btn:hover{background:var(--gold2)}
h1{font-size:32px;line-height:1.5;margin-bottom:14px}
h2{font-size:23px;margin:38px 0 12px;color:var(--gold2)}
p,li{font-size:16.5px;color:#e6e3da}
.mut{color:var(--mut);font-size:14.5px}
.answer{background:var(--panel);border:1px solid var(--gold);border-radius:14px;padding:22px 24px;margin:22px 0}
.answer strong{color:var(--gold2)}
.price{font-size:30px;font-weight:900;color:var(--gold2)}
ul{padding-inline-start:22px}
table{width:100%;border-collapse:collapse;margin:14px 0}
td,th{border:1px solid var(--line);padding:10px 14px;text-align:start;font-size:15.5px}
th{color:var(--gold2);background:var(--panel)}
.faq{border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-bottom:10px;background:var(--panel)}
.faq h3{font-size:17px;margin-bottom:6px}
.cta{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:26px;text-align:center;margin-top:40px}
footer{border-top:1px solid var(--line);margin-top:50px;padding-top:22px}
footer a{margin-inline-end:14px;font-size:14.5px}
.langbox{background:#0e0e14;border:1px dashed var(--line);border-radius:12px;padding:18px 22px;margin-top:26px}
.langbox p{font-size:15px}
"""

def wa_link(text):
    return "https://wa.me/%s?text=%s" % (WA, urllib.parse.quote(text))

def page(slug, title, desc, h1, answer_html, body_html, faqs, service_name, price, wa_text, fr, en):
    faq_schema = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    svc_schema = {"@type": "Service", "name": service_name, "provider": {"@id": BASE + "/#business"},
                  "areaServed": ["طنجة", "المغرب"], "url": BASE + "/" + slug,
                  "offers": {"@type": "Offer", "price": price, "priceCurrency": "MAD",
                             "availability": "https://schema.org/InStock"}}
    crumb = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "فيرتكس ويب", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "الخدمات", "item": BASE + "/services.html"},
        {"@type": "ListItem", "position": 3, "name": service_name, "item": BASE + "/" + slug}]}
    ld = {"@context": "https://schema.org", "@graph": [svc_schema, faq_schema, crumb]}
    faq_html = "\n".join('<div class="faq"><h3>%s</h3><p>%s</p></div>' % (q, a) for q, a in faqs)
    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s/%s">
<meta property="og:type" content="website">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s/%s">
<meta property="og:image" content="%s/og-vertex.jpg">
<script type="application/ld+json">%s</script>
<style>%s</style>
</head>
<body>
<header><div class="wrap"><a class="logo" href="index.html">فيرتكس <span>ويب</span> · VERTEX WEB</a><a href="services.html">جميع الخدمات</a></div></header>
<div class="wrap">
<h1>%s</h1>
<div class="answer">%s</div>
%s
<h2>أسئلة شائعة</h2>
%s
<div class="langbox"><p><strong>En résumé (FR) :</strong> %s</p><p style="margin-top:8px"><strong>In short (EN):</strong> %s</p></div>
<div class="cta"><h2 style="margin-top:0">بغيتي عرض ثمن واضح ومكتوب؟</h2><p>صيفط فكرة مشروعك في واتساب — الجواب في نفس اليوم، بلا التزام.</p><p style="margin-top:14px"><a class="btn" href="%s">اطلب عرض ثمن عبر واتساب</a></p></div>
<footer>
<p class="mut">فيرتكس ويب — تصميم مواقع إلكترونية، طنجة، المغرب · واتساب ‎+212 693-981822‎</p>
<p style="margin-top:10px"><a href="index.html">الرئيسية</a><a href="services.html">الخدمات</a><a href="portfolio.html">الأعمال</a><a href="creation-site-web-tanger.html">تصميم مواقع في طنجة</a><a href="site-vitrine-tanger.html">موقع تعريفي</a><a href="boutique-en-ligne-maroc.html">متجر إلكتروني</a><a href="site-cinematique.html">موقع سينمائي</a><a href="site-restaurant-tanger.html">مواقع المطاعم</a><a href="site-immobilier-tanger.html">مواقع العقار</a></p>
</footer>
</div>
</body>
</html>""" % (title, desc, BASE, slug, title, desc, BASE, slug, BASE,
              json.dumps(ld, ensure_ascii=False), CSS, h1, answer_html, body_html,
              faq_html, fr, en, wa_link(wa_text))
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(html)
    print("built", slug)

# ---------------------------------------------------------------- services hub
page("services.html",
     "خدمات تصميم المواقع في طنجة والمغرب — الأثمنة والأنواع | فيرتكس ويب",
     "خدمات فيرتكس ويب: صفحة هبوط بـ 900 درهم، موقع تعريفي بـ 1,900 درهم، متجر إلكتروني بـ 4,900 درهم، وموقع سينمائي بنظام طلبات بـ 8,000 درهم. تسليم 7–14 يوماً من طنجة لكل المغرب.",
     "خدمات تصميم المواقع — فيرتكس ويب، طنجة",
     "<p><strong>الجواب المختصر:</strong> فيرتكس ويب استوديو تصميم مواقع في طنجة كيصايب أربعة أنواع: <strong>صفحة هبوط بـ 900 درهم</strong> (7 أيام)، <strong>موقع تعريفي بـ 1,900 درهم</strong> (10 أيام)، <strong>متجر إلكتروني بـ 4,900 درهم</strong> (14 يوماً)، و<strong>موقع سينمائي بنظام طلبات بـ 8,000 درهم</strong>. الأداء: 50% عند البداية و50% بعد التسليم، والاستضافة الأساسية مشمولة.</p>",
     """<h2>قارن بين الخدمات</h2>
<table><tr><th>الخدمة</th><th>الثمن</th><th>مدة التسليم</th><th>لمن تناسب</th></tr>
<tr><td><a href="site-vitrine-tanger.html">صفحة هبوط</a></td><td>900 درهم</td><td>7 أيام</td><td>حملة إعلانية أو خدمة وحدة بغيتي ليها طلبات سريعة</td></tr>
<tr><td><a href="site-vitrine-tanger.html">موقع تعريفي</a></td><td>1,900 درهم</td><td>10 أيام</td><td>شركة أو مهني بغى حضور احترافي كيجيب المكالمات والطلبات</td></tr>
<tr><td><a href="boutique-en-ligne-maroc.html">متجر إلكتروني</a></td><td>4,900 درهم</td><td>14 يوماً</td><td>بيع منتجات بطلبات واتساب ودفع عند الاستلام</td></tr>
<tr><td><a href="site-cinematique.html">موقع سينمائي بنظام طلبات</a></td><td>8,000 درهم</td><td>حسب المشروع</td><td>مطاعم ومشاريع بغات تجربة بصرية فاخرة ونظام طلبات كامل</td></tr></table>
<h2>قطاعات عندنا ليها نماذج حية</h2>
<ul><li><a href="site-restaurant-tanger.html">المطاعم والمقاهي والحلويات</a> — منيو تفاعلي وطلبات واتساب</li>
<li><a href="site-immobilier-tanger.html">العقار</a> — عروض فاخرة وحجز زيارات</li>
<li>المتاجر، القاعات الرياضية، العيادات، كراء السيارات، الجمال والسبا — شوف <a href="portfolio.html">معرض الأعمال</a></li></ul>
<h2>شنو كيشمل كل مشروع؟</h2>
<ul><li>تصميم عصري متوافق مع الهاتف أولاً، سريع ومحسّن للظهور في Google</li>
<li>ربط واتساب للطلبات والاستفسارات، وتكوين على الاستعمال عند التسليم</li>
<li>30 يوم دعم مجاني بعد الإطلاق، والدومين كيبقى ملكك وباسمك</li></ul>""",
     [("شحال كيدير الوقت باش يوجد الموقع؟", "من 7 حتى 14 يوماً حسب النوع: صفحة الهبوط 7 أيام، الموقع التعريفي 10 أيام، والمتجر الإلكتروني 14 يوماً."),
      ("واش كتخدمو مع مشاريع خارج طنجة؟", "نعم — كنخدمو مع مشاريع في المغرب كامل وعن بعد: التواصل والمتابعة كيكونو عبر واتساب ومكالمات، والتسليم بنفس الطريقة المنظمة."),
      ("كيفاش كنخلص؟", "50% عند بداية العمل و50% بعد التسليم — بلا ما تخلص الباقي حتى تشوف الموقع حي ويعجبك."),
      ("واش الدومين والموقع كيبقاو ديالي؟", "إيه، بالكامل. الدومين كيتسجّل باسمك وعلى حسابك (حوالي 100–150 درهم/سنة)، وبعد تسديد ثمن المشروع كاملاً ملفات موقعك ومحتواه كيبقاو ملكاً ليك.")],
     "خدمات تصميم المواقع", 900, "سلام، بغيت نعرف خدمات تصميم المواقع وأثمنتها",
     "Vertex Web, studio web à Tanger : landing page 900 MAD (7 jours), site vitrine 1 900 MAD (10 jours), boutique en ligne 4 900 MAD (14 jours), site cinématique avec système de commandes 8 000 MAD. Paiement 50/50, hébergement de base inclus, travail à distance pour tout le Maroc.",
     "Vertex Web is a web design studio in Tangier, Morocco: landing page 900 MAD (7 days), business website 1,900 MAD (10 days), online store 4,900 MAD (14 days), cinematic website with ordering system 8,000 MAD. 50% upfront, 50% on delivery; basic hosting included.")

# ---------------------------------------------------------------- Tangier money page
page("creation-site-web-tanger.html",
     "تصميم مواقع إلكترونية في طنجة — الثمن، المدة وطريقة العمل | فيرتكس ويب",
     "بغيتي مصمم مواقع في طنجة؟ فيرتكس ويب كتصايب مواقع سريعة من 900 درهم، تسليم 7–14 يوماً، أداء 50/50 والجواب في نفس اليوم عبر واتساب +212693981822.",
     "تصميم مواقع إلكترونية في طنجة",
     "<p><strong>الجواب المختصر:</strong> ثمن تصميم موقع في طنجة عند فيرتكس ويب كيبدا من <strong>900 درهم</strong> لصفحة هبوط، <strong>1,900 درهم</strong> لموقع تعريفي، <strong>4,900 درهم</strong> لمتجر إلكتروني، و<strong>8,000 درهم</strong> لموقع سينمائي بنظام طلبات. التسليم من 7 إلى 14 يوماً، والأداء على جوج دفعات: 50% في البداية و50% بعد ما تشوف موقعك حي.</p>",
     """<h2>علاش تختار استوديو من طنجة؟</h2>
<p>حيت كنفهمو السوق المغربي: الزبون المغربي كيطلب عبر واتساب، كيدفع عند الاستلام، وكيتصفح من التيليفون. مواقعنا مبنية على هاد الواقع: زر واتساب واضح، سرعة عالية في الهاتف، ومحتوى بالعربية والفرنسية حسب زبنائك.</p>
<h2>طريقة العمل في 4 خطوات</h2>
<ul><li><strong>1. الاستشارة:</strong> كتصيفط فكرة المشروع في واتساب، وكنجاوبوك في نفس اليوم بأسئلة دقيقة وعرض ثمن مكتوب بلا التزام.</li>
<li><strong>2. التصميم:</strong> كنبنّيو الشكل والمحتوى على مقاس مشروعك — ماشي قالب جاهز.</li>
<li><strong>3. المراجعة:</strong> كتشوف النسخة الحية وكتطلب تعديلاتك قبل الإطلاق.</li>
<li><strong>4. الإطلاق والدعم:</strong> الموقع كيطلع حي، مع تكوين على الاستعمال و30 يوم دعم مجاني.</li></ul>
<h2>أمثلة حية من طنجة</h2>
<ul><li><a href="https://chef-patisserie-tanger.onrender.com/">باتيسري سيهام</a> — مشروع حقيقي لشيف حلويات في طنجة بطلبات واتساب</li>
<li><a href="demo-qasr.html">مطعم القصر</a> — نموذج موقع سينمائي بنظام طلبات كامل</li>
<li><a href="portfolio.html">42 مشروعاً ونموذجاً حياً</a> في قطاعات مختلفة</li></ul>""",
     [("شحال ثمن تصميم موقع إلكتروني في طنجة؟", "كيبدا من 900 درهم لصفحة هبوط، 1,900 درهم لموقع تعريفي، 4,900 درهم لمتجر إلكتروني، و8,000 درهم لموقع سينمائي بنظام طلبات — الثمن كيتأكد بعرض مكتوب حسب مشروعك."),
      ("شحال كيدير الوقت باش يوجد الموقع؟", "من 7 حتى 14 يوماً حسب النوع: صفحة الهبوط 7 أيام، الموقع التعريفي 10 أيام، والمتجر الإلكتروني 14 يوماً."),
      ("واش خاصني نكون في طنجة باش نخدم معاكم؟", "لا — كنخدمو مع مشاريع في المغرب كامل وعن بعد عبر واتساب ومكالمات، بنفس التنظيم والتسليم في الموعد."),
      ("واش الموقع غادي يبان في Google؟", "الموقع كيتبنى سريعاً ومهيكلاً تقنياً للظهور في Google (عناوين، وصف، بيانات مهيكلة وسرعة)، وكنعاونوك في ربطو بأدوات Google عند الإطلاق."),
      ("كيفاش كنبداو مشروع؟", "صيفط فكرة المشروع في واتساب أو عمر استمارة طلب عرض الثمن في الموقع الرئيسي — غادي نجاوبوك في نفس اليوم.")],
     "تصميم مواقع إلكترونية في طنجة", 900, "سلام، بغيت موقع لمشروعي في طنجة — بغيت عرض ثمن",
     "Création de site web à Tanger par Vertex Web : à partir de 900 MAD (landing), 1 900 MAD (vitrine), 4 900 MAD (e-commerce), 8 000 MAD (site cinématique). Livraison 7 à 14 jours, commande WhatsApp intégrée, paiement 50/50.",
     "Web design in Tangier by Vertex Web: from 900 MAD for a landing page, 1,900 MAD for a business site, 4,900 MAD for an online store, 8,000 MAD for a cinematic site with ordering. Delivery in 7-14 days, WhatsApp ordering built in, 50/50 payment.")

# ---------------------------------------------------------------- vitrine / landing
page("site-vitrine-tanger.html",
     "موقع تعريفي وصفحة هبوط في طنجة — 1,900 و900 درهم | فيرتكس ويب",
     "موقع تعريفي احترافي بـ 1,900 درهم في 10 أيام، وصفحة هبوط بـ 900 درهم في 7 أيام — تصميم سريع للهاتف، واتساب مدمج، من فيرتكس ويب طنجة.",
     "موقع تعريفي (1,900 درهم) وصفحة هبوط (900 درهم)",
     "<p><strong>الجواب المختصر:</strong> <strong>صفحة الهبوط بـ 900 درهم</strong> صفحة وحدة مركزة على هدف واحد (طلبات أو تسجيلات) وكتوجد في 7 أيام. <strong>الموقع التعريفي بـ 1,900 درهم</strong> موقع كامل متعدد الصفحات (الرئيسية، الخدمات، الأعمال، التواصل) كيوجد في 10 أيام. بجوج مهيئين للهاتف وفيهم ربط واتساب.</p>",
     """<h2>الفرق بيناتهم</h2>
<table><tr><th></th><th>صفحة هبوط — 900 درهم</th><th>موقع تعريفي — 1,900 درهم</th></tr>
<tr><td>الصفحات</td><td>صفحة واحدة طويلة</td><td>عدة صفحات + مدونة خفيفة</td></tr>
<tr><td>تناسب</td><td>حملة إعلانية، خدمة واحدة، إطلاق منتج</td><td>شركة، عيادة، مكتب، مهني حر</td></tr>
<tr><td>الهدف</td><td>تحويل الزائر لطلب واحد واضح</td><td>بناء ثقة وحضور دائم في Google</td></tr></table>
<h2>شنو كيشمل الموقع التعريفي؟</h2>
<ul><li>تصميم خاص بمشروعك (ماشي قالب)، بالعربية و/أو الفرنسية</li>
<li>صفحات: الرئيسية، من نحن، الخدمات، الأعمال أو الأسعار، والتواصل</li>
<li>أزرار واتساب ومكالمات، خريطة Google، ونموذج تواصل</li>
<li>تهيئة تقنية للظهور في Google + سرعة عالية في الهاتف</li>
<li>تكوين عند التسليم + 30 يوم دعم مجاني</li></ul>
<p class="mut">الاستضافة الأساسية مشمولة؛ الدومين باسمك بحوالي 100–150 درهم/سنة.</p>""",
     [("واش 900 درهم صفحة هبوط كافية لمشروعي؟", "إلا كان عندك هدف واحد — مثلاً طلبات لخدمة وحدة أو حملة إعلانية — إيه. إلا بغيتي تقدم شركتك وخدمات متعددة وتبان في Google على المدى الطويل، الموقع التعريفي بـ 1,900 درهم هو الاختيار الصح."),
      ("واش تقدرو تعاودو تصميم موقع موجود؟", "نعم — خدمة تحسين موقع موجود كتشمل إعادة تصميم عصرية كاملة، تحسين السرعة وتجربة الهاتف، وتحسين الظهور في Google."),
      ("واش كتوفرو المحتوى والصور؟", "كنعاونوك في تنظيم المحتوى واختيار الصور المناسبة، وكنوجّهو بالضبط شنو نحتاجو منك (نصوص، صور، أثمنة) باش الموقع يوجد بسرعة وبلا تعطيل."),
      ("شكون كيخلص الدومين والاستضافة؟", "الاستضافة الأساسية مشمولة في الثمن. الدومين كيكون على العميل وكيبقى ملكو: حوالي 100–150 درهم في السنة، وكنعاونوك في اختيارو وربطو.")],
     "موقع تعريفي وصفحة هبوط", 900, "سلام، بغيت موقع تعريفي / صفحة هبوط لمشروعي",
     "Site vitrine à Tanger : 1 900 MAD en 10 jours ; landing page : 900 MAD en 7 jours. Design sur mesure, mobile-first, WhatsApp intégré, hébergement de base inclus — Vertex Web.",
     "Business website in Tangier: 1,900 MAD in 10 days; landing page: 900 MAD in 7 days. Custom mobile-first design, WhatsApp integration, basic hosting included — Vertex Web.")

# ---------------------------------------------------------------- e-commerce
page("boutique-en-ligne-maroc.html",
     "متجر إلكتروني في المغرب بطلبات واتساب — 4,900 درهم | فيرتكس ويب",
     "متجر إلكتروني كامل بـ 4,900 درهم في 14 يوماً: كتالوج منتجات، طلب عبر واتساب، دفع عند الاستلام ودفع إلكتروني — من فيرتكس ويب، طنجة.",
     "متجر إلكتروني في المغرب — 4,900 درهم",
     "<p><strong>الجواب المختصر:</strong> المتجر الإلكتروني عند فيرتكس ويب بـ <strong>4,900 درهم</strong> وكيوجد في <strong>14 يوماً</strong>. كيشمل كتالوج منتجات كامل، سلة وطلبات عبر <strong>واتساب</strong> (اللي خدام مزيان في المغرب)، الدفع عند الاستلام وربط وسائل الدفع الإلكتروني المتاحة.</p>",
     """<h2>علاش الطلب عبر واتساب؟</h2>
<p>حيت الزبون المغربي كيثق في واتساب وكيكمل الطلب فيه أسرع من أي نموذج طويل. المتجر كيعرض المنتجات بشكل احترافي، والزبون كيختار وكيصيفط طلبو مرتباً وجاهزاً لواتساب ديالك — بلا عمولات منصات وبلا ما يضيع بين الخطوات.</p>
<h2>شنو كيشمل المتجر؟</h2>
<ul><li>كتالوج منتجات بتصنيفات وبحث وصور عالية الجودة</li>
<li>سلة شراء + طلب واتساب منظم (المنتجات، الكميات، المجموع)</li>
<li>الدفع عند الاستلام + ربط الدفع الإلكتروني المتاح في المغرب</li>
<li>صفحات منتجات مهيئة لـ Google، وسرعة عالية في الهاتف</li>
<li>تكوين على إضافة وتعديل المنتجات بنفسك + 30 يوم دعم مجاني</li></ul>""",
     [("واش المتجر كيدعم واتساب والدفع الإلكتروني؟", "نعم — الطلب عبر واتساب هو الأساس في متاجرنا حيت هو اللي خدام مزيان في المغرب، وكنربطو حتى وسائل الدفع الإلكتروني المتاحة إضافة للدفع عند الاستلام."),
      ("شحال كيدير الوقت باش يوجد المتجر؟", "14 يوماً من نهار يكتمل المحتوى (المنتجات والصور والأثمنة)."),
      ("واش نقدر نسير المتجر بنفسي من بعد؟", "نعم — كتحصل على تكوين على الاستعمال عند التسليم، وزيد 30 يوم دعم مجاني: إصلاحات، تعديلات بسيطة، وأي سؤال عندك."),
      ("واش كاينة عمولة على المبيعات؟", "لا — المتجر ديالك بالكامل، بلا عمولات على الطلبات. كتخلص غير ثمن الإنشاء مرة واحدة: 50% في البداية و50% بعد التسليم.")],
     "متجر إلكتروني", 4900, "سلام، بغيت متجر إلكتروني لمنتجاتي",
     "Boutique en ligne au Maroc par Vertex Web : 4 900 MAD, prête en 14 jours, catalogue complet, commandes via WhatsApp, paiement à la livraison et paiement en ligne, sans commission sur les ventes.",
     "Online store in Morocco by Vertex Web: 4,900 MAD, ready in 14 days, full product catalogue, WhatsApp ordering, cash on delivery and online payment, zero sales commission.")

# ---------------------------------------------------------------- cinematic flagship
page("site-cinematique.html",
     "موقع سينمائي بنظام طلبات — الباقة الرائدة 8,000 درهم | فيرتكس ويب",
     "موقع سينمائي بفيلم كيتحكم فيه السكرول ونظام طلبات كامل بـ 8,000 درهم — تجربة بصرية فاخرة للمطاعم والمشاريع الراقية، من فيرتكس ويب طنجة.",
     "موقع سينمائي بنظام طلبات — 8,000 درهم",
     "<p><strong>الجواب المختصر:</strong> الموقع السينمائي هو الباقة الرائدة عند فيرتكس ويب بـ <strong>8,000 درهم</strong>: موقع كيتحرك بحال فيلم — مشاهد مثبتة كتتقدم مع السكرول (scroll-film) — مع <strong>نظام طلبات كامل</strong> (منيو/كتالوج تفاعلي، سلة، وطلبات كتوصل لواتساب ديالك). مناسب للمطاعم والمشاريع اللي بغات تتميز بصرياً على المنافسين.</p>",
     """<h2>شنو كيميز الموقع السينمائي؟</h2>
<ul><li><strong>فيلم سكرول:</strong> الزائر كيتحكم في الفيلم بالسكرول — المشاهد كتتقدم وكترجع معاه، بتقنية إطارات canvas عالية الجودة (حتى 1920px)</li>
<li><strong>نظام طلبات حقيقي:</strong> اختيار الأصناف والكميات والإضافات، توصيل أو استلام، والمجموع كيتحسب تلقائياً قبل ما يوصل الطلب لواتساب</li>
<li><strong>ثلاث لغات:</strong> العربية والفرنسية والإنجليزية في نفس الموقع</li>
<li><strong>أداء الهاتف أولاً:</strong> التجربة كاملة خدامة في التيليفون، حيت أغلب الزبناء منو كيجيو</li></ul>
<h2>شوفو حي</h2>
<ul><li><a href="demo-qasr.html">مطعم القصر — AL QASR</a>: نموذج كامل بهاد النظام (منيو قابل للطلب، سلة، وطلبات واتساب)</li>
<li><a href="demo-villa-horizon.html">فيلا الأفق</a>: نموذج عقاري بفيلمين سكرول سينمائيين</li></ul>
<p class="mut">«مطعم القصر» و«فيلا الأفق» نماذج عرض (démo) كتورّي النظام والجودة؛ الأثمنة والمدة النهائية كتتأكد بعرض مكتوب حسب مشروعك.</p>""",
     [("شحال ثمن الموقع السينمائي؟", "8,000 درهم للباقة الرائدة بنظام الطلبات. الأداء: 50% عند بداية العمل و50% بعد التسليم."),
      ("واش نظام الطلبات كيوصل لواتساب ديالي؟", "نعم — الطلب كيتجمع في الموقع (الأصناف، الكميات، الإضافات، طريقة الاستلام والعنوان) وكيتصيفط مرتباً لواتساب ديالك أو واتساب مشروعك."),
      ("واش هاد الستايل مناسب لأي مشروع؟", "كيصلح بزاف للمطاعم، الحلويات، العقار الفاخر وأي مشروع كيبيع بالتجربة البصرية. للمشاريع البسيطة، الموقع التعريفي بـ 1,900 درهم غالباً كافي."),
      ("واش الموقع بالعربية والفرنسية؟", "بجوج — وكنزيدو حتى الإنجليزية في الباقة السينمائية: العربية، الفرنسية والإنجليزية في موقع واحد.")],
     "موقع سينمائي بنظام طلبات", 8000, "سلام، بغيت موقع سينمائي بنظام طلبات لمشروعي",
     "Site cinématique avec système de commandes — pack flagship Vertex Web à 8 000 MAD : film contrôlé par le scroll, menu interactif, panier et commandes WhatsApp, en arabe, français et anglais.",
     "Cinematic website with ordering system — Vertex Web flagship at 8,000 MAD: scroll-controlled film scenes, interactive menu, cart and WhatsApp orders, in Arabic, French and English.")

# ---------------------------------------------------------------- restaurant sector
page("site-restaurant-tanger.html",
     "تصميم مواقع المطاعم في طنجة — منيو وطلبات واتساب | فيرتكس ويب",
     "موقع مطعم في طنجة بمنيو تفاعلي وطلبات كتوصل لواتساب: من 1,900 درهم للموقع التعريفي حتى 8,000 درهم للموقع السينمائي بنظام طلبات كامل — فيرتكس ويب.",
     "مواقع المطاعم في طنجة — منيو وطلبات واتساب",
     "<p><strong>الجواب المختصر:</strong> موقع المطعم عند فيرتكس ويب كيبدا من <strong>1,900 درهم</strong> (موقع تعريفي بمنيو وزر طلب واتساب) وكيوصل لـ <strong>8,000 درهم</strong> للموقع السينمائي بنظام طلبات كامل: الزبون كيختار الأطباق والكميات والإضافات، وطلبو كيوصلك مرتباً في واتساب — <strong>بلا عمولات تطبيقات التوصيل</strong>.</p>",
     """<h2>شنو خاص موقع المطعم يدير؟</h2>
<ul><li><strong>منيو كيتباع:</strong> صور كبيرة، أثمنة واضحة، وتصنيفات سريعة (مقبلات، أطباق، حلويات...)</li>
<li><strong>طلب في دقيقة:</strong> سلة + توصيل/استلام + العنوان، والمجموع محسوب قبل الإرسال</li>
<li><strong>بلا وسطاء:</strong> الطلبات كتوصلك نتا مباشرة في واتساب — ماشي عبر تطبيق كياخد نسبة من كل طلب</li>
<li><strong>Google والخرائط:</strong> ربط الموقع بملف Google Business باش يلقاوك في «مطعم قريب مني»</li></ul>
<h2>أمثلة حية</h2>
<ul><li><a href="demo-qasr.html">مطعم القصر — AL QASR</a> (نموذج): موقع سينمائي بمنيو كامل قابل للطلب ونظام سلة</li>
<li><a href="https://chef-patisserie-tanger.onrender.com/">باتيسري سيهام</a> (مشروع حقيقي، طنجة): كتالوج حلويات بطلبات واتساب بلا نماذج معقدة</li></ul>""",
     [("شحال ثمن موقع مطعم؟", "من 1,900 درهم لموقع تعريفي بمنيو وطلب واتساب، حتى 8,000 درهم لموقع سينمائي بنظام طلبات كامل (سلة، إضافات، توصيل/استلام)."),
      ("واش الزبون يقدر يطلب من الموقع مباشرة؟", "نعم — في نظام الطلبات الكامل كيختار الأطباق والكميات والإضافات، وكيتصيفط الطلب مرتباً لواتساب المطعم. الدفع كيبقى عند الاستلام أو بالتحويل حسب اختيارك."),
      ("واش كتحسبو عمولة على الطلبات؟", "لا — الموقع ديالك والطلبات ديالك، بلا أي نسبة على كل طلب، عكس تطبيقات التوصيل."),
      ("عندي غير صور التيليفون للأطباق، واش كافية؟", "كنبداو باللي عندك وكنوجّهو شنو ناقص بالضبط. الصور الجيدة كتفرق بزاف في المبيعات، وخدمة التصوير ممكنة باتفاق منفصل.")],
     "تصميم مواقع المطاعم", 1900, "سلام، عندي مطعم وبغيت موقع بمنيو وطلبات واتساب",
     "Site web pour restaurants à Tanger par Vertex Web : dès 1 900 MAD (vitrine avec menu et commande WhatsApp) jusqu'à 8 000 MAD (site cinématique avec système de commandes complet), sans commission sur les commandes.",
     "Restaurant websites in Tangier by Vertex Web: from 1,900 MAD (site with menu and WhatsApp ordering) to 8,000 MAD (cinematic site with full ordering system), with zero commission on orders.")

# ---------------------------------------------------------------- real estate sector
page("site-immobilier-tanger.html",
     "تصميم مواقع العقار في طنجة — عروض فاخرة وحجز زيارات | فيرتكس ويب",
     "موقع وكالة عقارية في طنجة بعروض مصورة، أفلام سكرول سينمائية وحجز زيارات عبر واتساب — من 1,900 درهم، والموقع السينمائي بـ 8,000 درهم. فيرتكس ويب.",
     "مواقع العقار في طنجة — عروض كتبيع وحجز زيارات",
     "<p><strong>الجواب المختصر:</strong> موقع العقار عند فيرتكس ويب كيبدا من <strong>1,900 درهم</strong> (موقع تعريفي بقوائم عقارات وطلبات واتساب) وكيوصل لـ <strong>8,000 درهم</strong> للموقع السينمائي: عرض عقار واحد أو وكالة كاملة بأفلام سكرول، صور كبيرة، وزر <strong>حجز زيارة</strong> كيوصل لواتساب ديالك مباشرة.</p>",
     """<h2>شنو كيفرق موقع عقار كيبيع؟</h2>
<ul><li><strong>العقار هو البطل:</strong> صور وأفلام بملء الشاشة، والثمن والمواصفات واضحين من أول ثانية</li>
<li><strong>جولة سينمائية:</strong> فيلم سكرول كيمشي بالزائر داخل العقار (مدخل، صالون، مسبح...) بحال زيارة حقيقية</li>
<li><strong>حجز زيارة في واتساب:</strong> الزائر كيختار العقار وكيصيفط طلب زيارة مرتب — بلا مكالمات ضائعة</li>
<li><strong>ثقة:</strong> صفحات أحياء، أسئلة شائعة، وربط Google Maps وملف Google Business</li></ul>
<h2>أمثلة حية</h2>
<ul><li><a href="demo-villa-horizon.html">فيلا الأفق</a> (نموذج): صفحة عقار واحدة بفيلمين سكرول وحجز زيارة واتساب</li>
<li><a href="demo-immoluxe.html">Tanja Luxe</a> (نموذج): وكالة عقار فاخر بأفلام حقيقية بملء الشاشة</li>
<li><a href="portfolio.html">نماذج عقارية أخرى</a> في معرض الأعمال</li></ul>
<p class="mut">النماذج معلمة كناذج عرض؛ موقعك كيتبنى بعقاراتك وصورك الحقيقية.</p>""",
     [("شحال ثمن موقع وكالة عقارية؟", "من 1,900 درهم لموقع تعريفي بقوائم وطلبات واتساب، حتى 8,000 درهم لموقع سينمائي بأفلام سكرول ونظام حجز زيارات."),
      ("واش نقدر نزيد ونبدل العقارات بنفسي؟", "نعم — كتحصل على تكوين عند التسليم على إضافة وتعديل العقارات، وزيد 30 يوم دعم مجاني."),
      ("عندي غير عقار واحد للبيع، واش كاينة صفحة خاصة؟", "نعم — صفحة عقار واحدة سينمائية (بحال نموذج فيلا الأفق) كتركز على عقار واحد وكتحول الزوار لطلبات زيارة في واتساب."),
      ("واش الموقع كيبان في Google إلا بحث شي حد على شقق في طنجة؟", "الموقع كيتبنى مهيكلاً تقنياً (عناوين، وصف، بيانات مهيكلة وسرعة) مع صفحات أحياء وأسئلة شائعة — هادا هو الأساس اللي كيبني الظهور مع الوقت والمحتوى.")],
     "تصميم مواقع العقار", 1900, "سلام، عندي وكالة/عقار في طنجة وبغيت موقع",
     "Sites immobiliers à Tanger par Vertex Web : dès 1 900 MAD (site d'agence avec annonces et WhatsApp) jusqu'à 8 000 MAD (site cinématique avec films scroll et réservation de visites via WhatsApp).",
     "Real estate websites in Tangier by Vertex Web: from 1,900 MAD (agency site with listings and WhatsApp) to 8,000 MAD (cinematic site with scroll films and WhatsApp visit booking).")

print("done")
