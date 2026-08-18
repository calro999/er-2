import json
import os

# 1. 女優特集: 田野憂
p1 = {
    "id": "feature-tano-yuu",
    "hinban": "SPECIAL-TANOYUU",
    "title": "【2026年最新版】田野憂 Lカップぷるぷる神乳＆圧倒的包容力！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】Lカップ美少女の最高峰！『田野憂』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>実りに実ったプルプルLカップ爆乳、可憐で可愛いルックス、そして尽くしたがりの神対応で男子を虜にするS1専属女優<strong>『田野憂』</strong>。「田野憂 おすすめ」「田野憂 Lカップ」「田野憂 彼女の妹」「田野憂 ベスト」などの検索クエリでアクセスが殺到している。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 田野憂が誇るLカップ神乳と圧倒的ご奉仕力</h3>
<p>田野憂の最大の抜きどころは、柔らかく弾むLカップおっぱいと、男子を全力で甘えさせてくれる包容力にある。</p>
<ul>
    <li><strong>実りに実ったプルプルLカップ：</strong> 思わず顔を埋めたくなる圧倒的ボリュームと柔らかさ。</li>
    <li><strong>彼女の妹シチュエーションでのノーブラ密着：</strong> 「お兄ちゃん…」と甘えてくるノーブラ密着パイズリ＆抱擁。</li>
</ul>

<h3>2. 【神作厳選】田野憂の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『彼女の妹が僕に一目惚れ！実りに実ったプルプルLカップをノーブラで！大胆見せつけ！むにゅっむにゅ密着！』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">彼女の妹・田野憂がノーブラLカップで猛アタック！むにゅむにゅ密着パイズリと生ハメに理性が吹き飛ぶ最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00713&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでノーブラLカップ妹作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『Lカップで美少女で尽くしたがりの神女優 田野憂 AVデビュー1周年 初ベスト 12時間』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">デビュー1年間の軌跡と最新12タイトルを12時間一挙収録したファン必携の完全保存版初ベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dofje00534&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで12時間初ベストを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>田野憂</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・超爆乳・Lカップ・彼女の妹・ベスト・単体作品</td></tr>
    <tr><td>胸・Lカップ度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ルックス・可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>田野憂は、Lカップ爆乳と可憐な笑顔でおっぱい好きを幸せにする最高の女優。ぜひ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00713/sone00713pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00713/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00713/sone00713jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00713&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "超爆乳", "Lカップ", "彼女の妹", "単体作品"],
    "actresses": ["田野憂"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "田野憂", "S1", "SEO特化"]
}

# 2. 女優特集: 兒玉七海
p2 = {
    "id": "feature-kodama-nanami",
    "hinban": "SPECIAL-KODAMANANAMI",
    "title": "【2026年最新版】兒玉七海 凛とした美貌＆真面目女子のノーパン背徳！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】真面目女子の恥じらい背徳！『兒玉七海』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>凛としたクールな美貌、真面目で清楚な雰囲気、そしてペナルティや裏の顔で見せる過激なギャップで大人気のS1専属女優<strong>『兒玉七海』</strong>。「兒玉七海 おすすめ」「兒玉七海 経理」「兒玉七海 ノーパン」「兒玉七海 デリヘル」などの検索インテントに応える完全特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 兒玉七海が魅せる真面目女子の背徳ギャップ</h3>
<p>兒玉七海最大の強みは、生真面目な美人が恥じらいながらも快楽に染まっていくリアルな表情にある。</p>

<h3>2. 【神作厳選】兒玉七海の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『「会社でこんな事させるなんて変態ですね…」 生真面目すぎる経理部の兒玉さんとまさかのデリヘル鉢合わせ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">会社の真面目な経理部・兒玉七海とデリヘルで衝撃の鉢合わせ！秘密を共有しながら濃厚な性交へと至る背徳の最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00972&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで経理部デリヘル作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『真面目な女子社員‘兒玉’さんがまさかのノルマ未達成！ペナルティのノーパン勤務に恥じらう姿がエロすぎる』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">ノルマ未達成のペナルティでノーパン勤務命令！恥ずかしさに頬を赤らめながら勤務する背徳オフィスドラマ！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00356&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでノーパン勤務作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>兒玉七海</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・OL・ノーパン・デリヘル・単体作品</td></tr>
    <tr><td>美貌・クールさ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>恥じらい・背徳感</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>兒玉七海は、真面目な美人が背徳の快楽に屈していく姿を描く最高の女優。ぜひ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00972/sone00972pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00972/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00972/sone00972jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00972&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "OL", "デリヘル", "単体作品"],
    "actresses": ["兒玉七海"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "兒玉七海", "S1", "SEO特化"]
}

# 3. 女優特集: 渚あいり
p3 = {
    "id": "feature-nagisa-airi",
    "hinban": "SPECIAL-NAGISA AIRI",
    "title": "【2026年最新版】渚あいり 天使の可愛さ＆圧倒的エロス！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】天使系美少女の最高峰！『渚あいり』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>愛くるしい天使のようなビジュアル、柔らかなボディ、そしてS1オールスター作品でも圧倒的存在感を放つトップ女優<strong>『渚あいり』</strong>。「渚あいり おすすめ」「渚あいり 美少女」「渚あいり 騎乗位」「渚あいり VR」などの検索クエリに応える完全特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>を徹底解説する。</p>
</div>

<h3>1. 渚あいりの天使系ビジュアルと濃厚エロスのギャップ</h3>
<p>渚あいり最大の魅力は、守ってあげたくなる可憐なルックスと、本能全開で快楽を楽しむ騎乗位・フェラパフォーマンスにある。</p>

<h3>2. 【神作厳選】渚あいりの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【VR】AV業界を席巻する超豪華S1専属女優25名とSEXできる！8KVRベスト第2弾！』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">8KVRの最高画質で渚あいりとの超至近距離SEXを体感！彼女の息遣いと可憐な笑顔が目の前に迫る至高のVR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsivr00380&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで8KVRベストを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『キングオブエロ痴女優21人 女性上位のアンアン イクイク 騎乗位100』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">渚あいりらトップ女優たちが自ら腰を振り喘ぎ狂う騎乗位特化総集編！女性上位の快楽を存分に堪能できる傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dofje00512&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで騎乗位100ベストを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>渚あいり</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・スレンダー・VR・騎乗位・単体作品</td></tr>
    <tr><td>天使度・可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>感度・演技力</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>渚あいりは、天使のような可憐さと情熱的なパフォーマンスでファンを魅了する最高の美少女女優。今すぐ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sivr00380/sivr00380pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sivr00380/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sivr00380/sivr00380jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsivr00380&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "スレンダー", "VR", "単体作品"],
    "actresses": ["渚あいり"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "渚あいり", "S1", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
