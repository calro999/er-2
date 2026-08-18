import json
import os

# 1. 女優特集: 白上咲花
p1 = {
    "id": "feature-shirakami-sakura",
    "hinban": "SPECIAL-SHIRAKAMISAKURA",
    "title": "【2026年最新版】白上咲花 透明感溢れる純白少女！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】純白美少女の頂点！『白上咲花』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>透き通るような白肌、ウブで儚げな透明感、そして背徳的なシチュエーションで見せるギャップ絶頂で絶大な人気を誇るS1専属女優<strong>『白上咲花』</strong>。「白上咲花 おすすめ」「白上咲花 妹」「白上咲花 ぶっかけ」「白上咲花 8KVR」などの検索クエリで常にアクセスが殺到している。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と、その圧倒的透明感を徹底解説する。</p>
</div>

<h3>1. 白上咲花がファンを惹きつけてやまない理由</h3>
<p>白上咲花の最大の魅力は、限りなく純白に近い美少女オーラと、淫らな刺激に染まっていく快楽堕ちのギャップである。</p>
<ul>
    <li><strong>圧倒的な透明感と可憐な笑顔：</strong> 雪国育ちを思わせる色白肌と無垢なルックス。</li>
    <li><strong>ウブな少女が快楽に屈していくリアルさ：</strong> 恥じらいながらもピストンの衝撃に背中を反らせる本気演技。</li>
</ul>

<h3>2. 【神作厳選】白上咲花の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『ウブでシャイで未成熟な彼女の妹に欲情し、こっそりハメ続けた最低な僕。 白上咲花』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">彼女の未成熟な妹・白上咲花をこっそり誘惑し、背徳の快楽に沈めていく背徳ドラマの最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00822&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで彼女の妹背徳作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『限りなく透明に近い純白少女 白上咲花 1年のすべて。12作品コンプリート初ベスト』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">白上咲花のデビュー1年間の軌跡と神作12本を凝縮した、ファン必携の完全保存版コンプリートベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dofje00531&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでコンプリートベストを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>白上咲花</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・妹・スレンダー・背徳・単体作品</td></tr>
    <tr><td>透明感・ルックス</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>背徳感・没入度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>白上咲花は、純白の透明感と背徳エロスのギャップでファンを魅了する最高の美少女女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00822/sone00822pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00822/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00822/sone00822jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00822&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "妹", "スレンダー", "単体作品"],
    "actresses": ["白上咲花"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "白上咲花", "S1", "SEO特化"]
}

# 2. 女優特集: 三田真鈴
p2 = {
    "id": "feature-mita-marin",
    "hinban": "SPECIAL-MITAMARIN",
    "title": "【2026年最新版】三田真鈴 ほんわか癒し系＆小悪魔従順エロス！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】ほんわか癒し系美少女！『三田真鈴』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>柔らかい笑顔、ほんわかとした癒し系オーラ、そして男子に尽くしてくれる圧倒的な優しさで大人気を誇るS1専属女優<strong>『三田真鈴』</strong>。「三田真鈴 おすすめ」「三田真鈴 家庭教師」「三田真鈴 VR」「三田真鈴 筆おろし」などの検索インテントに応える完全特集である。</p>
<p>本記事では、彼女の魅力が最も発揮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 三田真鈴のほんわかボイスと密着ご奉仕</h3>
<p>三田真鈴が多くのファンを沼らせる理由は、お母さんのような優しさと、彼氏に依存して尽くしてくれる従順さにある。</p>

<h3>2. 【神作厳選】三田真鈴の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『童貞君の成績と射精を徹底管理してくれる ほんわか家庭教師の超優しい筆おろしレクチャー 三田真鈴』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">ほんわか家庭教師・三田真鈴が童貞男子のペニスを優しくリードし、管理・筆おろししてくれる至高の癒し名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00836&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで家庭教師筆おろし作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】クラスで一番かわいい真鈴さんは放課後、僕の前だけでマゾちらかす欲しがり雑魚ペットでした。』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">クラスのアイドル・三田真鈴が放課後に自分だけのペットに！圧倒的距離感と密着度を誇る主観VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsivr00500&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでマゾペットVR作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>三田真鈴</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・家庭教師・筆おろし・VR・単体作品</td></tr>
    <tr><td>癒し度・笑顔</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ご奉仕・没入感</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>三田真鈴は、優しさと甘いボイスで男子を包み込む最高の癒し系女優。ぜひ今すぐ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00836/sone00836pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00836/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00836/sone00836jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00836&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "家庭教師", "筆おろし", "単体作品"],
    "actresses": ["三田真鈴"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "三田真鈴", "S1", "SEO特化"]
}

# 3. 女優特集: 清宮仁愛
p3 = {
    "id": "feature-kiyomiya-niina",
    "hinban": "SPECIAL-KIYOMIYANIINA",
    "title": "【2026年最新版】清宮仁愛 Jカップ超ダイナマイトボディ痴女！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】Jカップ爆乳＆黒ギャル痴女！『清宮仁愛』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>Jカップの超ダイナマイトボディ、170cm超の圧倒的プロポーション、そしてイケイケなギャル＆痴女パフォーマンスで爆発的な人気を誇る<strong>『清宮仁愛』</strong>。「清宮仁愛 おすすめ」「清宮仁愛 Jカップ」「清宮仁愛 ギャル」「清宮仁愛 VR」などの検索クエリに応える完全特集である。</p>
<p>本記事では、彼女の爆乳と痴女パフォーマンスが炸裂した<b>【絶対に見るべき最高傑作3選】</b>を徹底解説する。</p>
</div>

<h3>1. 清宮仁愛のJカップボディと肉食痴女パフォーマンス</h3>
<p>清宮仁愛の最大の特徴は、圧倒的な胸の存在感と、男をグイグイ引っ張る肉食系ギャルのアプローチにある。</p>

<h3>2. 【神作厳選】清宮仁愛の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『ギャルと呑むと楽しいしエロがってくれる！ Jcup完璧ボディ痴女が酔った勢いでM男を容赦なくイカせまくる』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">Jカップ爆乳痴女・清宮仁愛が、酔った勢いで男を激しく責め立てて連続絶頂へ導く、圧巻の爆乳ギャル作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Debwh00243&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでJカップ痴女作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】ギャルをのぞく穴 おかずにしているのがバレて痴女られる可哀想な僕』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">清宮仁愛のJカップ胸が視界を埋め尽くす！壁の穴からのぞき見していたのがバレて逆レイプされる至高のVR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Debvr00129&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでのぞき穴VR作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>清宮仁愛</td></tr>
    <tr><td>所属メーカー</td><td>E-BODY</td></tr>
    <tr><td>主要属性</td><td>爆乳・Jカップ・ギャル・痴女・VR・単体作品</td></tr>
    <tr><td>胸・Jカップ爆乳</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>痴女度・迫力</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>清宮仁愛は、Jカップ爆乳とギャル痴女フェチにとって絶対に見逃せない最高峰の女優。ぜひ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ebwh00243/ebwh00243pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ebwh00243/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ebwh00243/ebwh00243jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Debwh00243&af_id=onchan555-007&ch=api",
    "genres": ["爆乳", "Jカップ", "ギャル", "痴女", "単体作品"],
    "actresses": ["清宮仁愛"],
    "maker": "E-BODY",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "清宮仁愛", "E-BODY", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
