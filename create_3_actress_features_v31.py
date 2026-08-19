import json
import os

# 1. 女優特集: 希志あいの
p1 = {
    "id": "feature-kishi-aino",
    "hinban": "SPECIAL-KISHIAINO",
    "title": "【2026年最新版】希志あいの 伝説のレジェンドアイドル＆48時間コンプリート！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】全AV界の伝説的アイドル！『希志あいの』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>圧巻のアイドル級美貌、完璧なプロポーション、そしてアイデアポケットの絶対的看板として時代を創り上げた伝説のヒロイン<strong>『希志あいの』</strong>。「希志あいの おすすめ」「希志あいの コンプリート48時間」「希志あいの 引退SP」「希志あいの 裏道デート」「希志あいの 100SEX」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の圧倒的スター性と官能エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 希志あいのが「伝説のスーパーアイドル」として語り継がれる理由</h3>
<p>希志あいのが引退後もなお神格化され愛され続ける理由は、完璧なアイドルビジュアルと、作品ごとに魅せる本気のリアクションにある。</p>

<h3>2. 【神作厳選】希志あいのの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『希志あいの COMPLETE BOX 48時間』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">伝説の全記録！希志あいのの輝かしい名作と成長を48時間という超大ボリュームでコンプリートした、ファン永久保存版BOX！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Didbd00754&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで48時間コンプリートBOXを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『ありがとう 希志あいの引退SP』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">全ファンが涙した感動と歓喜の引退スペシャル！希志あいののプロ意識と極上エロスの全てを解き放つ伝説作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dipz00667&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでありがとう希志あいの引退SPを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">③『【AIリマスター版】ちょっと危ない裏道デート～渋谷編～ 希志あいの』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">渋谷の裏道で秘密のデート！AIリマスターで超高画質に甦った、希志あいのみずみずしい素顔と情熱的なイチャラブ性交！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsrxv00799ai&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで裏道デートAIリマスター版を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>希志あいの</td></tr>
    <tr><td>所属メーカー</td><td>IDEAPOCKET（アイデアポケット）</td></tr>
    <tr><td>主要属性</td><td>独占配信・伝説・スーパーアイドル・引退・コンプリート・単体作品</td></tr>
    <tr><td>美貌・アイドル性</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>レジェンド・存在感</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>希志あいのは、全AV史において燦然と輝く絶対的スーパーアイドル。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/idbd00754/idbd00754pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=idbd00754/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/idbd00754/idbd00754jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Didbd00754&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "伝説", "スーパーアイドル", "引退", "単体作品"],
    "actresses": ["希志あいの"],
    "maker": "アイデアポケット",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "希志あいの", "アイデアポケット", "SEO特化"]
}

# 2. 女優特集: 初川みなみ
p2 = {
    "id": "feature-hatsukawa-minami",
    "hinban": "SPECIAL-HATSUKAWAMINAMI",
    "title": "【2026年最新版】初川みなみ 照れカワ絶対的ヒロイン＆極上ねっとりエロス！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】照れカワ＆極上甘々！『初川みなみ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>ふんわり甘い笑顔、照れながらも相手を気持ちよくさせてくれる優しさ、そしてプレステージ＆MOODYZで絶大な人気を誇った絶対的ヒロイン<strong>『初川みなみ』</strong>。「初川みなみ おすすめ」「初川みなみ 乳首こねくり」「初川みなみ 温泉相部屋NTR」「初川みなみ 女教師」「初川みなみ 引退作」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の可愛さと極上甘々エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 初川みなみが全男子から愛される理由</h3>
<p>初川みなみ最大の魅力は、ふんわりとした「照れカワ」の表情と、男性をトロけさせるねっとりとしたご奉仕にある。</p>

<h3>2. 【神作厳選】初川みなみの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『乳首をず～っとこねくりっ放し性交 初川みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">性交中もずっと乳首を優しく攻め立てられる！初川みなみの甘い吐息と指先で脳が溶ける至高の快楽名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmide00543&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで乳首こねくりっ放し性交を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『出張先のひなびた温泉旅館で新卒女子社員とまさかの相部屋逆NTR 初川みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">温泉旅館で新卒女子社員・初川みなみと相部屋！彼女の凄い腰使いに何度も中出しさせられてしまう大ヒット作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmvsd00474&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで温泉旅館相部屋逆NTRを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">③『中華なると原作 女教師 京子 ～快楽調教室～ 初川みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">大人気コミック実写化！初川みなみが美しき女教師を演じ、調教され快楽に開眼していく伝説の官能名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dure00070&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで女教師京子快楽調教室を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>初川みなみ</td></tr>
    <tr><td>所属メーカー</td><td>MOODYZ / プレステージ</td></tr>
    <tr><td>主要属性</td><td>照れカワ・甘々・温泉・相部屋・女教師・単体作品</td></tr>
    <tr><td>可愛さ・癒やし</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ねっとり密着</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>初川みなみは、照れカワな愛らしさと濃厚な密着でファンを魅了する最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/mide00543/mide00543pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=mide00543/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/mide00543/mide00543jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmide00543&af_id=onchan555-007&ch=api",
    "genres": ["照れカワ", "甘々", "温泉", "女教師", "単体作品"],
    "actresses": ["初川みなみ"],
    "maker": "MOODYZ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "初川みなみ", "MOODYZ", "SEO特化"]
}

# 3. 女優特集: 立花里子
p3 = {
    "id": "feature-tachibana-satoko",
    "hinban": "SPECIAL-TACHIBANASATOKO",
    "title": "【2026年最新版】立花里子 狂乱の絶対女王＆AIリマスター！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】AV界最高の絶対女王！『立花里子』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>ドSかつ狂乱の痴女演技、ポルチオ覚醒での激しい膣痙攣、そしてAV界の歴史で異彩を放つ伝説の絶対女王<strong>『立花里子』</strong>。「立花里子 おすすめ」「立花里子 女教師中出し」「立花里子 ポルチオトランス」「立花里子 8時間ベスト」「立花里子 麻薬捜査官」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の凄まじい熱量とAIリマスターで鮮烈に甦る最高潮エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 立花里子が「伝説の女王」として崇拝され続ける理由</h3>
<p>立花里子最大の魅力は、他者を圧倒するドSな存在感と、ポルチオ刺激によって限界まで崩壊・痙攣する過激なギャップにある。</p>

<h3>2. 【神作厳選】立花里子の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【AIリマスター】女教師 中出し20連発 立花里子』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">AIリマスターで鮮明に甦る！女教師・立花里子が連続中出し20連発で屈服し絶頂する、伝説のハード名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1iesp00107h&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで女教師中出し20連発を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『ULTRA ポルチオトランス 立花里子』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">ポルチオ覚醒でトランス状態！立花里子の身体が歓喜の悲鳴を上げ、全身痙攣でイク衝撃の過激作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dh_175dupt00001&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでULTRAポルチオトランスを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">③『あの時の君に会いたい。 立花里子 8時間』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">あの時の激しさを8時間贅沢に凝縮！立花里子の伝説の過激シーンを網羅した、永久保存版メモリアルベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D55t2800283&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで立花里子8時間ベストを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>立花里子</td></tr>
    <tr><td>所属メーカー</td><td>エスワン / アタッカーズ / KMP</td></tr>
    <tr><td>主要属性</td><td>伝説・ドS女王・ポルチオ・AIリマスター・中出し・単体作品</td></tr>
    <tr><td>女王オーラ・ドS度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ポルチオ感度・痙攣</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>立花里子は、AV史において唯一無二の狂乱とカリスマ性を誇った伝説の女王。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/1iesp00107h/1iesp00107hpl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=1iesp00107h/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/1iesp00107h/1iesp00107hjp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1iesp00107h&af_id=onchan555-007&ch=api",
    "genres": ["伝説", "ドS女王", "ポルチオ", "AIリマスター", "単体作品"],
    "actresses": ["立花里子"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "立花里子", "S1", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
