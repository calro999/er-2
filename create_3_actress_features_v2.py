import json
import os

# 1. 女優特集: 小野六花
p1 = {
    "id": "feature-ono-rikka",
    "hinban": "SPECIAL-ONORIKKA",
    "title": "【2026年最新版】小野六花 国宝級の可愛さと小悪魔エロス！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】学園アイドル＆小悪魔の最高峰！『小野六花』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>くりっとした大きな瞳、弾けるような可憐な笑顔、そして内に秘めた小悪魔的エロスで圧倒的な人気を誇るMOODYZの絶対的ヒロイン<strong>『小野六花』</strong>。「小野六花 おすすめ」「小野六花 フェラ」「小野六花 中出し」「小野六花 VR」などの検索クエリで絶大なアクセスを誇る。</p>
<p>本記事では、彼女の魅力が最も発揮された<b>【絶対に見るべき最高傑作3選】</b>と、その可憐なルックスと濃厚なご奉仕テクニックを徹底解説する。</p>
</div>

<h3>1. 小野六花がファンを虜にする3つの理由</h3>
<p>なぜ小野六花はこれほどまでに愛され続けるのか。その理由は3つの奇跡的なギャップにある。</p>
<ul>
    <li><strong>学園アイドル級の可憐なルックス：</strong> 清楚で可愛らしいルックス。画面越しに目が合うだけで恋に落ちる圧倒的ヒロイン力。</li>
    <li><strong>追撃フェラ＆ご奉仕の圧倒的積極性：</strong> 射精後もペニスを放さず、何度も顔射や中出しを求めてくる小悪魔パフォーマンス。</li>
    <li><strong>VR作品における圧倒的彼女感：</strong> 手を繋ぎ、耳元で吐息を漏らすVR作品での没入感は業界最高峰。</li>
</ul>

<h3>2. 【神作厳選】小野六花の絶対見るべき最高傑作3选</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『射精後チ●ポも追撃フェラでまた顔射させてくれる学園アイドル 小野六花』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">1発終わった後の敏感ペニスを優しく舐め上げ、連続で顔射へと導く小悪魔追撃フェラの最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmida00730&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで追撃フェラ作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】MOODYZファン感謝祭 バコバコバスツアー2025VR』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">小野六花をはじめとするMOODYZトップ女優陣との夢の一泊二日。超至近距離で手をつなぎ、密会する最高のVR体験。</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmdvr00388&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでバコバスVRを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>小野六花</td></tr>
    <tr><td>所属メーカー</td><td>MOODYZ（ムーディーズ）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・小柄・学園・フェラ・顔射・VR・単体作品</td></tr>
    <tr><td>ルックス・アイドル性</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ご奉仕・エロ度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>小野六花は、可憐な可愛さと濃厚なご奉仕で男を癒し・狂わせる最高のヒロインである。ぜひ彼女の代表作を今すぐ体感してほしい。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/mida00730/mida00730pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=mida00730/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/mida00730/mida00730jp-1.jpg",
        "https://pics.dmm.co.jp/digital/video/mida00730/mida00730jp-2.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmida00730&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "小柄", "フェラ", "顔射", "単体作品"],
    "actresses": ["小野六花"],
    "maker": "MOODYZ",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "小野六花", "MOODYZ", "SEO特化"]
}

# 2. 女優特集: 未歩なな
p2 = {
    "id": "feature-miho-nana",
    "hinban": "SPECIAL-MIHONANA",
    "title": "【2026年最新版】未歩なな 奇跡の美顔＆圧倒的ご奉仕！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】美顔ご奉仕の最高峰！『未歩なな』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>整った端正な顔立ちと、弾けるような笑顔、そして圧倒的なご奉仕精神で全男を魅了するS1トップ女優<strong>『未歩なな』</strong>。「未歩なな おすすめ」「未歩なな フェラ」「未歩なな 顔射」「未歩なな 8KVR」などの検索インテントに応える完全特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作】</b>と、その美貌と濃厚エロスを徹底解説する。</p>
</div>

<h3>1. 未歩ななが愛され続ける理由</h3>
<p>未歩ななの最大の強みは、どんな激しいプレイでも崩れない圧倒的美貌と、男を心から喜ばせようとする笑顔にある。</p>

<h3>2. 【神作厳選】未歩ななの絶対見るべき最高傑作</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『毎日スペルマ洗顔させてください！顔面がちょー可愛くって明るくてご奉仕精神のかたまり』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">顔面国宝の未歩ななが、満面の笑みで大量のスペルマを受け止めるご奉仕フェラ＆顔射の最高峰！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00854&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでスペルマ洗顔作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>未歩なな</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・スレンダー・フェラ・顔射・ご奉仕・単体作品</td></tr>
    <tr><td>ルックス・美顔度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ご奉仕・エロ度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>未歩ななは、美しさとご奉仕精神の双方で頂点に立つ女優。ぜひ彼女の代表作をチェックしよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00854/sone00854pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00854/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00854/sone00854jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00854&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "スレンダー", "フェラ", "顔射", "単体作品"],
    "actresses": ["未歩なな"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "未歩なな", "S1", "SEO特化"]
}

# 3. 女優特集: 楓ふうあ
p3 = {
    "id": "feature-kaede-fua",
    "hinban": "SPECIAL-KAEDEFUA",
    "title": "【2026年最新版】楓ふうあ 長身高身長ボディ＆エロス！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】高身長スレンダーの頂点！『楓ふうあ』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>モデルのような圧倒的高身長、スラリと伸びる長い脚、そして小悪魔的なエロスでファンを熱狂させるS1専属女優<strong>『楓ふうあ』</strong>。「楓ふうあ おすすめ」「楓ふうあ 長身」「楓ふうあ 乳首」「楓ふうあ 顔射」などの検索クエリに応える完全特集である。</p>
<p>本記事では、彼女の長身ボディが生み出す神作と見どころを徹底解説する。</p>
</div>

<h3>1. 楓ふうあの長身スレンダーボディとフェティシズム</h3>
<p>高身長ならではの長い手足を駆使した密着プレイと、強烈なドS・ドM両対応のパフォーマンスが光る。</p>

<h3>2. 【神作厳選】楓ふうあの絶対見るべき最高傑作</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『M男カレシの乳首を長い手足でずっと責め続けるエッチな年上彼女の24時間ち・く・び責めデート 楓ふうあ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">長身ボディでカレシを覆いかぶさり、長い手足で絶え間なく乳首を責め続ける至高のフェチ作品！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00361&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで乳首責めデート作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>楓ふうあ</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・長身・スレンダー・巨乳・乳首・単体作品</td></tr>
    <tr><td>スタイル・長身美身</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>エロ度・フェチ感</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>楓ふうあは、高身長スレンダー好きにとって生涯一度は見るべき最高の女優である。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/snos00361/snos00361pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=snos00361/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/snos00361/snos00361jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00361&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "長身", "スレンダー", "巨乳", "乳首", "単体作品"],
    "actresses": ["楓ふうあ"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "楓ふうあ", "S1", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
