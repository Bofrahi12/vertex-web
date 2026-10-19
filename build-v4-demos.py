#!/usr/bin/env python3
# Build 4 personalized VERTEX WEB v4 prospect demos from sector templates.
# Templates are NEVER modified: we read them, transform in memory, write new files.
import re, urllib.parse, pathlib, sys

BASE = pathlib.Path.home() / "workspace/mounir-web"
OLD = "212693981822"

def enc(s):
    return urllib.parse.quote(s, safe='')

class Rep:
    def __init__(self, s):
        self.s = s
        self.fails = []
    def sub(self, old, new, cnt=None):
        n = self.s.count(old)
        if cnt is not None and n != cnt:
            self.fails.append(f"count {n} != {cnt} for: {old[:70]!r}")
        elif n == 0:
            self.fails.append(f"NOT FOUND: {old[:70]!r}")
        self.s = self.s.replace(old, new)
        return self
    def regex(self, pat, new, cnt=None):
        self.s, n = re.subn(pat, new, self.s, flags=re.S)
        if cnt is not None and n != cnt:
            self.fails.append(f"regex count {n} != {cnt} for: {pat[:70]}")
        elif n == 0:
            self.fails.append(f"regex NOT FOUND: {pat[:70]}")
        return self
    def wa_text_links(self, number, messages):
        pat = re.compile(r'href="https://wa\.me/' + OLD + r'\?text=[^"]*"')
        idx = [0]
        def f(m):
            msg = messages[idx[0]]; idx[0] += 1
            return f'href="https://wa.me/{number}?text={enc(msg)}"'
        self.s, n = pat.subn(f, self.s)
        if n != len(messages):
            self.fails.append(f"wa text links {n} != {len(messages)}")
        return self
    def done(self, label):
        if self.fails:
            print(f"== FAILURES in {label}:")
            for f in self.fails:
                print("  -", f)
            sys.exit(1)
        return self.s

def svc_row(name, desc, service, verb):
    return (f'<div class="svc-row"><div class="svc-txt"><h4>{name}</h4><p>{desc}</p></div>'
            f'<button class="book-mini" onclick="wa(\'{service}\')">{verb}</button></div>')

def svc_cat(emoji_title, rows):
    body = "\n      ".join(rows)
    return f'<div class="svc-cat rv">\n      <h3>{emoji_title}</h3>\n      {body}\n    </div>'

# =====================================================================
# SPA TEMPLATE -> Jouhaina & Baan Thai
# =====================================================================
def build_spa(cfg):
    s = (BASE / "demo-spa.html").read_text(encoding="utf-8")
    r = Rep(s)
    B = cfg["brand"]            # brand as used in Arabic messages
    NUM = cfg["number"]

    # --- title / meta / json-ld ---
    r.sub("واحة الجمال — صالون وسبا نسائي بطنجة · تجربة افتتاحية 3D", cfg["title"], cnt=2)
    r.sub("نموذج تجريبي لصالون وسبا نسائي بطنجة: تصفيف شعر، عناية بالبشرة، حمّام مغربي، مساج وأظافر — الحجز عبر واتساب.",
          cfg["meta"], cnt=1)
    # --- demobar -> required banner ---
    r.sub('<div class="demobar">📌 نموذج تجريبي — الصور والأثمنة توضيحية</div>',
          f'<div class="demobar">📌 نموذج أولي صُمّم خصيصاً لـ {cfg["banner_name"]} · من VERTEX WEB</div>', cnt=1)
    # --- wa text links (order: header, ov5, cta, waf) ---
    r.wa_text_links(NUM, [
        f"السلام، بغيت نحجز موعد في {B}",
        f"السلام {B}، بغيت نحجز موعد. شكراً!",
        f"السلام، بغيت نستفسر على خدمات {B}",
        f"السلام، بغيت نستفسر على خدمات {B}",
    ])
    # --- header logo + nav ---
    r.sub('<div class="logo">واحة <b>الجمال</b></div>', f'<div class="logo">{cfg["logo"]}</div>', cnt=1)
    r.sub('<a href="#packs">03 · الباقات</a>', '<a href="#gallery">03 · المعرض</a>', cnt=1)
    r.sub('href="https://wa.me/' + OLD + '"', 'href="https://wa.me/' + NUM + '"')  # placeholder guard (none expected)
    # --- hero overlays ---
    r.sub('<img src="demo-spa/img/wide3d.webp" alt="واحة الجمال">',
          f'<img src="demo-spa/img/wide3d.webp" alt="{B}">', cnt=1)
    r.sub(cfg["ov1_h1_old"], cfg["ov1_h1"], cnt=1)
    r.sub(cfg["ov1_p_old"], cfg["ov1_p"], cnt=1)
    r.sub('<span class="micro">EST. 2026 — TANGER</span><span class="micro">HAMMAM ROYAL · 250 DH</span><span class="micro">FEMMES UNIQUEMENT</span>',
          cfg["ov1_meta"], cnt=1)
    r.sub("الحمّام الملكي — صابون بلدي، غاسول الأعشاب وزيت الأركان: طقوس مغربية أصيلة على ضوء الشموع.",
          cfg["ov3_p"], cnt=1)
    r.sub("بطاقات كتطفو في العمق — الحمّام الملكي، العناية بالبشرة وتصفيف الشعر. البطاقة اللي في الوسط هي نجمتنا.",
          cfg["ov4_p"], cnt=1)
    r.sub("شفتي الواحة… دابا عيشيها.", cfg["ov5_h2"], cnt=1)
    r.sub(cfg["ov5_p_old"], cfg["ov5_p"], cnt=1)
    r.sub("احجزي باقة الاسترخاء — 650 درهم", cfg["ov5_btn"], cnt=1)
    r.sub('<a href="#packs">الباقات</a>', '<a href="#gallery">المعرض</a>', cnt=1)
    r.sub("OASIS DE BEAUTÉ © 2026 · VERTEX WEB — WEBGL / GSAP / LENIS", cfg["techfoot"], cnt=1)
    # --- marquee ---
    old_marquee = ('<span>حمّام مغربي <i>//</i> مساج <i>//</i> عناية بالبشرة <i>//</i> تصفيف شعر <i>//</i> أظافر <i>//</i> ماكياج عروسة <i>//</i></span>')
    r.sub(old_marquee, cfg["marquee"], cnt=2)
    # --- feature stats ---
    for old, new in cfg["stats"]:
        r.sub(old, new, cnt=1)
    # --- services section ---
    r.sub('<h2 class="sec-title rv">خدماتنا وأثمنتها</h2>', '<h2 class="sec-title rv">خدماتنا</h2>', cnt=1)
    r.sub("أثمنة واضحة بلا مفاجآت — اختاري خدمتك واحجزي موعدك مباشرة عبر واتساب.",
          cfg["svc_sub"], cnt=1)
    r.regex(r'<div class="svc-grid">.*?\n  </div>\n</div></section>',
            '<div class="svc-grid">\n\n    ' + cfg["services_html"] + '\n\n  </div>\n</div></section>', cnt=1)
    # --- remove PACKAGES section entirely ---
    r.regex(r'<!-- PACKAGES -->.*?</section>\n', '', cnt=1)
    # --- gallery ---
    r.sub("✦ جولة في الواحة ✦", "✦ جولة عندنا ✦", cnt=1)
    r.sub("أجواء مصمّمة لراحتك من أول خطوة داخل الصالون.", "أجواء مصمّمة لراحتك واسترخائك.", cnt=1)
    for old, new in cfg["gallery"]:
        r.sub(old, new, cnt=1)
    # --- booking form options ---
    r.sub("""        <option>تصفيف الشعر</option>
        <option>العناية بالوجه</option>
        <option>الحمّام المغربي</option>
        <option>المساج</option>
        <option>الأظافر</option>
        <option>ماكياج المناسبات</option>
        <option>باقة العروسة</option>
        <option>باقة الاسترخاء</option>
        <option>باقة الجمال السريع</option>
        <option>خدمة أخرى</option>""", cfg["form_options"], cnt=1)
    r.sub("""          <option>10:00</option><option>11:00</option><option>12:00</option>
          <option>14:00</option><option>15:00</option><option>16:00</option>
          <option>17:00</option><option>18:00</option>""", cfg["time_options"], cnt=1)
    # --- infos stats ---
    for old, new in cfg["infos"]:
        r.sub(old, new, cnt=1)
    r.sub("+212 693-981822", cfg["phone_display"], cnt=1)
    # --- CTA ---
    r.sub(cfg["cta_h2_old"], cfg["cta_h2"], cnt=1)
    r.sub("احجزي موعدك في دقيقة — طلبك يوصلنا مباشرة على واتساب.", cfg["cta_p"], cnt=1)
    r.sub("💬 احجزي عبر واتساب", cfg["cta_btn"], cnt=1)
    # --- footer ---
    r.sub("© 2026 واحة الجمال — نموذج تجريبي للعرض فقط — الصور والأثمنة توضيحية ولا تمثل صالوناً حقيقياً.<br>موقع تجريبي من إنجاز فيرتكس ويب — تصميم مواقع.",
          f"© 2026 {B} — نموذج أولي للعرض — الصور توضيحية.<br>نموذج من إنجاز فيرتكس ويب — تصميم مواقع.", cnt=1)
    # --- JS strings ---
    r.sub("واحة الجمال — الحجز عبر واتساب (من النسخة الأصلية)", f"{B} — الحجز عبر واتساب", cnt=1)
    r.sub(f"'السلام واحة الجمال، بغيت نحجز: '", f"'السلام {B}، بغيت نحجز: '", cnt=1)
    r.sub("'السلام واحة الجمال، بغيت نحجز موعد:\\n'", f"'السلام {B}، بغيت نحجز موعد:\\n'", cnt=1)
    # --- 3D layer labels / screen url ---
    r.sub("url:'oasis-beaute.ma'", f"url:'{cfg['screen_url']}'", cnt=1)
    r.sub("label:'HAMMAM ROYAL — 250 DH'", f"label:'{cfg['lbl1']}'", cnt=1)
    r.sub("label:'SOIN HYDRATANT — 300 DH'", f"label:'{cfg['lbl2']}'", cnt=1)
    r.sub("label:'COIFFURE — 150 DH'", f"label:'{cfg['lbl3']}'", cnt=1)
    r.sub("label:'L\\'OASIS — ESPACE DÉTENTE'", f"label:'{cfg['lbl4']}'", cnt=1)
    # --- global number swap (plain links + JS const) ---
    r.sub(OLD, NUM)
    out = r.done(cfg["outfile"])
    (BASE / cfg["outfile"]).write_text(out, encoding="utf-8")
    print("WROTE", cfg["outfile"], len(out.encode()), "bytes")

# ---------------- Jouhaina ----------------
JOU = dict(
    outfile="demo-v4-jouhaina.html", brand="Maison Jouhaina", banner_name="Maison Jouhaina",
    number="212668382028", phone_display="+212 668-382028",
    title="Maison Jouhaina — حمّام وسبا 100% نساء في طنجة · تجربة افتتاحية 3D",
    meta="Maison Jouhaina — حمّام تقليدي وسبا جمال مخصّص للنساء فقط في طنجة: حمّام مغربي، مساج، عناية بالوجه وليساج بروتين — مفتوح 7/7، الحجز عبر واتساب.",
    logo="Maison <b>Jouhaina</b>",
    ov1_h1_old="واحتكِ الخاصة<br><span class=\"stroke\">للجمال</span> والاسترخاء.",
    ov1_h1="حمّامكِ الخاص<br><span class=\"stroke\">100% نساء</span> في طنجة.",
    ov1_p_old="صالون وسبا نسائي في قلب طنجة — تصفيف شعر، عناية بالبشرة، حمّام مغربي أصيل ومساج مهدّئ، في فضاء أنيق ومريح وخاص بالنساء فقط.",
    ov1_p="Maison Jouhaina — حمّام تقليدي وسبا جمال مخصّص للنساء فقط، في شارع العشاق بطنجة: حمّام مغربي، مساج، عناية بالوجه وليساج بروتين، في فضاء أنيق ومريح.",
    ov1_meta='<span class="micro">RUE EL OUCHAK — TANGER</span><span class="micro">FEMMES UNIQUEMENT</span><span class="micro">7J/7 · 10:00 — 22:00</span>',
    ov3_p="الحمّام التقليدي — صابون بلدي وتقشير بالقفاز التقليدي: طقوس مغربية أصيلة، في فضاء نسائي هادئ وعلى ضوء الشموع.",
    ov4_p="بطاقات كتطفو في العمق — الحمّام، المساج والعناية بالوجه. البطاقة اللي في الوسط هي نجمتنا.",
    ov5_h2="شفتي الأجواء… دابا عيشيها.",
    ov5_p_old="باقة الاسترخاء: حمّام مغربي تقليدي + مساج استرخائي 60 دقيقة + عناية مرطّبة للوجه — نهار دلال كامل بـ650 درهم.",
    ov5_p="حمّام تقليدي، مساج «30°» ولا عناية بالوجه — احجزي جلستك عندنا. مفتوحين كل أيام الأسبوع من 10:00 حتى 22:00.",
    ov5_btn="احجزي موعدك عبر واتساب",
    techfoot="MAISON JOUHAINA © 2026 · VERTEX WEB — WEBGL / GSAP / LENIS",
    marquee='<span>حمّام مغربي <i>//</i> مساج «30°» <i>//</i> عناية بالوجه <i>//</i> قناع البخار <i>//</i> ليساج بروتين <i>//</i> فضاء 100% نساء <i>//</i></span>',
    stats=[
        ('<div class="stat rv d1"><div class="fic">💇‍♀️</div><h3>خبيرات تجميل</h3><p>فريق نسائي محترف</p></div>',
         '<div class="stat rv d1"><div class="fic">💇‍♀️</div><h3>فريق نسائي</h3><p>خبيرات في الحمّام والعناية</p></div>'),
        ('<div class="stat rv d2"><div class="fic">🌿</div><h3>منتجات طبيعية</h3><p>زيوت وأقنعة من مكونات مغربية</p></div>',
         '<div class="stat rv d2"><div class="fic">🌿</div><h3>طقوس مغربية</h3><p>صابون بلدي وعناية تقليدية</p></div>'),
    ],
    svc_sub="اختاري خدمتك واحجزي موعدك مباشرة عبر واتساب.",
    services_html="\n\n    ".join([
        svc_cat("🧖‍♀️ الحمّام المغربي", [
            svc_row("حمّام تقليدي للنساء", "صابون بلدي وتقشير بالقفاز التقليدي، في فضاء 100% نسائي.", "الحمّام المغربي — حمّام تقليدي", "احجزي"),
            svc_row("حمّام + قناع البخار", "طقوس الحمّام مع عناية Steam Mask للوجه.", "الحمّام المغربي — حمّام + قناع البخار", "احجزي"),
        ]),
        svc_cat("💆‍♀️ المساج", [
            svc_row("مساج «30°»", "المساج المميّز ديال الدار، للاسترخاء العميق.", "المساج — مساج 30°", "احجزي"),
        ]),
        svc_cat("✨ العناية والجمال", [
            svc_row("عناية بالوجه", "تنظيف وترطيب لبشرة نضرة ومشرقة.", "العناية والجمال — عناية بالوجه", "احجزي"),
            svc_row("ليساج بروتين", "تمليس وعناية بالبروتين لشعر ناعم ولامع.", "العناية والجمال — ليساج بروتين", "احجزي"),
        ]),
    ]),
    gallery=[
        ('<article class="card rv"><img src="demo-spa/img/g3.webp" alt="ركن تصفيف الشعر" loading="lazy"><div class="cin"><h3>💇‍♀️ ركن تصفيف الشعر</h3><p>مرايا ذهبية وكراسٍ وردية في فضاء مضيء وهادئ.</p></div></article>',
         '<article class="card rv"><img src="demo-spa/img/g3.webp" alt="ليساج بروتين" loading="lazy"><div class="cin"><h3>💇‍♀️ ليساج بروتين</h3><p>شعر ناعم ولامع بعناية البروتين.</p></div></article>'),
        ('<article class="card rv d1"><img src="demo-spa/img/g1.webp" alt="الحمّام المغربي" loading="lazy"><div class="cin"><h3>🧖‍♀️ الحمّام المغربي</h3><p>زليج تقليدي وبخار مهدّئ وطقوس أصيلة.</p></div></article>',
         '<article class="card rv d1"><img src="demo-spa/img/g1.webp" alt="الحمّام المغربي" loading="lazy"><div class="cin"><h3>🧖‍♀️ الحمّام المغربي</h3><p>طقوس تقليدية: صابون بلدي وتقشير بالقفاز.</p></div></article>'),
        ('<article class="card rv d2"><img src="demo-spa/img/g2.webp" alt="العناية بالبشرة" loading="lazy"><div class="cin"><h3>✨ غرفة العناية بالبشرة</h3><p>أجواء دافئة وشموع لعناية عميقة ومريحة.</p></div></article>',
         '<article class="card rv d2"><img src="demo-spa/img/g2.webp" alt="العناية بالبشرة" loading="lazy"><div class="cin"><h3>✨ العناية بالوجه</h3><p>عناية وقناع البخار في أجواء دافئة ومريحة.</p></div></article>'),
    ],
    form_options="""        <option>الحمّام المغربي</option>
        <option>المساج — مساج 30°</option>
        <option>عناية بالوجه</option>
        <option>قناع البخار</option>
        <option>ليساج بروتين</option>
        <option>خدمة أخرى</option>""",
    time_options="""          <option>10:00</option><option>11:00</option><option>12:00</option>
          <option>13:00</option><option>14:00</option><option>15:00</option>
          <option>16:00</option><option>17:00</option><option>18:00</option>
          <option>19:00</option><option>20:00</option><option>21:00</option>""",
    infos=[
        ("<p>الاثنين – السبت: 9:30 → 19:30<br>الأحد: 10:00 → 14:00</p>", "<p>كل أيام الأسبوع<br>10:00 → 22:00</p>"),
        ("<p>شارع محمد الخامس<br>وسط المدينة، 90000 طنجة</p>", "<p>Rue El Ouchak<br>طنجة</p>"),
    ],
    cta_h2_old="جاهزة لنهار دلال؟", cta_h2="جاهزة لنهار دلال؟",
    cta_p="احجزي موعدك في دقيقة — طلبك يوصلنا مباشرة على واتساب.",
    cta_btn="💬 احجزي عبر واتساب",
    screen_url="instagram.com/maisonjouhaina",
    lbl1="HAMMAM TRADITIONNEL", lbl2="SOIN DU VISAGE", lbl3="LISSAGE PROTÉINE", lbl4="MAISON JOUHAINA",
)

# ---------------- Baan Thai ----------------
BAAN = dict(
    outfile="demo-v4-baanthai.html", brand="Baan Thaï", banner_name="Baan Thaï Institut Tanger",
    number="212670708315", phone_display="+212 670-708315",
    title="Baan Thaï Institut — مساج تايلاندي وحمّام مغربي في طنجة · تجربة افتتاحية 3D",
    meta="Baan Thaï Institut Tanger — مساج تايلاندي تقليدي وحمّام مغربي في طنجة، بمعالجات مدرّبات في مدارس تايلاندية — مفتوح 7/7 من 11:00 حتى 23:00، الحجز عبر واتساب.",
    logo="Baan <b>Thaï</b>",
    ov1_h1_old="واحتكِ الخاصة<br><span class=\"stroke\">للجمال</span> والاسترخاء.",
    ov1_h1="مساج تايلاندي<br><span class=\"stroke\">وحمّام مغربي</span> في طنجة.",
    ov1_p_old="صالون وسبا نسائي في قلب طنجة — تصفيف شعر، عناية بالبشرة، حمّام مغربي أصيل ومساج مهدّئ، في فضاء أنيق ومريح وخاص بالنساء فقط.",
    ov1_p="Baan Thaï Institut — معهد مساج تايلاندي تقليدي وحمّام مغربي في قلب طنجة، بمعالجات مدرّبات في مدارس تايلاندية. مفتوح كل أيام الأسبوع من 11:00 حتى 23:00.",
    ov1_meta='<span class="micro">RÉSIDENCE FLAMANT ROSE — TANGER</span><span class="micro">MASSAGE THAÏ · HAMMAM</span><span class="micro">7J/7 · 11:00 — 23:00</span>',
    ov3_p="المساج التايلاندي التقليدي — تقنيات عريقة على أيدي معالجات خبيرات، لاسترخاء عميق من أول جلسة.",
    ov4_p="بطاقات كتطفو في العمق — المساج التايلاندي والحمّام المغربي. البطاقة اللي في الوسط هي نجمتنا.",
    ov5_h2="شفتي الأجواء… دابا جرّبها.",
    ov5_p_old="باقة الاسترخاء: حمّام مغربي تقليدي + مساج استرخائي 60 دقيقة + عناية مرطّبة للوجه — نهار دلال كامل بـ650 درهم.",
    ov5_p="مساج تايلاندي تقليدي ولا حمّام مغربي — احجز جلستك عندنا. مفتوحين كل أيام الأسبوع من 11:00 حتى 23:00.",
    ov5_btn="احجز موعدك عبر واتساب",
    techfoot="BAAN THAÏ © 2026 · VERTEX WEB — WEBGL / GSAP / LENIS",
    marquee='<span>مساج تايلاندي <i>//</i> حمّام مغربي <i>//</i> استرخاء <i>//</i> عناية <i>//</i> رفاهية <i>//</i></span>',
    stats=[
        ('<div class="stat rv"><div class="fic">🔒</div><h3>خصوصية تامة</h3><p>فضاء مخصّص للنساء فقط</p></div>',
         '<div class="stat rv"><div class="fic">🌺</div><h3>مساج تايلاندي أصيل</h3><p>معالجات مدرّبات في مدارس تايلاندية</p></div>'),
        ('<div class="stat rv d1"><div class="fic">💇‍♀️</div><h3>خبيرات تجميل</h3><p>فريق نسائي محترف</p></div>',
         '<div class="stat rv d1"><div class="fic">🧖‍♀️</div><h3>حمّام مغربي</h3><p>طقوس تقليدية أصيلة</p></div>'),
        ('<div class="stat rv d2"><div class="fic">🌿</div><h3>منتجات طبيعية</h3><p>زيوت وأقنعة من مكونات مغربية</p></div>',
         '<div class="stat rv d2"><div class="fic">🕚</div><h3>أوقات واسعة</h3><p>7/7 · 11:00 ← 23:00</p></div>'),
    ],
    svc_sub="اختر خدمتك واحجز موعدك مباشرة عبر واتساب.",
    services_html="\n\n    ".join([
        svc_cat("💆‍♀️ المساج التايلاندي", [
            svc_row("مساج تايلاندي تقليدي", "تقنيات تايلاندية عريقة على أيدي معالجات مدرّبات في مدارس تايلاندية.", "المساج التايلاندي — مساج تقليدي", "احجز"),
        ]),
        svc_cat("🧖‍♀️ الحمّام المغربي", [
            svc_row("حمّام مغربي تقليدي", "صابون بلدي وتقشير بالقفاز التقليدي.", "الحمّام المغربي — حمّام تقليدي", "احجز"),
        ]),
    ]),
    gallery=[
        ('<article class="card rv"><img src="demo-spa/img/g3.webp" alt="ركن تصفيف الشعر" loading="lazy"><div class="cin"><h3>💇‍♀️ ركن تصفيف الشعر</h3><p>مرايا ذهبية وكراسٍ وردية في فضاء مضيء وهادئ.</p></div></article>',
         '<article class="card rv"><img src="demo-spa/img/g3.webp" alt="المساج التايلاندي" loading="lazy"><div class="cin"><h3>🌺 ركن المساج التايلاندي</h3><p>تقنيات تايلاندية عريقة لاسترخاء كامل.</p></div></article>'),
        ('<article class="card rv d1"><img src="demo-spa/img/g1.webp" alt="الحمّام المغربي" loading="lazy"><div class="cin"><h3>🧖‍♀️ الحمّام المغربي</h3><p>زليج تقليدي وبخار مهدّئ وطقوس أصيلة.</p></div></article>',
         '<article class="card rv d1"><img src="demo-spa/img/g1.webp" alt="الحمّام المغربي" loading="lazy"><div class="cin"><h3>🧖‍♀️ الحمّام المغربي</h3><p>طقوس تقليدية: صابون بلدي وتقشير بالقفاز.</p></div></article>'),
        ('<article class="card rv d2"><img src="demo-spa/img/g2.webp" alt="العناية بالبشرة" loading="lazy"><div class="cin"><h3>✨ غرفة العناية بالبشرة</h3><p>أجواء دافئة وشموع لعناية عميقة ومريحة.</p></div></article>',
         '<article class="card rv d2"><img src="demo-spa/img/g2.webp" alt="أجواء الهدوء" loading="lazy"><div class="cin"><h3>✨ أجواء الهدوء</h3><p>فضاء هادئ مصمّم لراحتك واسترخائك.</p></div></article>'),
    ],
    form_options="""        <option>المساج التايلاندي</option>
        <option>الحمّام المغربي</option>
        <option>خدمة أخرى</option>""",
    time_options="""          <option>11:00</option><option>12:00</option><option>13:00</option>
          <option>14:00</option><option>15:00</option><option>16:00</option>
          <option>17:00</option><option>18:00</option><option>19:00</option>
          <option>20:00</option><option>21:00</option><option>22:00</option>""",
    infos=[
        ("<p>الاثنين – السبت: 9:30 → 19:30<br>الأحد: 10:00 → 14:00</p>", "<p>كل أيام الأسبوع<br>11:00 → 23:00</p>"),
        ("<p>شارع محمد الخامس<br>وسط المدينة، 90000 طنجة</p>", "<p>Résidence Flamant Rose<br>Angle Rue Omar Ibn Abdelaziz / Rue Ibn Aajeroume<br>طنجة</p>"),
    ],
    cta_h2_old="جاهزة لنهار دلال؟", cta_h2="محتاج لحظة هدوء؟",
    cta_p="احجز موعدك في دقيقة — طلبك يوصلنا مباشرة على واتساب.",
    cta_btn="💬 احجز عبر واتساب",
    screen_url="instagram.com/baanthai.tanger",
    lbl1="HAMMAM MAROCAIN", lbl2="MASSAGE THAÏ", lbl3="DÉTENTE & BIEN-ÊTRE", lbl4="BAAN THAÏ — TANGER",
)

build_spa(JOU)
build_spa(BAAN)
print("SPA demos done")


# =====================================================================
# CAFE TEMPLATE -> Frutello
# =====================================================================
def build_frutello():
    s = (BASE / "demo-cafe.html").read_text(encoding="utf-8")
    r = Rep(s)
    NUM = "212700196943"
    B = "Frutello"
    r.sub("مقهى الأصالة — قهوة مختصة وبرانش في طنجة · تجربة 3D (نموذج تجريبي)",
          "Frutello — مقهى وباتيسري وجلاصيي في تطوان · تجربة 3D (نموذج أولي)", cnt=2)
    r.sub("نموذج تجريبي لموقع مقهى مختصة في طنجة: قهوة مختصة، برانش، عصائر طازجة وحلويات — الطلب والحجز عبر واتساب.",
          "Frutello — مقهى، باتيسري وجلاصيي بفرعين في تطوان: بسطيلة، تشوروس بالشوكولاتة، جيلاتو الدار وقائمة كاملة — الطلب عبر واتساب.", cnt=1)
    r.sub('<div class="demobar">📌 نموذج تجريبي — الصور والأثمنة توضيحية</div>',
          '<div class="demobar">📌 نموذج أولي صُمّم خصيصاً لـ Frutello · من VERTEX WEB</div>', cnt=1)
    r.wa_text_links(NUM, [
        "السلام Frutello، بغيت نستفسر وبغيت نطلب.",
        "السلام Frutello، بغيت نطلب.",
        "السلام Frutello، بغيت نستفسر وبغيت نطلب.",
        "السلام Frutello، عندي استفسار.",
    ])
    r.sub('<div class="logo">مقهى <b>الأصالة</b></div>', '<div class="logo">Fru<b>tello</b></div>', cnt=1)
    r.sub('<div id="fallback3d"><img src="demo-cafe/img/hero.webp" alt="مقهى الأصالة"></div>',
          '<div id="fallback3d"><img src="demo-cafe/img/hero.webp" alt="Frutello"></div>', cnt=1)
    # hero
    r.sub("// Scene 01 — Café Al Assala", "// Scene 01 — Frutello · Tétouan", cnt=1)
    r.sub('قهوة تتصنع بحب…<br><span class="stroke">على الطريقة الأصيلة</span>',
          'حلاوة تطوان…<br><span class="stroke">على طريقة فروتيلو</span>', cnt=1)
    r.sub("مقهى الأصالة — طنجة: حبوب مختصة محمّصة بعناية، برانش مغربي كامل، وترّاس كيطل على أزقة المدينة القديمة. مرّر… وسافر بين الأجواء.",
          "Frutello — تطوان: مقهى، باتيسري وجلاصيي بفرعين (عين ملول والولاية). من البسطيلة والتشوروس بالشوكولاتة الذائبة حتى الجيلاتو المصنوع في الدار. مرّر… وسافر بين الأجواء.", cnt=1)
    r.sub('<span class="micro">TANGER — CENTRE-VILLE</span><span class="micro">BRUNCH COMPLET · 55 DH</span><span class="micro">OUVERT · 7:30 — 23:00</span>',
          '<span class="micro">TÉTOUAN — AIN MELLOUL · WILAYA</span><span class="micro">BASTELLA · CHURROS · GELATO</span><span class="micro">08:00 — 23:00</span>', cnt=1)
    r.sub("الفضاء بالزليج، الترّاس على المدينة القديمة، وكاس القهوة — طبقات كتتحرك بسرعات مختلفة، بحال جلسة حقيقية عندنا.",
          "الفضاء، ركن الحلويات وكاس القهوة — طبقات كتتحرك بسرعات مختلفة، بحال جلسة حقيقية عندنا.", cnt=1)
    r.sub("الترّاس ديالنا كيطل على أزقة طنجة القديمة — الشمس، النعناع، ورائحة القهوة الطازجة.",
          "الجيلاتو ديالنا كيتصنع في الدار، والتشوروس كتدوب في الشوكولاتة — توقيعات فروتيلو كتستناك في الفرعين.", cnt=1)
    r.sub("بطاقات كتطفو في العمق — برانش كامل، لاتيه آرت وحبوب مختصة. البطاقة اللي في الوسط هي توقيع الدار.",
          "بطاقات كتطفو في العمق — البسطيلة، التشوروس والجيلاتو ديال الدار. البطاقة اللي في الوسط هي توقيع الدار.", cnt=1)
    r.sub("شفتي الأجواء… مرحبا بيك على الطاولة.", "شفتي الأجواء… مرحبا بيك عندنا.", cnt=1)
    r.sub("فطور الأصالة الكامل: مسمن ساخن، أملو، جبن بلدي، بيض بلدي وعصير برتقال طازج — بـ55 درهم فقط. احجز طاولتك ولا اطلب للتوصيل.",
          "اطلب من فرع عين ملول ولا فرع الولاية عبر واتساب — ولا لقانا في Glovo بالقائمة الكاملة.", cnt=1)
    r.sub("اطلب فطور الأصالة — 55 درهم", "اطلب عبر واتساب", cnt=1)
    r.sub("CAFÉ AL ASSALA © 2026 · VERTEX WEB — WEBGL / GSAP / LENIS",
          "FRUTELLO © 2026 · VERTEX WEB — WEBGL / GSAP / LENIS", cnt=1)
    # marquee
    mq = '<span>قهوة مختصة <i>//</i> أتاي بالنعناع <i>//</i> برانش مغربي <i>//</i> لاتيه آرت <i>//</i> حلويات الدار <i>//</i> ترّاس مشمس <i>//</i></span>'
    r.sub(mq, '<span>بسطيلة <i>//</i> تشوروس بالشوكولاتة <i>//</i> جيلاتو الدار <i>//</i> سموذي وشيكس <i>//</i> طواجن وبيتزا <i>//</i> باتيسري <i>//</i></span>', cnt=2)
    # trust grid
    r.sub('<div class="trust-item"><span class="t-icon">🌱</span><span>حبوب مختصة<small>تحميص خفيف ومتوسط</small></span></div>',
          '<div class="trust-item"><span class="t-icon">🍦</span><span>جيلاتو الدار<small>جلاص مصنوع عندنا</small></span></div>', cnt=1)
    r.sub('<div class="trust-item"><span class="t-icon">🥐</span><span>مخبوزات صباحية<small>كرواسون ومسمن ساخن</small></span></div>',
          '<div class="trust-item"><span class="t-icon">⭐</span><span>توقيعات الدار<small>بسطيلة وتشوروس بالشوكولاتة</small></span></div>', cnt=1)
    r.sub('<div class="trust-item"><span class="t-icon">📶</span><span>واي فاي وخدمة هادئة<small>بلاصة مناسبة للخدمة والقراية</small></span></div>',
          '<div class="trust-item"><span class="t-icon">📍</span><span>فرعان في تطوان<small>عين ملول · الولاية</small></span></div>', cnt=1)
    r.sub('<div class="trust-item"><span class="t-icon">🚚</span><span>توصيل داخل طنجة<small>للطلبات عبر واتساب</small></span></div>',
          '<div class="trust-item"><span class="t-icon">🛵</span><span>القائمة عبر Glovo<small>ولا اطلب واتساب للاستلام</small></span></div>', cnt=1)
    # about
    r.sub('<div class="about-img"><img src="demo-cafe/img/g2.webp" alt="بارستا كيوجد لاتيه آرت في مقهى الأصالة"></div>',
          '<div class="about-img"><img src="demo-cafe/img/g2.webp" alt="تحضيرات طازجة في فروتيلو"></div>', cnt=1)
    r.sub("<h2>مقهى صغير بروح كبيرة، في قلب طنجة</h2>", "<h2>فروتيلو — مقهى وباتيسري وجلاصيي، بفرعين في تطوان</h2>", cnt=1)
    r.sub("في «الأصالة» كنآمنو أن القهوة الزوينة كتبدا من الحبة: كنختارو حبوب مختصة من مصادر معروفة، كنطحنوها في البلاصة، وكنوجدو كل كاس بعناية — من الإسبريسو المضبوط حتى الكابتشينو برغوة حريرية ولاتيه آرت متقن.",
          "فروتيلو هو مقهى وباتيسري وجلاصيي في تطوان، معروف بتوقيعاتو: البسطيلة، التشوروس بالشوكولاتة الذائبة، والجيلاتو اللي كيتصنع عندنا في الدار — بلا ما ننساو السموذي والشيكس بالفواكه الطازجة.", cnt=1)
    r.sub("وبالموازاة مع القهوة، كنقدمو برانش مغربي كامل: مسمن ساخن، أملو، جبن بلدي، زيتون وعصير برتقال طازج — فطور كيشبه لدارنا، في أجواء دافئة بزليج وخشب منحوت.",
          "والقائمة أوسع من الحلويات: طواجن، بيتزا وتاباس — القائمة الكاملة متوفرة في الفرعين وعبر Glovo، والطلب يقدر يتم أيضاً عبر واتساب.", cnt=1)
    r.sub("<div>☕ قهوة مختصة<span>إسبريسو، فلتر وطرق تحضير بطيئة</span></div>",
          "<div>📍 فرع عين ملول<span>08:00 ← 21:00</span></div>", cnt=1)
    r.sub("<div>🥞 برانش كامل<span>مغربي وعصري، حتى 14:00</span></div>",
          "<div>📍 فرع الولاية<span>08:00 ← 23:00</span></div>", cnt=1)
    r.sub("<div>🍰 حلويات الدار<span>تشيز كيك وتيراميسو وحلويات اليوم</span></div>",
          "<div>🍦 جيلاتو الدار<span>جلاص مصنوع عندنا</span></div>", cnt=1)
    r.sub("<div>🌿 ترّاس مشمس<span>إطلالة على أزقة المدينة القديمة</span></div>",
          "<div>🛵 عبر Glovo<span>القائمة كاملة في التطبيق</span></div>", cnt=1)
    # menu headers + sub
    r.sub("أثمنة توضيحية في هذا النموذج — القائمة الحقيقية كتتبدل حسب الموسم وتوفر المنتجات الطازجة.",
          "مختارات من قائمة فروتيلو — القائمة الكاملة متوفرة في الفرعين وعبر Glovo.", cnt=1)
    r.sub("<h3>☕ قهوة مختصة</h3>", "<h3>⭐ توقيعات فروتيلو</h3>", cnt=1)
    r.sub("<h3>🧃 عصائر ومشروبات</h3>", "<h3>🍽️ من القائمة</h3>", cnt=1)
    r.sub("<h3>🥞 فطور وبرانش</h3>", "<h3>🧁 باتيسري وحلويات</h3>", cnt=1)
    r.sub("<h3>🍰 حلويات</h3>", "<h3>☕ قهوة ومشروبات</h3>", cnt=1)
    # menu items: rewrite
    def item(name, desc):
        return f'<div class="item"><div class="item-txt"><h4>{name}</h4><p>{desc}</p></div></div>'
    r.sub('<div class="item"><div class="item-txt"><h4>إسبريسو</h4><p>جرعة مركزة من حبوب مختصة محمصة متوسطة.</p></div><div class="item-price">14 <small>درهم</small></div></div>',
          item("بسطيلة فروتيلو", "من توقيعات الدار اللي كيتمدح بيها زبناؤنا."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>أمريكانو</h4><p>إسبريسو ممدد بماء ساخن، نكهة نظيفة ومتوازنة.</p></div><div class="item-price">16 <small>درهم</small></div></div>',
          item("تشوروس بالشوكولاتة الذائبة", "تشوروس ساخنة كتتقدم مع شوكولاتة ذائبة."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>كابتشينو</h4><p>رغوة حليب حريرية مع رشة كاكاو خفيفة.</p></div><div class="item-price">20 <small>درهم</small></div></div>',
          item("جيلاتو الدار", "جلاص مصنوع عندنا في الدار."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>لاتيه آرت</h4><p>حليب مبخّر بعناية ورسم يدوي على الوجه.</p></div><div class="item-price">22 <small>درهم</small></div></div>',
          item("سموذي وشيكس", "فواكه طازجة مخلوطة في البلاصة."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>عصير برتقال طازج</h4><p>برتقال الموسم معصور في البلاصة، بلا سكر مضاف.</p></div><div class="item-price">22 <small>درهم</small></div></div>',
          item("طواجن", "من قائمتنا الكاملة — أطباق مغربية."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>سموذي أفوكادو ولوز</h4><p>أفوكادو، حليب لوز، عسل حر ولمسة فانيليا.</p></div><div class="item-price">30 <small>درهم</small></div></div>',
          item("بيتزا", "من الفرن — من قائمتنا الكاملة."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>عصير رمان</h4><p>رمان طازج معصور يدوياً، غني ومنعش.</p></div><div class="item-price">26 <small>درهم</small></div></div>',
          item("تاباس", "مختارات خفيفة للمشاركة."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>فطور الأصالة الكامل</h4><p>مسمن، أملو، جبن بلدي، زيتون، بيض بلدي، عصير برتقال وقهوة أو أتاي.</p></div><div class="item-price">55 <small>درهم</small></div></div>',
          item("حلويات الدار", "تشكيلة الحلويات — كتتبدل حسب اليوم."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>توست أفوكادو وبيض</h4><p>خبز محمص، أفوكادو مهروس وبيض مسلوق بالتوابل الخفيفة.</p></div><div class="item-price">45 <small>درهم</small></div></div>',
          item("ديسيرات", "من قائمتنا الكاملة ديال الحلويات والديسيرات."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>تشيز كيك الفواكه الحمراء</h4><p>قاعدة بسكويت بالزبدة وكريمة خفيفة وفواكه الموسم.</p></div><div class="item-price">28 <small>درهم</small></div></div>',
          item("قهوة ومشروبات ساخنة", "من الإسبريسو حتى الكابتشينو."), cnt=1)
    r.sub('<div class="item"><div class="item-txt"><h4>تيراميسو</h4><p>الوصفة الإيطالية الأصلية بقهوة الأصالة.</p></div><div class="item-price">30 <small>درهم</small></div></div>',
          item("عصائر طازجة", "عصائر وسموذي فواكه الموسم."), cnt=1)
    # menu items: delete the rest
    for old in [
        '<div class="item"><div class="item-txt"><h4>فلات وايت</h4><p>جرعة مزدوجة مع طبقة رقيقة من الحليب المخملي.</p></div><div class="item-price">22 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>موكا بالشوكولاتة البلجيكية</h4><p>إسبريسو، شوكولاتة ذائبة وحليب مبخّر.</p></div><div class="item-price">24 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>آيس لاتيه</h4><p>إسبريسو بارد مع حليب طازج ومكعبات ثلج.</p></div><div class="item-price">24 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>أتاي بالنعناع</h4><p>شاي أخضر ونعناع طازج، كيتصب على الطريقة المغربية.</p></div><div class="item-price">16 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>أومليت الأعشاب والجبن</h4><p>بيض بلدي، أعشاب طازجة وجبن ذائب، مع خبز الدار.</p></div><div class="item-price">35 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>بانكيك بالعسل واللوز</h4><p>بانكيك هش مع عسل حر ورقائق لوز محمصة.</p></div><div class="item-price">32 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>براونيز الشوكولاتة</h4><p>قطعة غنية بالشوكولاتة الداكنة والجوز.</p></div><div class="item-price">25 <small>درهم</small></div></div>\n',
        '<div class="item"><div class="item-txt"><h4>كرواسون بالزبدة</h4><p>كيتحضر كل صباح، هش وذهبي.</p></div><div class="item-price">12 <small>درهم</small></div></div>\n',
    ]:
        r.sub(old, "", cnt=1)
    r.sub("البرانش كيتقدم حتى 14:00 · جميع المشروبات متوفرة ساخنة أو باردة · سولنا على حلوى اليوم في واتساب.",
          "عين ملول: 08:00 ← 21:00 · الولاية: 08:00 ← 23:00 · القائمة الكاملة متوفرة أيضاً عبر Glovo.", cnt=1)
    # gallery
    r.sub('<h2 class="sec-title">أجواء الأصالة بالصور</h2>', '<h2 class="sec-title">أجواء فروتيلو بالصور</h2>', cnt=1)
    r.sub("من رائحة القهوة الصباحية حتى غروب الشمس على الترّاس.", "أجواء دافئة، من الصباح حتى الليل — في الفرعين.", cnt=1)
    r.sub('<figure><img src="demo-cafe/img/hero.webp" alt="فضاء مقهى الأصالة بالزليج المغربي"><figcaption>الفضاء الداخلي بالزليج المغربي</figcaption></figure>',
          '<figure><img src="demo-cafe/img/hero.webp" alt="فضاء فروتيلو الداخلي"><figcaption>الفضاء الداخلي</figcaption></figure>', cnt=1)
    r.sub('<figure><img src="demo-cafe/img/g1.webp" alt="طاولة برانش مغربي كاملة"><figcaption>برانش الأصالة الكامل</figcaption></figure>',
          '<figure><img src="demo-cafe/img/g1.webp" alt="من توقيعات فروتيلو"><figcaption>من توقيعات الدار</figcaption></figure>', cnt=1)
    r.sub('<figure><img src="demo-cafe/img/g2.webp" alt="تحضير لاتيه آرت"><figcaption>لاتيه آرت كيتحضر قدامك</figcaption></figure>',
          '<figure><img src="demo-cafe/img/g2.webp" alt="تحضيرات طازجة"><figcaption>تحضيرات طازجة كل نهار</figcaption></figure>', cnt=1)
    r.sub('<figure><img src="demo-cafe/img/g3.webp" alt="تراس المقهى المطل على المدينة القديمة"><figcaption>الترّاس وإطلالة المدينة القديمة</figcaption></figure>',
          '<figure><img src="demo-cafe/img/g3.webp" alt="جلسة هادئة في فروتيلو"><figcaption>جلسة هادئة</figcaption></figure>', cnt=1)
    # infos
    r.sub("تلقانا في وسط طنجة، على مقربة من المحطة والمدينة القديمة.", "فرعان في تطوان — اختر الأقرب ليك.", cnt=1)
    r.sub("<p>الاثنين – الأحد<br>7:30 ← 23:00<br>البرانش حتى 14:00</p>",
          "<p>كل أيام الأسبوع<br>عين ملول: 08:00 ← 21:00<br>الولاية: 08:00 ← 23:00</p>", cnt=1)
    r.sub("<p>شارع محمد الخامس<br>وسط المدينة<br>طنجة، المغرب</p>",
          "<p>فرعان في تطوان:<br>عين ملول<br>الولاية</p>", cnt=1)
    r.sub("+212 693-981822", "+212 700-196943", cnt=2)
    r.sub("واتساب — رد سريع في أوقات العمل", "واتساب — فرع عين ملول", cnt=1)
    # order form
    r.sub("<option>طلب للتوصيل</option>", "<option>طلب للاستلام من الفرع</option>", cnt=1)
    r.sub("<option>طلب فطور/برانش لمجموعة</option>\n          ", "", cnt=1)
    r.sub('placeholder="مثال: طاولة لشخصين غداً مع 10:00، وفطور الأصالة الكامل…"',
          'placeholder="مثال: طاولة لشخصين غداً مع 10:00…"', cnt=1)
    r.sub("'السلام مقهى الأصالة، عندي طلب:\\n'", "'السلام Frutello، عندي طلب:\\n'", cnt=1)
    # footer
    r.sub('<div class="foot-logo">مقهى <span>الأصالة</span></div>', '<div class="foot-logo">Fru<span>tello</span></div>', cnt=1)
    r.sub("مقهى مختصة في قلب طنجة: قهوة مختصة، برانش مغربي وحلويات الدار — في أجواء دافئة مستوحاة من تراث المدينة.",
          "مقهى، باتيسري وجلاصيي في تطوان: بسطيلة، تشوروس بالشوكولاتة، جيلاتو الدار وقائمة كاملة — بفرعين: عين ملول والولاية.", cnt=1)
    r.sub("<li>📍 شارع محمد الخامس، طنجة</li>", "<li>📍 تطوان — عين ملول · الولاية</li>", cnt=1)
    r.sub("<li>🕖 كل أيام الأسبوع: 7:30 ← 23:00</li>", "<li>🕖 عين ملول 08:00 ← 21:00 · الولاية 08:00 ← 23:00</li>", cnt=1)
    r.sub("© 2026 مقهى الأصالة — Démo · 📌 نموذج تجريبي للعرض فقط — الصور والأثمنة توضيحية ولا تمثل مقهى حقيقياً.",
          "© 2026 Frutello — Démo VERTEX WEB · الصور توضيحية.", cnt=1)
    r.sub("أقسام مقهى الأصالة الأصلية", "أقسام Frutello الأصلية", cnt=1)
    # 3D layers
    r.sub("url:'cafe-assala.ma'", "url:'linktr.ee/frutello'", cnt=1)
    r.sub("label:'BRUNCH COMPLET — 55 DH'", "label:'BASTELLA'", cnt=1)
    r.sub("label:'LATTE ART — 22 DH'", "label:'CHURROS & CHOCOLAT'", cnt=1)
    r.sub('label:"L\'ESPACE — ZELLIGE"', 'label:"L\'ESPACE"', cnt=1)
    r.sub("label:'ATAY & CAFÉ — 16 DH'", "label:'GELATO MAISON'", cnt=1)
    # global number swap
    r.sub(OLD, NUM)
    out = r.done("demo-v4-frutello.html")
    (BASE / "demo-v4-frutello.html").write_text(out, encoding="utf-8")
    print("WROTE demo-v4-frutello.html", len(out.encode()), "bytes")

build_frutello()
print("CAFE demo done")


# =====================================================================
# PHOTO TEMPLATE -> Sara Loukili "moment with sara"
# =====================================================================
def build_sara():
    s = (BASE / "demo-photo.html").read_text(encoding="utf-8")
    r = Rep(s)
    NUM = "212776448922"
    r.sub("Atelier Lumière — Studio Photo à Tanger | Mariages, Portraits, Événements",
          "moment with sara — Sara Loukili, photographe d'événements à Tanger | Mariages & Fêtes", cnt=2)
    r.sub("Atelier Lumière, studio de photographie à Tanger : mariages, portraits, événements et photo produits. Un regard éditorial, des images qui traversent le temps.",
          "moment with sara — Sara Loukili, photographe d'événements à Tanger : mariages et fêtes documentés à l'iPhone, avec un regard spontané et naturel.", cnt=1)
    r.sub('<div class="demobar">📌 Modèle de démonstration — projet fictif présenté à titre d\'exemple, tarifs indicatifs</div>',
          '<div class="demobar">📌 Aperçu conçu spécialement pour « moment with sara » — Sara Loukili · par VERTEX WEB</div>', cnt=1)
    # remove priced PACKS section + TESTIMONIALS section first (drops 3 wa text links)
    r.regex(r'<section class="packs" id="packs">.*?</section>\n', '', cnt=1)
    r.regex(r'<section>\s*<div class="wrap">\s*<div class="sec-head">\s*<p class="kicker">Témoignages</p>.*?</section>\n', '', cnt=1)
    # wa text links (order: header, ov5, cta-band, footer, float)
    r.wa_text_links(NUM, [
        "Bonjour Sara, je souhaite réserver une séance photo pour un événement. Pouvez-vous me transmettre vos disponibilités ?",
        "Bonjour Sara, je souhaite réserver une séance photo pour un événement. Pouvez-vous me transmettre vos disponibilités ?",
        "Bonjour Sara, je prépare un événement à Tanger et je cherche une photographe. Pourriez-vous me transmettre un devis ?",
        "Bonjour Sara, je souhaite des informations pour une séance photo.",
        "Bonjour Sara, je souhaite des informations pour une séance photo.",
    ])
    r.sub('<div class="logo">Atelier <b>Lumière</b></div>', '<div class="logo">moment <b>with sara</b></div>', cnt=1)
    r.sub('<a href="#packs">03 · Formules</a>', '', cnt=1)
    r.sub('<img src="demo-photo/img/wide3d.webp" alt="Studio photo Atelier Lumière">',
          '<img src="demo-photo/img/wide3d.webp" alt="moment with sara — photographie d\'événements à Tanger">', cnt=1)
    # hero
    r.sub("// Scene 01 — L'Atelier · Tanger", "// Scene 01 — moment with sara · Tanger", cnt=1)
    r.sub('Atelier<br><span class="stroke">Lumière</span>', 'moment<br><span class="stroke">with sara</span>', cnt=1)
    r.sub("Mariages, portraits et événements à Tanger. Une lumière travaillée, un regard éditorial — faites défiler : écrans, images et typographie flottent devant vous, en 3D.",
          "Mariages et événements heureux à Tanger, photographiés à l'iPhone par Sara Loukili — un regard spontané et naturel. Faites défiler : écrans, images et typographie flottent devant vous, en 3D.", cnt=1)
    r.sub('<span class="micro">350+ mariages racontés</span>', '<span class="micro">Photographie iPhone</span>', cnt=1)
    r.sub('<span class="micro">Aperçu sous 48 h</span>', '<span class="micro">Mariages & événements</span>', cnt=1)
    r.sub("L'écran du studio, la photo large et le boîtier en couche libre — chacun avance à sa vitesse, parce que la profondeur est réelle.",
          "L'écran, la photo large et l'appareil en couche libre — chacun avance à sa vitesse, parce que la profondeur est réelle.", cnt=1)
    r.sub("Le studio en plein cadre — la lumière de Tanger, votre histoire.",
          "Vos moments en plein cadre — la lumière de Tanger, votre histoire.", cnt=1)
    r.sub("Chaque carte est un reportage à part entière — le mariage au centre, la mode et la beauté autour, en suspension.",
          "Chaque carte est un reportage à part entière — le mariage au centre, les fêtes et célébrations autour, en suspension.", cnt=1)
    r.sub("Les belles dates partent vite. Écrivez-nous sur WhatsApp avec la date de votre événement : réponse sous quelques heures, devis gratuit et sans engagement.",
          "Les belles dates partent vite. Écrivez-lui sur WhatsApp avec la date de votre événement pour vérifier sa disponibilité et recevoir un devis.", cnt=1)
    r.sub('<a href="#packs">Formules</a>', '', cnt=1)
    r.sub("Atelier Lumière © 2026 · Vertex Web — WebGL / GSAP / Lenis",
          "moment with sara © 2026 · Vertex Web — WebGL / GSAP / Lenis", cnt=1)
    # marquee
    mq = '<span>Mariages <i>//</i> Portraits <i>//</i> Événements <i>//</i> Éditorial <i>//</i> Produits &amp; marques <i>//</i></span>'
    r.sub(mq, '<span>Mariages <i>//</i> Fêtes <i>//</i> Événements <i>//</i> Moments heureux <i>//</i> Reportage iPhone <i>//</i></span>', cnt=2)
    # services
    r.sub("Du mariage intimiste au shooting de marque, chaque reportage est préparé sur mesure et retouché à la main, image par image.",
          "Mariages, fiançailles et fêtes de famille : Sara documente vos événements heureux à Tanger, à l'iPhone, avec un regard naturel et spontané.", cnt=1)
    r.regex(r'<div class="price">.*?</div>', '', cnt=4)
    r.sub("<h3>Portraits</h3>", "<h3>Fêtes & célébrations</h3>", cnt=1)
    r.sub("Séances portrait en studio ou en extérieur : book professionnel, portrait corporate, famille ou séance personnelle.",
          "Fiançailles, anniversaires et fêtes de famille, documentés avec spontanéité et discrétion.", cnt=1)
    r.sub("<h3>Produits & marques</h3>", "<h3>Reportage iPhone</h3>", cnt=1)
    r.sub("Photographie produit et contenu de marque pour boutiques, restaurants et créateurs qui veulent une image haut de gamme.",
          "Sa signature : un iPhone et un œil attentif — des images naturelles, prises sur le vif, qui racontent votre journée telle qu'elle s'est vécue.", cnt=1)
    # about
    r.sub('<figure><img src="demo-photo/img/about.jpg" alt="Le photographe d\'Atelier Lumière au travail"></figure>',
          '<figure><img src="demo-photo/img/about.jpg" alt="Photographe en plein reportage d\'événement"></figure>', cnt=1)
    r.sub("<h2>Derrière l'objectif, un œil formé à l'éditorial</h2>",
          "<h2>Derrière l'iPhone, un œil qui aime les vrais moments</h2>", cnt=1)
    r.sub("Atelier Lumière est né à Tanger d'une conviction simple : les plus belles images sont celles que l'on ne force pas. Nous travaillons en lumière naturelle dès que possible, nous dirigeons sans figer, et nous retouchons avec retenue pour garder la vérité des visages.",
          "« moment with sara », c'est le regard de Sara Loukili, photographe d'événements à Tanger. Spécialisée dans la documentation des moments heureux — mariages et fêtes — elle travaille à l'iPhone, en toute discrétion, pour capter les émotions telles qu'elles sont vécues.", cnt=1)
    r.sub("Chaque projet commence par un échange — autour d'un café ou en visio — pour comprendre votre histoire avant de la raconter en images.",
          "Son portfolio vit sur Instagram, au fil de ses reportages. Pour votre date, tout commence par un simple message WhatsApp : parlez-lui de votre événement.", cnt=1)
    r.sub("« La lumière de Tanger fait la moitié du travail. Nous faisons le reste. »",
          "« مصورة أيفونية لتوثيق لحظاتكم الحلوة » — Sara Loukili", cnt=1)
    # portfolio
    r.sub("Un aperçu de nos reportages récents — cliquez sur une image pour l'agrandir.",
          "Des ambiances qui ressemblent à vos plus beaux jours. Son portfolio complet est sur Instagram : @photographer_sara03 — cliquez sur une image pour l'agrandir.", cnt=1)
    r.sub('<figcaption>Éditorial mode</figcaption>', '<figcaption>Célébration</figcaption>', cnt=1)
    r.sub('<figcaption>Portrait beauté</figcaption>', '<figcaption>Moments complices</figcaption>', cnt=1)
    r.sub('<figcaption>Séance studio</figcaption>', '<figcaption>Fête de famille</figcaption>', cnt=1)
    r.sub('<figcaption>Portrait intérieur</figcaption>', '<figcaption>Détails du jour J</figcaption>', cnt=1)
    r.sub('<figcaption>Éditorial — Rouge</figcaption>', '<figcaption>Ambiance festive</figcaption>', cnt=1)
    r.sub('<figcaption>Shooting extérieur</figcaption>', '<figcaption>En extérieur</figcaption>', cnt=1)
    r.sub('<figcaption>Série artistique</figcaption>', '<figcaption>Instants volés</figcaption>', cnt=1)
    # cta band
    r.sub("Écrivez-nous sur WhatsApp avec la date de votre événement : réponse sous quelques heures, devis gratuit et sans engagement.",
          "Écrivez-lui sur WhatsApp avec la date de votre événement pour vérifier sa disponibilité et recevoir un devis.", cnt=1)
    r.sub("Demander un devis gratuit", "Demander un devis", cnt=1)
    # footer
    r.sub('<a class="flogo" href="#">Atelier <span>Lumière</span><small>Tanger · Photographie</small></a>',
          '<a class="flogo" href="#">moment <span>with sara</span><small>Tanger · Photographie d\'événements</small></a>', cnt=1)
    r.sub("Studio de photographie à Tanger spécialisé dans les mariages, les portraits et l'image de marque. Disponible dans tout le Nord du Maroc.",
          "Sara Loukili — photographe d'événements à Tanger. Mariages, fêtes et célébrations, documentés à l'iPhone avec un regard naturel.", cnt=1)
    r.sub('<li><a href="#services">Portraits</a></li>', '<li><a href="#services">Fêtes & célébrations</a></li>', cnt=1)
    r.sub('<li><a href="#services">Produits & marques</a></li>', '<li><a href="#services">Reportage iPhone</a></li>', cnt=1)
    r.sub("<li>📍 Centre-ville, Tanger</li>", "<li>📍 Tanger</li>", cnt=1)
    r.sub("<li>🕙 Mar – Sam : 10h00 – 19h00</li>",
          '<li>📷 Instagram : <a href="https://www.instagram.com/photographer_sara03" target="_blank" rel="noopener">@photographer_sara03</a></li>', cnt=1)
    r.sub('<p class="foot-line">نموذج تجريبي من مكتبة فيرتكس ويب — VERTEX WEB</p>',
          '<p class="foot-line">VERTEX WEB — Aperçu · Photos d\'illustration</p>', cnt=1)
    # 3D layers
    r.sub("url:'atelier-lumiere.tanger'", "url:'instagram.com/photographer_sara03'", cnt=1)
    r.sub("label:'ÉDITORIAL — MODE'", "label:'FÊTES & FAMILLE'", cnt=1)
    r.sub("label:'PORTRAIT — BEAUTÉ'", "label:'MOMENTS HEUREUX'", cnt=1)
    # global number swap (all remaining occurrences were wa text links, already replaced)
    r.s = r.s.replace(OLD, NUM)
    out = r.done("demo-v4-sara.html")
    (BASE / "demo-v4-sara.html").write_text(out, encoding="utf-8")
    print("WROTE demo-v4-sara.html", len(out.encode()), "bytes")

build_sara()
print("PHOTO demo done")
print("ALL 4 BUILT")
