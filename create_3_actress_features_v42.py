import json
import os

# 1. 女優特集: 夏目響
p1 = {
    "id": "feature-natsume-hibiki-v2",
    "hinban": "SPECIAL-NATSUMEHIBIKI-V2",
    "title": "【2026年最新版】夏目響 圧倒的クール美貌＆引退メモリアル10時間！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】クール美貌の絶対的アイコン！『夏目響』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>クールでスタイリッシュな極上美貌、ショートカットが映える完璧なスタイル、そしてSODstarの絶対的エースとして時代を駆け抜けたカリスマ女優<strong>『夏目響』</strong>。「夏目響 おすすめ」「夏目響 引退10時間」「夏目響 最後のセックス」「夏目響 クール執事」「夏目響 ギャルライダー」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の圧倒的クール美貌とエロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 夏目響が「AV界至高のクールアイコン」と呼ばれる理由</h3>
<p>夏目響最大の魅力は、媚びない凛とした美しさと、本気の性交で見せる熱く激しい感情の吐露にある。</p>

<h3>2. 【神作厳選】夏目響の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『夏目響 引退 名前がなかったAV女優 最後のセックス』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">夏目響の集大成！彼女が最後に捧げる圧倒的熱量の濃厚性交。全ファン涙と感動の永久保存版引退作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1start00600&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで夏目響 引退 最後のセックスを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『夏目響 AV卒業記念SP総集編！ 25作品25SEX 10時間完全版』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">夏目響の全軌跡！デビューから名作、中出し解禁まで25作品25SEXを10時間に凝縮した、至高の卒業記念ベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1sods0085&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで卒業記念10時間完全版を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>夏目響</td></tr>
    <tr><td>所属メーカー</td><td>SODstar（エスオーディー スター）</td></tr>
    <tr><td>主要属性</td><td>独占配信・クール・引退作・総集編10時間・ショートカット・単体作品</td></tr>
    <tr><td>クール美貌・気品</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>スタイリッシュ感度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>夏目響は、クールなルックスと情熱的な演技で時代を創った至高の女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/1start00600/1start00600pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=1start00600/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/1start00600/1start00600jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1start00600&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "クール", "引退作", "ショートカット", "単体作品"],
    "actresses": ["夏目響"],
    "maker": "SODクリエイト",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "夏目響", "SODstar", "SEO特化"]
}

# 2. 女優特集: 風間ゆみ
p2 = {
    "id": "feature-kazama-yumi-v2",
    "hinban": "SPECIAL-KAZAMAYUMI-V2",
    "title": "【2026年最新版】風間ゆみ 熟女界の絶対女王＆過激教育ママ！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】全熟女ファンの絶対女王！『風間ゆみ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>豊かな包容力と妖艶な色気、熟女ジャンルの絶対的女王として四半世紀にわたりトップに君臨し続けるレジェンド女優<strong>『風間ゆみ』</strong>。「風間ゆみ おすすめ」「風間ゆみ 教育ママお仕置き」「风間ゆみ ムチ尻女上司」「風間ゆみ ブラック保育園」「風間ゆみ 僕の大好きな母」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の成熟した肉体美と濃厚な熟女エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 風間ゆみが「熟女界の永遠のクイーン」と呼ばれる理由</h3>
<p>風間ゆみ最大の魅力は、衰えぬ美貌と豊満なプロポーション、そして男性を優しく包み込みながら淫らに乱れさせる母性に溢れた色気にある。</p>

<h3>2. 【神作厳選】風間ゆみの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『過激すぎる教育ママのお仕置き射精管理 風間ゆみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">教育ママ・風間ゆみのご褒美お仕置き！息子を熟女の色気と手腕で射精管理する、ドM必見の超人気作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00827&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで過激教育ママのお仕置きを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『仕事中も気になって仕方ない欲求不満なムチ尻女上司 風間ゆみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">欲求不満なムチ尻女上司・風間ゆみが職場で誘惑！部下の視線を奪いながら情熱的にハメ狂う熟女大ヒット作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00850&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでムチ尻女上司作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>風間ゆみ</td></tr>
    <tr><td>所属メーカー</td><td>JUICY / マドンナ（Madonna）</td></tr>
    <tr><td>主要属性</td><td>独占配信・熟女・絶対女王・教育ママ・ムチ尻・単体作品</td></tr>
    <tr><td>熟女色気・母性</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>包容力・ご奉仕</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>風間ゆみは、熟女界の頂点に立ち続ける永遠のクイーン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/jur00827/jur00827pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=jur00827/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/jur00827/jur00827jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00827&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "熟女", "絶対女王", "教育ママ", "単体作品"],
    "actresses": ["風間ゆみ"],
    "maker": "マドンナ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "風間ゆみ", "マドンナ", "SEO特化"]
}

# 3. 女優特集: 竹内有紀
p3 = {
    "id": "feature-takeuchi-yuki-v2",
    "hinban": "SPECIAL-TAKEUCHIYUKI-V2",
    "title": "【2026年最新版】竹内有紀 筋肉美ボディ＆真夏の大痙攣エビ反り不倫！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】引き締まった筋肉美ボディ！『竹内有紀』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>美しく鍛え上げられた筋肉美ボディ、元キャスターのような知性と品格、そしてマドンナで激しい跳ねイキ・エビ反り絶頂を見せる実力派女優<strong>『竹内有紀』</strong>。「竹内有紀 おすすめ」「竹内有紀 筋肉美ボディ」「竹内有紀 エビ反り不倫」「竹内有紀 最高の愛人」「竹内有紀 密着トレーニング」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の筋肉美スタイルと極上エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 竹内有紀が「美ボディお姉さん」として大絶賛される理由</h3>
<p>竹内有紀最大の魅力は、無駄のない美しい筋肉スタイルと、激しい性交で宙に浮くほど跳ね狂う絶頂反応のギャップにある。</p>

<h3>2. 【神作厳選】竹内有紀の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『宙に浮くほどイキ跳ねる真夏の大痙攣エビ反り不倫SEX 竹内有紀』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">竹内有紀がエビ反り大痙攣！宙に浮くほどピストンでイキ跳ね、真夏の不倫性交で快楽の限界を突破する大ヒット作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00812&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで大痙攣エビ反り不倫を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『最高の愛人、最高の中出し。 竹内有紀』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">理想の愛人・竹内有紀と過ごす最高のひととき！美しい筋肉美ボディを抱きしめ、何度も濃密中出しを注ぎ込む名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dyuj00054&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで最高の愛人最高の中出しを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>竹内有紀</td></tr>
    <tr><td>所属メーカー</td><td>マドンナ（Madonna） / JUICY</td></tr>
    <tr><td>主要属性</td><td>独占配信・筋肉美・美ボディ・エビ反り・中出し・単体作品</td></tr>
    <tr><td>美ボディ・スタイル</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>絶頂・エビ反り感度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>竹内有紀は、筋肉美スタイルと激しいエビ反り絶頂でファンを魅了する最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/jur00812/jur00812pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=jur00812/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/jur00812/jur00812jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Djur00812&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "筋肉美", "美ボディ", "エビ反り", "単体作品"],
    "actresses": ["竹内有紀"],
    "maker": "マドンナ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "竹内有紀", "マドンナ", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
