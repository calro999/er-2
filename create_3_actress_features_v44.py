import json
import os

# 1. 女優特集: 桜ゆの
p1 = {
    "id": "feature-sakura-yuno-v2",
    "hinban": "SPECIAL-SAKURAYUNO-V2",
    "title": "【2026年最新版】桜ゆの Gカップ爆乳アニ声＆ツンデレ潮吹き！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】アニメ声×Gカップ爆乳のギャップ！『桜ゆの』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>可愛すぎるアニメ声、圧倒的ボリューミーなGカップ爆乳、そしてツンデレ＆大量潮吹きでファンの心を掴んで離さない大人気女優<strong>『桜ゆの』</strong>。「桜ゆの おすすめ」「桜ゆの アニメ声Gカップ」「桜ゆの 連れ子ヤリ爆」「桜ゆの 天井特化VR」「桜ゆの アニ声妹中出し」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女のキュートな声筋と極上爆乳エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 桜ゆのが「ギャップ萌え爆乳ヒロイン」として絶賛される理由</h3>
<p>桜ゆの最大の魅力は、耳に心地よいアニメ声と、ふんわりぷるぷる揺れるGカップ爆乳、そして激しい潮吹き絶頂ギャップにある。</p>

<h3>2. 【神作厳選】桜ゆのの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【ツンデレ潮吹き美少女】アニメ声×Gカップの最強ギャップ！ 桜ゆの』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">最強ギャップ萌え！生意気なのに鬼カワイイ桜ゆのが、アニメ声で喘ぎながらGカップ爆乳を揺らして激しく潮吹きする超人気作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dh_1711maan01175&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでアニメ声×Gカップツンデレ潮吹きを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『いもうとケータリングサービス Gカップ妹に合法イチャラブ中出し 桜ゆの』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">アニ声もカラダもボク専用！Gカップ爆乳妹・桜ゆのと自室で夢の合法イチャラブ中出し性交を堪能する大ヒット作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dymdd00498&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでアニ声Gカップ妹イチャラブ中出しを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>桜ゆの</td></tr>
    <tr><td>所属メーカー</td><td>マショウ / YMDD / ボンデージ</td></tr>
    <tr><td>主要属性</td><td>爆乳・Gカップ・アニメ声・ツンデレ・潮吹き・単体作品</td></tr>
    <tr><td>声・アニ声可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>胸・Gカップ爆乳</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>桜ゆのは、アニメ声の可愛さとGカップ爆乳で男性を虜にする最高のギャップ萌えヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/h_1711maan01175/h_1711maan01175pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=h_1711maan01175/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/h_1711maan01175/h_1711maan01175jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dh_1711maan01175&af_id=onchan555-007&ch=api",
    "genres": ["爆乳", "Gカップ", "アニメ声", "ツンデレ", "単体作品"],
    "actresses": ["桜ゆの"],
    "maker": "マショウ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "桜ゆの", "マショウ", "SEO特化"]
}

# 2. 女優特集: 小島みなみ
p2 = {
    "id": "feature-kojima-minami-v2",
    "hinban": "SPECIAL-KOJIMAMINAMI-V2",
    "title": "【2026年最新版】小島みなみ こじはま天使＆マドンナ衝撃中出し解禁！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】永久不滅の天使＆マドンナ看板！『小島みなみ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>「こじまこ」の愛称で親しまれる奇跡のアイドル美貌、甘いウィスパーボイス、そして13年の時を経てマドンナで中出し解禁を果たした伝説のヒロイン<strong>『小島みなみ』</strong>。「小島みなみ おすすめ」「小島みなみ 中出し解禁」「小島みなみ MadonnaVR」「小島みなみ 夫の上司」「小島みなみ 退職届NTR」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の可憐な可愛さと熟成された濃密エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 小島みなみが「全男の永久のアイドル」であり続ける理由</h3>
<p>小島みなみ最大の魅力は、衰えを知らない天使のスマイルと、マドンナ移籍で見せた大人の色気＆本気の中出し解禁にある。</p>

<h3>2. 【神作厳選】小島みなみの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『衝撃移籍第2弾！！13年の時を経て遂に中出し解禁 小島みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">AV史上の大事件！13年の歴史を経て遂に中出し解禁！小島みなみが義父に何度も中出しされる永久保存版最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00002&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで13年目の衝撃中出し解禁作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】MadonnaVR初登場！！小島みなみが大人の色気で迫る 小島みなみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">MadonnaVR初登場！妻の友人・小島みなみが大人の色気で淫靡に迫る！耳元で甘く囁かれながら密着性交を楽しむ至高の主観VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djuvr00273&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでMadonnaVR初登場作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>小島みなみ</td></tr>
    <tr><td>所属メーカー</td><td>マドンナ（Madonna） / S1 / アリスJAPAN</td></tr>
    <tr><td>主要属性</td><td>独占配信・天使・中出し解禁・MadonnaVR・人妻・単体作品</td></tr>
    <tr><td>アイドル美貌・笑顔</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>中出し感度・色気</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>小島みなみは、全男の夢を乗せて輝き続ける永遠のアイドルヒロイン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/jur00002/jur00002pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=jur00002/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/jur00002/jur00002jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00002&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "天使", "中出し解禁", "人妻", "単体作品"],
    "actresses": ["小島みなみ"],
    "maker": "マドンナ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "小島みなみ", "マドンナ", "SEO特化"]
}

# 3. 女優特集: 美谷朱音
p3 = {
    "id": "feature-mitani-akane-v2",
    "hinban": "SPECIAL-MITANIAKANE-V2",
    "title": "【2026年最新版】美谷朱音 肉感スタイル＆ささやき寸止めJOI！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】肉感美ボディ＆寸止めオナサポ！『美谷朱音』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>男を虜にする豊満な肉感スタイル、甘くサディスティックな声色、そして本中やDASで圧倒的な人気を誇るトップ女優<strong>『美谷朱音』</strong>。「美谷朱音 おすすめ」「美谷朱音 寸止めJOI」「美谷朱音 悪魔的スロー」「美谷朱音 ぎしたにVR」「美谷朱音 電車痴漢VR」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の肉感スタイルと焦らしオナサポエロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 美谷朱音（あかね）が「全男の性欲を管理するクイーン」と呼ばれる理由</h3>
<p>美谷朱音最大の魅力は、抱き心地抜群の肉感ボディと、耳元で優しく囁きながら限界まで焦らす寸止めコントロールテクニックにある。</p>

<h3>2. 【神作厳選】美谷朱音の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『ささやき誘惑で欲求MAXなのに射精させてくれない究極寸止めJOI 美谷朱音』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">全男子悶絶！美谷朱音が耳元で囁き誘惑しながら限界まで焦らす！絶対に射精を許さない究極の寸止めJOI神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Ddass00657&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでささやき究極寸止めJOIを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】【8K】山岸あや花＆美谷朱音のガチエロ仲良しコンビ【ぎしたに】VR』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">8K最高峰VR！山岸あや花と美谷朱音のガチ仲良しコンビがW凄テクで迫る、超贅沢な本中コラボ共演VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dprvr00081&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでぎしたにW凄テク8KVRを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>美谷朱音（みたにあかね）</td></tr>
    <tr><td>所属メーカー</td><td>本中（HONNAKA） / DAS</td></tr>
    <tr><td>主要属性</td><td>独占配信・肉感・寸止めJOI・ぎしたに・8KVR・単体作品</td></tr>
    <tr><td>肉感・抱き心地</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>寸止めテク・ささやき</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>美谷朱音は、肉感ボディと至高の寸止めテクで全男を操る最高のクイーン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/dass00657/dass00657pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=dass00657/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/dass00657/dass00657jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Ddass00657&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "肉感", "寸止めJOI", "8KVR", "単体作品"],
    "actresses": ["美谷朱音"],
    "maker": "DAS",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "美谷朱音", "DAS", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
