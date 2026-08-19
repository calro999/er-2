import json
import os

# 1. 女優特集: 相沢みなみ
p1 = {
    "id": "feature-aizawa-minami-v2",
    "hinban": "SPECIAL-AIZAWAMINAMI-V2",
    "title": "【2026年最新版】相沢みなみ 奇跡のシンデレラ＆引退48時間コンプリート！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】奇跡のシンデレラ女王！『相沢みなみ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>誰もが息をのむ透明感溢れる美貌、誰からも愛されたプロ意識、そしてFANZA AWARDグランプリを獲得しアイデアポケットのトップとしてAV界に君臨した絶対的ヒロイン<strong>『相沢みなみ』</strong>。「相沢みなみ おすすめ」「相沢みなみ 引退48時間BOX」「相沢みなみ アイポケ」「相沢みなみ グランプリ」「相沢みなみ 完全コンプリート」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の神がかったスター性と輝かしい名作が凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 相沢みなみが「シンデレラ女王」として愛され続ける理由</h3>
<p>相沢みなみ最大の魅力は、圧倒的な美貌と、ファンのために全力を尽くす真摯で情熱的なご奉仕精神にある。</p>

<h3>2. 【神作厳選】相沢みなみの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『相沢みなみ 引退 COMPLETE BEST 48時間BOX』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">相沢みなみの全歴史と輝き！彼女のすべての名作と感動を48時間に凝縮した、ファン永久保存版のメモリアルコンプリートBOX！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dipok00007&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで引退48時間コンプリートBOXを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>相沢みなみ</td></tr>
    <tr><td>所属メーカー</td><td>IDEAPOCKET（アイデアポケット）</td></tr>
    <tr><td>主要属性</td><td>独占配信・シンデレラ・グランプリ・引退48時間・単体作品</td></tr>
    <tr><td>美貌・スター性</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>愛嬌・感動</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>相沢みなみは、完璧な美貌と誠実な愛しさで全ファンを夢中にさせた至高のヒロイン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ipok00007/ipok00007pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ipok00007/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ipok00007/ipok00007jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dipok00007&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "シンデレラ", "グランプリ", "引退48時間", "単体作品"],
    "actresses": ["相沢みなみ"],
    "maker": "アイデアポケット",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "相沢みなみ", "アイデアポケット", "SEO特化"]
}

# 2. 女優特集: 三上悠亜
p2 = {
    "id": "feature-mikami-yua-v2",
    "hinban": "SPECIAL-MIKAMIYUA-V2",
    "title": "【2026年最新版】三上悠亜 国民的アジアの女神＆最高の愛人沼！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】アジアを席巻した絶対女王！『三上悠亜』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>国民的アイドルグループ出身の圧倒的スター性、全世界に熱狂的ファンを持つアジアの女神、そしてS1の頂点として一時代を創り上げた伝説の女優<strong>『三上悠亜』</strong>。「三上悠亜 おすすめ」「三上悠亜 最高の愛人沼」「三上悠亜 S1専属」「三上悠亜 国民的アイドル」「三上悠亜 秘宝」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の華やかな美貌と極上エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 三上悠亜が「全アジアのアイコン」として君臨する理由</h3>
<p>三上悠亜最大の魅力は、誰しもを釘付けにする圧倒的アイドルオーラと、男が一番欲しがる最高の愛人シチュエーションの完成度にある。</p>

<h3>2. 【神作厳選】三上悠亜の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『最高の愛人沼 仕事にも家庭にも干渉してこないSEXだけの理想関係 三上悠亜』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">全男の憧れ！三上悠亜が最高の愛人になってSEXだけの理想関係を愉しむ、甘く溺れる至高の愛人沼神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssis00338&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで最高の愛人沼を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>三上悠亜</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・国民的・アジアの女神・愛人沼・S1専属・単体作品</td></tr>
    <tr><td>オーラ・スター性</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>愛人感・多幸感</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>三上悠亜は、全アジアを熱狂させた絶対的アイコン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ssis00338/ssis00338pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ssis00338/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ssis00338/ssis00338jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssis00338&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "国民的", "アジアの女神", "愛人沼", "単体作品"],
    "actresses": ["三上悠亜"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "三上悠亜", "S1", "SEO特化"]
}

# 3. 女優特集: 坂道みる
p3 = {
    "id": "feature-sakamichi-miru-v2",
    "hinban": "SPECIAL-SAKAMICHIMIRU-V2",
    "title": "【2026年最新版】坂道みる 圧倒的才能＆大量潮吹きオーガズム！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】驚異の感度＆潮吹き天才ヒロイン！『坂道みる』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>可憐な美少女スマイル、デビュー直後から天才と称された圧倒的な感度、そして大量潮吹きオーガズムでファンを魅了するS1看板女優<strong>『坂道みる』</strong>。「坂道みる おすすめ」「坂道みる 大量潮吹き」「坂道みる 激イキ193回」「坂道みる ド痴女メンズエステ」「坂道みる ノンストップ本気性交」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の天才的感度と爆発的エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 坂道みるが「潮吹きの天才」と呼ばれる理由</h3>
<p>坂道みる最大の魅力は、ピュアな顔立ちからは想像もつかない激しい絶頂反応と、追撃ピストンで溢れ出す大量の潮吹きにある。</p>

<h3>2. 【神作厳選】坂道みるの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『快感潮吹き絶頂マ●コを追撃ピストンでひたすら大量潮吹きオーガズム 坂道みる』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">潮吹きの天才・坂道みるが追撃ピストンで限界突破！ひたすら大量の潮を吹き出しながら絶頂しまくる大興奮神作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssni00608&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで大量潮吹きオーガズム作を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『激イキ193回！痙攣4700回！イキ潮10000cc！エロス覚醒 坂道みる』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">驚異の数字が証明する伝説作！激イキ193回・痙攣4700回・イキ潮10000cc！坂道みるのエロスが完全覚醒した大ヒット名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssni00353&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで激イキ193回エロス覚醒を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">③『中身はド痴女 精巣空っぽにしてくれるドスケベ淫語メンズエステ 坂道みる』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">見た目は清楚、中身はド痴女！坂道みるが淫語と凄テクで精巣を空っぽにするまで責め立てる至高のメンズエステ作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssis00005&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでド痴女淫語メンズエステを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>坂道みる</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン）</td></tr>
    <tr><td>主要属性</td><td>独占配信・天才感度・潮吹き・ド痴女・メンズエステ・単体作品</td></tr>
    <tr><td>可愛さ・ルックス</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>潮吹き・絶頂感度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>坂道みるは、天才的な感度と圧倒的な潮吹きで全男を驚愕させるS1最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ssni00608/ssni00608pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ssni00608/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ssni00608/ssni00608jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dssni00608&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "天才感度", "潮吹き", "ド痴女", "単体作品"],
    "actresses": ["坂道みる"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "坂道みる", "S1", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
