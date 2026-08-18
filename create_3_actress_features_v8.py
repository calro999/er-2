import json
import os

# 1. 女優特集: 榊原萌
p1 = {
    "id": "feature-sakakibara-moe",
    "hinban": "SPECIAL-SAKAKIBARAMOE",
    "title": "【2026年最新版】榊原萌 透明感純白美少女＆素直なご奉仕！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】純白可愛い美少女！『榊原萌』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>吸い込まれるような瞳、ウブで可憐なビジュアル、そして素直すぎるご奉仕精神で絶大な人気を誇るS1専属女優<strong>『榊原萌』</strong>。「榊原萌 おすすめ」「榊原萌 相部屋」「榊原萌 VR」「榊原萌 初ベスト」などの検索クエリでアクセスが急増している。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 榊原萌がファンをキュン死させる3つの理由</h3>
<p>榊原萌の最大の抜きどころは、無垢な少女のような可愛さと、素直に尽くしてくれるご奉仕のギャップにある。</p>
<ul>
    <li><strong>ウブでキュン死させる可憐なルックス：</strong> 透明感溢れる素肌と、恥じらいつつも見つめてくる可愛い表情。</li>
    <li><strong>相部屋やお泊まりでの密着VR：</strong> スーツ姿の真面目な印象から、部屋着で無邪気に甘えてくる密着度。</li>
</ul>

<h3>2. 【神作厳選】榊原萌の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『終電逃してセクハラ店長とまさかの相部屋…朝まで続くキモい性交に不覚にも感じてしまった汚れを知らないバイト女子』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">終電を逃したバイト先で嫌な店長と相部屋。朝まで続く密会で、汚れを知らない体が不覚にも感じてしまう背徳ドラマ！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00949&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで相部屋背徳作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】終電逃して後輩宅に泊めてもらうことに…部屋着だと無防備で幼くて酔うと無邪気にあざとくエロがってくる背徳すぎる一夜』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">無防備な部屋着の榊原萌が、酔った勢いで無邪気に迫ってくる至高の主観VR体験！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsivr00499&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでお泊まりVR作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>榊原萌</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美少女・相部屋・VR・ご奉仕・単体作品</td></tr>
    <tr><td>透明感・可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>素直さ・没入感</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>榊原萌は、キュン死必至の可愛さと素直なエロスでファンを虜にする最高の美少女女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00949/sone00949pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00949/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00949/sone00949jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00949&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美少女", "相部屋", "単体作品"],
    "actresses": ["榊原萌"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "榊原萌", "S1", "SEO特化"]
}

# 2. 女優特集: 葵いぶき
p2 = {
    "id": "feature-aoi-ibuki",
    "hinban": "SPECIAL-AOIIBUKI",
    "title": "【2026年最新版】葵いぶき 国宝級美スタイル＆濃厚中出し！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】美スタイル＆爆発的エロス！『葵いぶき』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>引き締まった国宝級の美スタイル、圧倒的な性欲と濃厚な中出しパフォーマンスで大人気のMOODYZ専属女優<strong>『葵いぶき』</strong>。「葵いぶき おすすめ」「葵いぶき ハメ撮り」「葵いぶき 中出し」「葵いぶき VR」などの検索インテントに応える完全特集である。</p>
<p>本記事では、彼女の魅力が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 葵いぶきが誇る美スタイルと肉食系エロス</h3>
<p>葵いぶき最大の魅力は、抜群のスタイルから繰り出される積極的な腰振りと、本気の中出しピストンである。</p>

<h3>2. 【神作厳選】葵いぶきの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『ハメドリ 配信限定 MOODYZ専属のナチュラルSEXを解禁 葵いぶき』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">MOODYZ専属・葵いぶきのプライベート感満載ハメ撮り！ナチュラルな笑顔と激しい中出し性交が凝縮された傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmihd00001&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでナチュラルハメ撮り作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】【最狂キメセクVR】美スタイルが汁まみれのブッ飛び野獣中出し』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">飲みだけの女友達・葵いぶきが媚薬で野獣化！美スタイルが体液まみれになる圧巻の最狂VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmdvr00422&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでキメセクVR作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>葵いぶき</td></tr>
    <tr><td>所属メーカー</td><td>MOODYZ（ムーディーズ）</td></tr>
    <tr><td>主要属性</td><td>独占配信・美スタイル・スレンダー・ハメ撮り・VR・中出し・単体作品</td></tr>
    <tr><td>スタイル・プロポーション</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>エロ度・激しさ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>葵いぶきは、スタイルと激しいエロスでファンを魅了する最高のトップ女優。ぜひ今すぐ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/mihd00001/mihd00001pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=mihd00001/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/mihd00001/mihd00001jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmihd00001&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "美スタイル", "スレンダー", "ハメ撮り", "中出し", "単体作品"],
    "actresses": ["葵いぶき"],
    "maker": "MOODYZ",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "葵いぶき", "MOODYZ", "SEO特化"]
}

# 3. 女優特集: 石原希望
p3 = {
    "id": "feature-ishihara-nozomi",
    "hinban": "SPECIAL-ISHIHARANOZOMI",
    "title": "【2026年最新版】石原希望 明るいギャル＆爆絶演技！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】ギャルAV界の太陽！『石原希望』の絶対見るべき神作・名作徹底特集</h2>
<div class="review-intro">
<p>親しみやすいギャルスマイル、元気いっぱいのキャラクター、そして本気の中イキ・中出しパフォーマンスで圧倒的人気を集めるMOODYZの看板女優<strong>『石原希望』</strong>。「石原希望 おすすめ」「石原希望 即ズボ」「石原希望 中イキ」「石原希望 ハメ撮り」などの検索クエリに応える完全特集である。</p>
<p>本記事では、彼女の魅力が爆発した<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 石原希望がファンを笑顔と興奮で包む理由</h3>
<p>石原希望最大の魅力は、圧倒的なギャル可愛さと、どんなハードな企画でも全力で楽しんで中イキするリアリティにある。</p>

<h3>2. 【神作厳選】石原希望の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『絶対に笑ってはいけない即ズボピストン中出しイカセ24時！ 石原希望』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">笑うと罰ゲーム！不意打ち即ズボピストンに耐えつつも、結局気持ち良すぎて中出しされちゃう最高のエンタメ神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmida00747&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで即ズボ24時作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『観れば絶対中イキさせられる！ アナタもヌイて学べる 石原希望と一緒に！How to SEX！』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">石原希望が自ら中イキの秘密をレクチャー！本気で気持ちよくなりながらイカされる、抜きどころ100%のHow to作品！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmidv00725&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでHow to SEX作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>石原希望</td></tr>
    <tr><td>所属メーカー</td><td>MOODYZ（ムーディーズ）</td></tr>
    <tr><td>主要属性</td><td>独占配信・ギャル・中イキ・中出し・即ズボ・単体作品</td></tr>
    <tr><td>ギャル度・笑顔</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>中イキ・実用性</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>石原希望は、明るい笑顔と本気の中イキで全男を元気にする最高のギャル女優。ぜひ今すぐ彼女の代表作を体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/mida00747/mida00747pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=mida00747/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/mida00747/mida00747jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dmida00747&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "ギャル", "中イキ", "中出し", "単体作品"],
    "actresses": ["石原希望"],
    "maker": "MOODYZ",
    "date": "2026-08-18 00:00:00",
    "labels": ["女優特集", "石原希望", "MOODYZ", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
