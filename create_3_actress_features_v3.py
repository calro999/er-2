import json
import os

# 1. 女優特集: 金松季歩
p1 = {
    "id": "feature-kanamatsuriho",
    "hinban": "SPECIAL-KANAMATSURIHO",
    "title": "【2026年最新版】金松季歩 元芸能人の圧倒的オーラ＆色気！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】元人気芸能人の圧倒的オーラ！『金松季歩』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>元人気グラビアアイドル・芸能人としての華やかなオーラ、豊満な巨乳、そして溢れ出る大人の色気で爆発的な人気を誇るS1専属女優<strong>『金松季歩』</strong>。「金松季歩 おすすめ」「金松季歩 痴漢」「金松季歩 不倫」「金松季歩 デリヘル」などの検索クエリで常にアクセスが殺到している。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と、その圧倒的ルックスと濃密なエロスを徹底解説する。</p>
</div>

<h3>1. 金松季歩が圧倒的オーラでファンを魅了する理由</h3>
<p>金松季歩の最大の強みは、芸能人時代の圧倒的なビジュアルと、それとは裏腹な体当たりの情熱的演技にある。</p>
<ul>
    <li><strong>芸能人レベルの圧倒的ルックスとボディ：</strong> 誰もが惹きつけられる洗練された顔立ちと、豊かなバストライン。</li>
    <li><strong>背徳的なシチュエーションが映える色気：</strong> 女教師、人妻、デリヘルなど、大人の背徳ドラマにおける圧倒的ハマり役。</li>
</ul>

<h3>2. 【神作厳選】金松季歩の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『聖職者でありながら電車痴●の虜になってしまった女教師 金松季歩』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">真面目な女教師・金松季歩が、満員電車で背徳の快楽に目覚めていく衝動と葛藤を描いた大傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00791&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで女教師痴漢作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『大停電の夜に…美人上司と二人きり 憧れの巨乳と色気と暗闇に理性を失い夜が明けるまで一晩中射精しまくった』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">停電したオフィスで憧れの美人上司・金松季歩と密会。理性を失い朝まで濃厚に求め合う背徳の一夜！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00309&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで美人上司密会作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>金松季歩</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・芸能人・巨乳・女教師・不倫・単体作品</td></tr>
    <tr><td>オーラ・美貌</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>色気・演技力</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>金松季歩は、圧倒的な美貌と色気で大人の背徳ドラマを完璧に演じ切るトップ女優。ぜひ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00791/sone00791pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00791/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00791/sone00791jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00791&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "芸能人", "巨乳", "女教師", "単体作品"],
    "actresses": ["金松季歩"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "金松季歩", "S1", "SEO特化"]
}

# 2. 女優特集: 山岸あや花
p2 = {
    "id": "feature-yamagishi-ayaka",
    "hinban": "SPECIAL-YAMAGISHIAYAKA",
    "title": "【2026年最新版】山岸あや花 熟練のテクニック＆感度絶頂！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】技巧派＆感度抜群！『山岸あや花』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>圧倒的なテクニック、感度抜群の絶頂リアクション、そして親しみやすい美貌で根強い人気を誇る専属女優<strong>『山岸あや花』</strong>。「山岸あや花 おすすめ」「山岸あや花 中イキ」「山岸あや花 VR」「山岸あや花 旅館」などの検索インテントに応える完全特集である。</p>
<p>本記事では、彼女の魅力が最も発揮された<b>【絶対に見るべき最高傑作3選】</b>と、その絶頂・ご奉仕パフォーマンスを徹底解説する。</p>
</div>

<h3>1. 山岸あや花が魅せる感度とテクニックの凄み</h3>
<p>山岸あや花が多くのファンを虜にする理由は、単なる演技を超えたリアルな絶頂リアクションにある。</p>

<h3>2. 【神作厳選】山岸あや花の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『アナタも絶対中イキさせられる！シコって学べる！How to SEX！山岸あや花をイカせよう！！！』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">山岸あや花の中イキ開発と濃厚ピストンを実践形式で描いた、快楽度100%の最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dpred00820&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでHow to SEX作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】シン・痴女VR 山岸あや花に射精させられるだけの世界 原点にして頂点！』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">山岸あや花が汗だくで攻めてくる超濃密VR。チンポに夢中な彼女のアプローチに昇天間違いなし！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dprvr00084&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで痴女VR作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>山岸あや花</td></tr>
    <tr><td>所属メーカー</td><td>PREMIUM（プレミアム）</td></tr>
    <tr><td>主要属性</td><td>独占配信・人妻・中イキ・VR・単体作品</td></tr>
    <tr><td>テクニック・感度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>エロ度・実用性</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>山岸あや花は、中イキ開発や濃厚VRで至高の快楽を提供する天才女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/pred00820/pred00820pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=pred00820/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/pred00820/pred00820jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dpred00820&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "人妻", "中イキ", "単体作品"],
    "actresses": ["山岸あや花"],
    "maker": "プレミアム",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "山岸あや花", "PREMIUM", "SEO特化"]
}

# 3. 女優特集: 美園和花
p3 = {
    "id": "feature-misono-waka",
    "hinban": "SPECIAL-MISONOWAKA",
    "title": "【2026年最新版】美園和花 爆乳＆連続アクメ中出し！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】爆乳＆連続絶頂姫！『美園和花』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>豊満な爆乳、可憐なルックス、そして「もうイッてるってばぁ！」と叫びながら何度も中出しされる連続アクメで絶大な人気を誇る女優<strong>『美園和花』</strong>。「美園和花 おすすめ」「美園和花 中出し」「美園和花 爆乳」「美園和花 寸止め」などの検索クエリに応える完全特集である。</p>
<p>本記事では、彼女の魅力が炸裂した<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 美園和花の爆乳ボディと連続中出しアクメ</h3>
<p>美園和花の最大の抜きどころは、絶頂しても止まらない怒涛の連激ピストンと生中出しの連続である。</p>

<h3>2. 【神作厳選】美園和花の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『「もうイッてるってばぁ！」状態で何度も中出し！ 美園和花』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">限界突破の連続絶頂の中で容赦なく注ぎ込まれる中出しラッシュ。美園和花の代表作であり最高峰の抜き作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dwaaa00436&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで連続中出し作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『ささやき誘惑でチンシコ欲求MAXなのに、絶対に射精させてくれない究極寸止めJOI 美園和花』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">美園和花が耳元で甘く囁きながらギリギリまで焦らす、寸止フェチ必見の究極JOI作品！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Ddass00913&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで寸止めJOI作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>美園和花</td></tr>
    <tr><td>所属メーカー</td><td>DAS / WAAA</td></tr>
    <tr><td>主要属性</td><td>爆乳・中出し・連続アクメ・寸止め・単体作品</td></tr>
    <tr><td>胸・爆乳度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>アクメ・絶頂感</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>美園和花は、爆乳好き・中出しフェチにとって至高の存在。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/waaa00436/waaa00436pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=waaa00436/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/waaa00436/waaa00436jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dwaaa00436&af_id=onchan555-007&ch=api",
    "genres": ["爆乳", "中出し", "連続アクメ", "単体作品"],
    "actresses": ["美園和花"],
    "maker": "WAAA",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "美園和花", "WAAA", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
