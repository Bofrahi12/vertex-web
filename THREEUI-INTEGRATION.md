# ThreeUI — بطاقة إدماج VERTEX (بأمر المالك 2026-11-06)

المصدر: ريل @rawad.dev (instagram.com/reel/DfXk7KNRibz) — «مواقع بـ$3K» بقوالب جاهزة.
المكتبة: **ThreeUI** ديال Meng To / DesignCode — https://threeui.com · https://github.com/MengTo/threeui
النسخة المحلية الكاملة: `~/workspace/tools/threeui/` (89MB، Community edition، تحقّق 2026-11-06: 50 مكوّناً رئيسياً، 164 نتيجة تصفّح، 7,131 نجمة GitHub).

## الترخيص — الخط الأحمر
- **Community فقط: رخصة MIT** (الكود + الصور ديال ThreeUI) — استعمال تجاري مسموح في مواقع الزبناء.
- **Pro / Beta: ماشي في الريبو وماشي MIT** — ممنوع جلبها أو تقليد مصدرها؛ أي مكوّن موسوم Pro في threeui.com خارج الخدمة.
- الخطوط المرفقة OFL، وThree.js بـMIT — كلشي نظيف.

## كيفاش كتدخل في بنائنا (مواقعنا ثابتة HTML، ماشي React)
1. **المسار المفضّل — Shaders مستقلة**: `src/shaders/` فيها 48 مجلداً و**70 ملف HTML قائم بذاتو** (بلا build) — كتتنسخ/كتتدمج مباشرة في صفحاتنا الثابتة. أمثلة: liquid-metal-button, lumen-cta, brand-orbs, globe, dot-matrix, koi-studies, temple-night, landscape, bookshelf.
2. **مسار React**: `src/package-components/` فيها 103 مكوّنات TSX (npm: `@designcodeio/threeui`) — كتستعمل غير في مشاريع React، أو كنحوّلو المكوّن يدوياً لـvanilla قبل الدمج في موقع ثابت.
3. كل مكوّن إجرائي (procedural) ~100–200KB بلا أصول ثقيلة — كيتبدّل الثيم/الإضاءة/الحركة بالكود، ماشي بصور جاهزة.

## المختارات الأولى حسب نوع الزبون
- **Hero / خلفيات**: DotMatrixBackground, FlowField, FluidFieldBackground, NebulaBackground, ConstellationField, CloudField, RibbonFieldBackground, WarpFieldBackground
- **أزرار وCTA**: LiquidMetalButton, GenerateButton, GradientCta / GradientBeamCta, GlassmorphismCta, IgnitionButton, SlidingTextCta
- **منتجات/عرض**: BookshelfScene + BestsellersBookShowcase (مكتبات/كتب/منتجات على رفوف), Gallery, CharacterCarousel
- **صفحات كاملة كمرجع بنية**: KageLandingPage (اللي بان في الريل), CompleteShelfLandingPage, MengToSketchbookLandingPage
- **نصوص وحركة**: NeonTypography, TextAnimationCollection, OutlineTypeflow, AnimatedTopDock, UplinkLoader (لودر)

## مصادر مجانية بنفس الجودة (بأمر المالك 2026-11-06: «نجيبهم من بلاصة أخرى فري بنفس الجودة»)
- **React Bits** — محلي: `~/workspace/tools/react-bits/` · ‏218 مكوّناً (64 خلفية WebGL: Aurora/Galaxy/LiquidChrome/Hyperspeed + 48 مكوّن + 33 نصاً متحركاً + 38 أنيميشن + 35 micro) · 51K نجمة · الترخيص **MIT + Commons Clause**: مجاني داخل مواقع/منتجات الزبناء، الممنوع غير إعادة بيع المكتبة نفسها كمنتج.
- **Magic UI** — محلي: `~/workspace/tools/magicui/` · ‏80 مكوّناً · **MIT نقي** · 23K نجمة.
- **GSAP كامل** — مجاني 100% بكل بلاغيناتو (SplitText/MorphSVG/ScrollSmoother اللي كانت مدفوعة) من بعد استحواذ Webflow، بترخيص GSAP «No Charge» (ماشي MIT ولكن مجاني تجارياً) — عبر npm/CDN، بلا حاجة لكلون.
- أبواب إضافية عند الحاجة: Aceternity UI (نسخ مجاني من الموقع)، Uiverse (MIT)، Codrops (افحص ترخيص كل ديمو بوحدو قبل الاستعمال).

## قواعد ملزمة عند الاستعمال
- تأثير WebGL **واحد ثقيل كحد أقصى في الصفحة** (hero) — الباقي خفيف؛ الأداء قبل الزينة.
- فحص 390px + إيقاف الحركة خارج الشاشة (offscreen pause) + احترام prefers-reduced-motion.
- ما كيبدّل حتى قاعدة قائمة: بوابة الأمان §10 (فحص الأسرار) وبوابة الحمل §11 (k6) قبل أي تسليم، وقاعدة «الأصول أولاً» وفحص التيليفون ديال المالك هو الحكم النهائي.
- ThreeUI **مكوّنات** ماشي موقعاً كاملاً: البنية والهوية والمحتوى الحقيقي ديال الزبون كيبقاو ديالنا (R1–R15 + Templates A–E كيتشاورو قبل البناء كالعادة، وThreeUI كتتسجّل في ملف المشروع كمصدر مكوّنات).
