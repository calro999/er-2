import json
import os

# 1. 女優特集: 坂道みる
p1 = {
    "id": "feature-sakamichi-miru",
    "hinban": "SPECIAL-SAKAMICHIMIRU",
    "title": "【2026年最新版】坂道みる 圧倒的才能＆爆量イキ潮絶頂！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】AV界の天才美少女＆爆発的オーガズム！『坂道みる』の絶対見るべき神作・名作完全攻略ガイド</h2>
<div class="review-intro">
<p>デビューから圧倒的な輝きを放ち、天才的な感度と爆量イキ潮絶頂でシーンを震撼させたS1絶対的ヒロイン<strong>『坂道みる』</strong>。「坂道みる おすすめ」「坂道みる 潮吹き」「坂道みる 追撃ピストン」「坂道みる 痙攣」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の天才的感度と圧倒的絶頂が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 坂道みるが「AV界の逸材」と賞賛される3つの理由</h3>
<p>坂道みるが今なお伝説として語り継がれ、圧倒的評価を受ける理由は3つの天才的感度にある。</p>
<ul>
    <li><strong>美少女ルックスと本能剥き出しの絶頂リアクション：</strong> 可憐なルックスからは想像もつかない本気のアへ顔とガクガク痙攣。</li>
    <li><strong>追撃ピストンで溢れ出す爆量イキ潮：</strong> 連続ピストンで体が吹き出すように潮を吹き続ける圧巻の感度。</li>
    <li><strong>S1史に残る大ヒット作品群のクオリティ：</strong> どの作品を手に取ってもハズレが一切ない高密度エロス。</li>
</ul>

<h3>2. 【神作厳選】坂道みるの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『快感潮吹き絶頂マ●コを怒涛の追撃ピストンでひたすら大量潮吹きオーガズム 坂道みる』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">絶頂に次ぐ絶頂！坂道みるが連続追撃ピストンで限界突破し、大量の潮を吹き荒らす伝説の最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssni00608&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで追撃ピストン潮吹き作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『激イキ193回！痙攣4700回！イキ潮10000cc！セックスの逸材18才 エロス覚醒 大大大・痙・攣』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">18歳のエロス覚醒！激イキ193回＆痙攣4700回を記録した、坂道みるの才能が爆発した衝撃の出世作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssni00353&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで18歳エロス覚醒作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>坂道みる</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・逸材・潮吹き・絶頂・単体作品</td></tr>
    <tr><td>感度・潮吹き度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ルックス・可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>坂道みるは、AV史に刻まれる天才的感度と圧倒的絶頂で全男を魅了する最高のヒロイン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ssni00608/ssni00608pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ssni00608/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ssni00608/ssni00608jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssni00608&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "逸材", "潮吹き", "単体作品"],
    "actresses": ["坂道みる"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "坂道みる", "S1", "SEO特化"]
}

# 2. 女優特集: 小島みなみ
p2 = {
    "id": "feature-kojima-minami",
    "hinban": "SPECIAL-KOJIMAMINAMI",
    "title": "【2026年最新版】小島みなみ 伝説の萌えキュン可愛さ＆中出し解禁！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】AV界のレジェンドアイドル！『小島みなみ』の絶対見るべき神作・名作完全攻略ガイド</h2>
<div class="review-intro">
<p>甘く可憐なボイス、10年以上にわたり業界の第一線で輝き続ける萌えルックス、そしてマドンナ移籍での衝撃中出し解禁で話題を呼ぶトップ女優<strong>『小島みなみ』</strong>。「小島みなみ おすすめ」「小島みなみ 中出し」「小島みなみ 義父」「小島みなみ マドンナ」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女のレジェンド級エロスが凝縮された<b>【絶対を見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 小島みなみが永きにわたり愛され続ける理由</h3>
<p>小島みなみの最大の強みは、変わらない圧倒的可愛さと、熟練した演技が生み出す背徳感のギャップにある。</p>

<h3>2. 【神作厳選】小島みなみの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『衝撃移籍第2弾！！13年の時を経て遂に…中出し解禁ー。 夫と子作りSEXをした後はいつも義父に中出しされ続けています…。 小島みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">13年の時を経て遂に解禁された衝撃の中出し！夫との子作りの裏で義父に種付けされ続ける背徳の超神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00002&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで中出し解禁義父作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『夫の上司に犯●れ続けて7日目、私は理性を失った…。 小島みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">夫の上司に連日犯され続ける人妻・小島みなみ。抗えない快楽に7日目で理性が崩壊していく濃厚NTR作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00815&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで夫の上司NTR作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>小島みなみ</td></tr>
    <tr><td>所属メーカー</td><td>マドンナ / Alice Japan</td></tr>
    <tr><td>主要属性</td><td>レジェンド・中出し解禁・人妻・NTR・萌えボイス・単体作品</td></tr>
    <tr><td>可愛さ・萌えボイス</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>背徳感・中出し</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>小島みなみは、可愛さと背徳の中出しエロスで全男を魅了するレジェンド女王。今すぐ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/jur00002/jur00002pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=jur00002/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/jur00002/jur00002jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00002&af_id=onchan555-007&ch=api",
    "genres": ["レジェンド", "中出し解禁", "人妻", "NTR", "単体作品"],
    "actresses": ["小島みなみ"],
    "maker": "マドンナ",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "小島みなみ", "マドンナ", "SEO特化"]
}

# 3. 女優特集: 安位薫
p3 = {
    "id": "feature-anwi-kaoru",
    "hinban": "SPECIAL-ANWIKAORU",
    "title": "【2026年最新版】安位薫（安位カヲル） むっちり爆胸グラドル＆凄テク手コキ！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】グラドル級むちむち肉感ボディ！『安位薫』の絶対見るべき神作・名作完全攻略ガイド</h2>
<div class="review-intro">
<p>グラビアアイドルとしても大活躍したむっちり肉感ボディ、とろけるような甘い接客、そして「油ベロぬる地獄」や凄テク手コキで男性を昇天させるトップ女優<strong>『安位薫（安位カヲル）』</strong>。「安位薫 おすすめ」「安位カヲル むっちり」「安位薫 手コキ」「安位薫 8KVR」などの検索クエリに応える完全保存版特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 安位薫が誇るむちむち肉体美と極上ハンドテク</h3>
<p>安位薫最大の魅力は、抱き心地抜群のむっちりボディと、指先一つで男の理性を吹き飛ばす凄テク手コキにある。</p>

<h3>2. 【神作厳選】安位薫の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『もうアカン。肉感むっちむち超甘イイ女の油ベロぬる地獄でチソポが異常トロける無限爆どぴゅ沼性交 安位薫』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">むっちむち肉感ボディの安位薫が、油ベロぬる愛撫でペニスを溶かす！無限射精沼へと引きずり込まれる最高峰名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Ddass00419&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで油ベロぬる沼性交作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】【8K】ヤッたら終わる系女子とヤッてしまってセク沼。（狂ったみたいに11発射精） 安位薫』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">8KVRの超高解像度で安位薫に狂ったように11発射精させられる！セク沼にどっぷりハマる至高の主観VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D13dsvr01828&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで11発射精セク沼8KVRを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>安位薫（安位カヲル）</td></tr>
    <tr><td>所属メーカー</td><td>DAS / FALENO / HONNAKA</td></tr>
    <tr><td>主要属性</td><td>グラドル・むっちり・爆乳・手コキ・VR・単体作品</td></tr>
    <tr><td>肉感・スタイル</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>テクニック・愛撫</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>安位薫は、むっちりボディと極上テクニックで男を骨抜きにする最高の女優。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/dass00419/dass00419pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=dass00419/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/dass00419/dass00419jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Ddass00419&af_id=onchan555-007&ch=api",
    "genres": ["グラドル", "むっちり", "爆乳", "手コキ", "単体作品"],
    "actresses": ["安位薫"],
    "maker": "DAS",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "安位薫", "DAS", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
