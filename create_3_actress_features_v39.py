import json
import os

# 1. 女優特集: 栗山莉緒
p1 = {
    "id": "feature-kuriyama-rio-v2",
    "hinban": "SPECIAL-KURIYAMARIO-V2",
    "title": "【2026年最新版】栗山莉緒 腹筋美くびれ＆全肯定彼女VR！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】腹筋くびれ美ボディ＆極上ボイス！『栗山莉緒』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>見惚れるような引き締まった腹筋美くびれ、甘く溶けるような癒やしの極上ボイス、そしてアタッカーズやDASの看板として圧倒的な人気を誇るトップ女優<strong>『栗山莉緒』</strong>。「栗山莉緒 おすすめ」「栗山莉緒 全肯定彼女VR」「栗山莉緒 ガテン系失禁」「栗山莉緒 美容インフルエンサー」「栗山莉緒 敏感ホットヨガ」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の美ボディと甘々・ハード両面の濃密エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 栗山莉緒がトップ女優として絶大な支持を集める理由</h3>
<p>栗山莉緒最大の魅力は、運動で鍛え上げられた腹筋美くびれスタイルと、相手を優しく包み込む「全肯定」の癒やしボイスにある。</p>

<h3>2. 【神作厳選】栗山莉緒の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【VR】脳みそとろける甘々ボイスで囁く全肯定彼女と同棲生活VR 栗山莉緒』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">全男子の理想！栗山莉緒が甘々ボイスで囁きながら丁寧に抜いてくれる同棲生活VR。脳みそがトロける至高の癒やし主観神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Datvr00071&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで全肯定彼女同棲生活VRを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『腹筋くびれボディの美容系インフルエンサーが話題のオイルエステでエビ反り絶頂 栗山莉緒』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">美しい腹筋くびれボディがオイル塗れ！話題のオイルエステで身体中の体液を溢れさせ、エビ反り絶頂を繰り返す大ヒット名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Datid00688&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでオイルエステエビ反り絶頂を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>栗山莉緒</td></tr>
    <tr><td>所属メーカー</td><td>ATTACKERS（アタッカーズ） / DAS</td></tr>
    <tr><td>主要属性</td><td>独占配信・腹筋くびれ・全肯定・ボイス・VR・単体作品</td></tr>
    <tr><td>腹筋・美ボディ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>甘々ボイス・癒やし</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>栗山莉緒は、完璧な腹筋くびれボディと甘々ボイスで全男を虜にする最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/atvr00071/atvr00071pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=atvr00071/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/atvr00071/atvr00071jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Datvr00071&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "腹筋くびれ", "全肯定", "VR", "単体作品"],
    "actresses": ["栗山莉緒"],
    "maker": "アタッカーズ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "栗山莉緒", "アタッカーズ", "SEO特化"]
}

# 2. 女優特集: 逢沢みゆ
p2 = {
    "id": "feature-aizawa-miyu-v2",
    "hinban": "SPECIAL-AIZAWAMIYU-V2",
    "title": "【2026年最新版】逢沢みゆ 華奢美乳＆神回ハメ撮り！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】華奢美乳＆ヤリマンオーラ全開！『逢沢みゆ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>守りたくなる華奢なスタイル、美しいバスト、そして『神回ハメログ』で酔うとヤリマンオーラ全開になる本能の魅力で大人気の女優<strong>『逢沢みゆ』</strong>。「逢沢みゆ おすすめ」「逢沢みゆ 神回ハメログ」「逢沢みゆ Re:Temptation」「逢沢みゆ ガン反り中出し」「逢沢みゆ バック大好き美尻」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の華奢な可愛さと生々しいハメ撮りエロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 逢沢みゆが男子の心を掴んで離さない理由</h3>
<p>逢沢みゆ最大の魅力は、華奢で小柄な美少女ボディと、お酒が回って素直に甘えてくるドスケベなギャップにある。</p>

<h3>2. 【神作厳選】逢沢みゆの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【神回ハメログ】逢沢みゆちゃんにお酒を飲ませたらヤリマンオーラが全開だったのでそのままハメ撮り』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">神回確定！お酒を飲んだ逢沢みゆがヤリマンオーラ全開で甘えてくる！リアルな体液交歓と生ハメを捉えた至高のハメ撮り名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dtikb00219&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで神回ハメログを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『バック大好き！！美尻セフレちゃん逢沢みゆとラブホをはしごして丸1日巣ごもり尻揉み中出し』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">バックが大好きな逢沢みゆとラブホをハシゴ！美尻を揉みしだかれながら何度も中出しを注ぎ込まれる最高のセフレ作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1jera00026&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでバック大好き美尻セフレ中出しを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>逢沢みゆ</td></tr>
    <tr><td>所属メーカー</td><td>MOODYZ / ロイヤル / チカチカ</td></tr>
    <tr><td>主要属性</td><td>華奢美乳・ハメ撮り・バック・セフレ・中出し・単体作品</td></tr>
    <tr><td>華奢感・可愛さ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ハメ撮り生々しさ</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>逢沢みゆは、華奢な身体と素直な生々しさでファンを熱狂させる最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/tikb00219/tikb00219pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=tikb00219/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/tikb00219/tikb00219jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dtikb00219&af_id=onchan555-007&ch=api",
    "genres": ["華奢美乳", "ハメ撮り", "バック", "セフレ", "単体作品"],
    "actresses": ["逢沢みゆ"],
    "maker": "チカチカ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "逢沢みゆ", "チカチカ", "SEO特化"]
}

# 3. 女優特集: 小野夕子
p3 = {
    "id": "feature-ono-yuko-v2",
    "hinban": "SPECIAL-ONOYUKO-V2",
    "title": "【2026年最新版】小野夕子 Hカップ爆乳痴女＆ザーメン狩り40本番！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】Hカップ極上爆乳＆圧倒的ザーメン狩り！『小野夕子』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>圧倒的な存在感を放つHカップ爆乳バスト、男の精子を根底から搾り尽くす激しい痴女テクニック、そしてFALENO最乳ヒロインとして君臨する大人気女優<strong>『小野夕子』</strong>。「小野夕子 おすすめ」「小野夕子 ザーメン狩り40本番」「小野夕子 チク活痴女」「小野夕子 温泉二人きり」「小野夕子 リップVR」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女のHカップ爆乳と圧倒的搾精エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 小野夕子が「全男のザーメンを狩るクイーン」と呼ばれる理由</h3>
<p>小野夕子最大の魅力は、圧倒的なHカップ爆乳と、どんな男性も快楽で骨抜きにしてしまう連続ご奉仕にある。</p>

<h3>2. 【神作厳選】小野夕子の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『FALENO最乳Hカップ痴女お姉さん小野夕子のザーメン狩り40本番12時間ベスト』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">小野夕子のザーメン狩り40本番！Hカップ爆乳で精子を搾り尽くす12時間超大ボリュームの永久保存版ベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1fcdss00061&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでザーメン狩り40本番12時間ベストを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『エグい程の快感でチクイキ射精させるチク活痴女 小野夕子』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">チク活で乳首絶頂！小野夕子がHカップ胸と指先で乳首を攻め立て、男性をチクイキ射精へ導く大ヒット作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1dldss00355&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでチク活痴女チクイキ射精を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>小野夕子</td></tr>
    <tr><td>所属メーカー</td><td>FALENO（ファレノ）</td></tr>
    <tr><td>主要属性</td><td>独占配信・Hカップ・爆乳・痴女・ザーメン狩り・単体作品</td></tr>
    <tr><td>胸・Hカップ度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>痴女ご奉仕・搾精</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>小野夕子は、Hカップ爆乳と圧倒的な搾精ご奉仕で全男を骨抜きにする最高の女優。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/1fcdss00061/1fcdss00061pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=1fcdss00061/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/1fcdss00061/1fcdss00061jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1fcdss00061&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "Hカップ", "爆乳", "痴女", "単体作品"],
    "actresses": ["小野夕子"],
    "maker": "ファレノ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "小野夕子", "ファレノ", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
