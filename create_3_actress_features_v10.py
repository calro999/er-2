import json
import os

# 1. 女優特集: 神木麗
p1 = {
    "id": "feature-kamiki-rei",
    "hinban": "SPECIAL-KAMIKIREI",
    "title": "【2026年最新版】神木麗 国宝級Gカップ神乳＆圧倒的ビジュアル！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】グラドル級Gカップ美貌！『神木麗』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>圧倒的な国宝級Gカップ美バスト、洗練されたモデル級のルックス、そして一度見たら忘れられない濃密なエロスでシーンの頂点に君臨するSODstar絶対的ヒロイン<strong>『神木麗』</strong>。「神木麗 おすすめ」「神木麗 セフレ」「神木麗 じゅぽフェラ」「神木麗 タワーマンション」などの検索クエリでアクセスが殺到している。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 神木麗がファンを狂わせる3つの理由</h3>
<p>神木麗がこれほどまでに愛され、トップを走り続ける理由は3つの圧倒的オーラにある。</p>
<ul>
    <li><strong>グラドル級の圧倒的Gカップ＆美顔：</strong> 誰もが目を奪われる極上のバストラインと、気品溢れるお姉さんルックス。</li>
    <li><strong>濃厚な「じゅぽフェラ」と積極的な誘惑：</strong> 画面越しに目が合うだけで射精に導かれる圧倒的なご奉仕テクニック。</li>
    <li><strong>タワマンやセフレドラマにおける圧倒的没入感：</strong> 背徳的なストーリーを完璧に演じ切る演技力。</li>
</ul>

<h3>2. 【神作厳選】神木麗の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『欲求不満女子大生は海の家の短期バイト中ビーチに集まる男達の筋肉と汗の匂いにムラムラが抑えられず…じゅぽフェラで誘惑しまくった 神木麗』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">海の家で働く欲求不満女子大生・神木麗が、男たちを濃厚じゅぽフェラで誘惑しまくる最高峰のご奉仕作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1start00232&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでじゅぽフェラ海の家作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『「結婚するのでもう会えない…」2年続いたセフレから連絡あり…夜明けまで生ハメ中出ししまくったのがどちゃくそ良かった件 神木麗』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">2年続いたセフレ関係の最後の一夜。神木麗と名残惜しみながら朝まで生ハメ中出しを繰り返す切なく官能的な神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1start00126&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでセフレ最後の一夜作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>神木麗</td></tr>
    <tr><td>所属メーカー</td><td>SODstar（エスオーディー スター）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・Gカップ・フェラ・セフレ・中出し・単体作品</td></tr>
    <tr><td>ルックス・グラドル美顔</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ご奉仕・Gカップ感度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>神木麗は、Gカップ美バストと濃厚なご奉仕で男を虜にする絶対的ヒロイン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/1start00232/1start00232pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=1start00232/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/1start00232/1start00232jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1start00232&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "Gカップ", "フェラ", "中出し", "単体作品"],
    "actresses": ["神木麗"],
    "maker": "SODクリエイト",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "神木麗", "SODstar", "SEO特化"]
}

# 2. 女優特集: 安達夕莉
p2 = {
    "id": "feature-adachi-yuri",
    "hinban": "SPECIAL-ADACHIYURI",
    "title": "【2026年最新版】安達夕莉 爆乳ボディ＆水泳コーチ密着！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】爆乳ボディ＆水泳コーチ！『安達夕莉』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>あふれんばかりの爆乳、弾ける笑顔、そして布面積1%の衝撃水着や浴衣姿でファンを魅了するS1専属女優<strong>『安達夕莉』</strong>。「安達夕莉 おすすめ」「安達夕莉 水泳」「安達夕莉 VR」「安達夕莉 浴衣」などの検索インテントに応える完全特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 安達夕莉が魅せる爆乳密着と開放的エロス</h3>
<p>安達夕莉最大の強みは、見ているだけで元気になる明るい笑顔と、爆乳が肉薄する圧倒的密着指導にある。</p>

<h3>2. 【神作厳選】安達夕莉の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『水泳部の美人コーチが男子部員のやる気をエロで爆上げ！ 布面積1％水着でほぼ裸体密着コーチング 安達夕莉』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">水泳部の美人コーチ・安達夕莉が布面積1%の超過激水着で密着指導！やる気を爆上げする最高の爆乳水着作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00306&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで水泳コーチ密着作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】浴衣から溢れる生おっぱいに舞い上がりバイト先の後輩ちゃんと絶頂花火を打ち上げまくった祭りのあと 安達夕莉』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">浴衣姿の安達夕莉と祭りのあとに二人きり。溢れ出す生おっぱいに埋もれる至高の主観VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsivr00328&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで浴衣生おっぱいVRを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>安達夕莉</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・爆乳・水泳・VR・浴衣・単体作品</td></tr>
    <tr><td>胸・爆乳密着度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>明るさ・可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>安達夕莉は、爆乳ボディと明るいエロスで全男を幸せにする最高のトップ女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/snos00306/snos00306pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=snos00306/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/snos00306/snos00306jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00306&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "爆乳", "水泳", "単体作品"],
    "actresses": ["安達夕莉"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "安達夕莉", "S1", "SEO特化"]
}

# 3. 女優特集: 流川莉央
p3 = {
    "id": "feature-rukawa-rio",
    "hinban": "SPECIAL-RUKAWARIO",
    "title": "【2026年最新版】流川莉央 デカ尻＆関西弁甘えエロス！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】デカ尻美少女＆関西弁甘え！『流川莉央』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>キュートなルックス、極上のデカ尻ヒップライン、そして甘い関西弁で男性を虜にするトップ女優<strong>『流川莉央』</strong>。「流川莉央 おすすめ」「流川莉央 デカ尻」「流川莉央 VR」「流川莉央 メンヘラ」などの検索クエリに応える完全特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>を徹底解説する。</p>
</div>

<h3>1. 流川莉央のデカ尻ヒップと関西弁ささやきの魅力</h3>
<p>流川莉央最大の魅力は、弾力のある豊満なデカ尻と、耳元で甘く囁かれる関西弁の多幸感にある。</p>

<h3>2. 【神作厳選】流川莉央の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【VR】【8K】子種をください…メンヘラちゃんと温泉不倫旅行 流川莉央』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">8KVRの超高精細映像で、流川莉央と温泉不倫旅行。子種を求める甘い囁きと至近距離性交に溺れる至高のVR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dpxvr00302&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで温泉不倫VRを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】デカ尻P活女子のとろける関西弁甘えささやきでお金もザーメンも搾り取られたボク。 流川莉央』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">とろける関西弁で甘えてくるデカ尻パパ活女子・流川莉央！ザーメンも精神も搾り取られる快感VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsavr00728&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで関西弁パパ活VRを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>流川莉央</td></tr>
    <tr><td>所属メーカー</td><td>CRYSTAL / Moodyz</td></tr>
    <tr><td>主要属性</td><td>美少女・デカ尻・関西弁・VR・パパ活・単体作品</td></tr>
    <tr><td>お尻・デカ尻度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>関西弁・甘え度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>流川莉央は、デカ尻と関西弁甘えでお尻フェチを狂わせる最高の女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/pxvr00302/pxvr00302pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=pxvr00302/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/pxvr00302/pxvr00302jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dpxvr00302&af_id=onchan555-007&ch=api",
    "genres": ["美少女", "デカ尻", "関西弁", "VR", "単体作品"],
    "actresses": ["流川莉央"],
    "maker": "クリスタル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "流川莉央", "CRYSTAL", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
