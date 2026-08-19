import json
import os

# 1. 女優特集: 深田えいみ
p1 = {
    "id": "feature-fukada-eimi-v2",
    "hinban": "SPECIAL-FUKADAEIMI-V2",
    "title": "【2026年最新版】深田えいみ インフルエンサー女王＆FALENOSNS直前生配信！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】SNSフォロワー数No.1女王！『深田えいみ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>SNSフォロワー数圧倒的日本一、美容・YouTube・タレントとしても全世代から注目を集めるAV界のカリスマ女王<strong>『深田えいみ』</strong>。「深田えいみ おすすめ」「深田えいみ SNS生配信」「深田えいみ FALENO」「深田えいみ 限界羞恥」「深田えいみ 単体」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の圧倒的スター性と最新作の過激エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 深田えいみが「時代を象徴するカリスマ」と呼ばれる理由</h3>
<p>深田えいみ最大の魅力は、洗練された圧倒的ルックスと、作品ごとに魅せる本気の体当たり演技、男心を完璧に理解したあざと可愛いご奉仕にある。</p>

<h3>2. 【神作厳選】深田えいみの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『AV初の限界羞恥！SEX直前5秒前までSNSで生配信 深田えいみ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">AV史上の限界突破！SEX直前5秒前までSNSで生配信！恥ずかしさのあまり全身が敏感クリトリスと化す、深田えいみ最新最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1fsdss00686&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでSEX直前SNS生配信作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>深田えいみ</td></tr>
    <tr><td>所属メーカー</td><td>FALENO（ファレノ） / Premium</td></tr>
    <tr><td>主要属性</td><td>独占配信・カリスマ・SNSNo.1・限界羞恥・単体作品</td></tr>
    <tr><td>ルックス・知名度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>あざとさ・表現力</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>深田えいみは、全世代から愛されるAV界の絶対的カリスマ女王。ぜひ彼女の最新代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/1fsdss00686/1fsdss00686pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=1fsdss00686/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/1fsdss00686/1fsdss00686jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1fsdss00686&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "カリスマ", "SNSNo.1", "限界羞恥", "単体作品"],
    "actresses": ["深田えいみ"],
    "maker": "ファレノ",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "深田えいみ", "ファレノ", "SEO特化"]
}

# 2. 女優特集: 本郷愛
p2 = {
    "id": "feature-hongo-ai-v2",
    "hinban": "SPECIAL-HONGOAI-V2",
    "title": "【2026年最新版】本郷愛 国宝級顔面＆S1全19作引退コンプリートBOX！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】国宝級の美貌＆S1全19作コンプリート！『本郷愛』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>誰もが息をのむ国宝級の顔面美貌、完璧なスタイル、そしてS1およびFALENOの絶対的エースとして世界中のファンを魅了したトップ女優<strong>『本郷愛』</strong>。「本郷愛 おすすめ」「本郷愛 S1全19作引退BOX」「本郷愛 顔面特化VR」「本郷愛 友達SEX」「本郷愛 FALENO16時間」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の神がかった美貌と極上エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 本郷愛が「顔面国宝」として世界のファンを魅了する理由</h3>
<p>本郷愛最大の魅力は、世界水準で美しい顔立ちと、至近距離で相手を愛おしそうに見つめながら行う濃密なご奉仕にある。</p>

<h3>2. 【神作厳選】本郷愛の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『本郷愛 引退 S1全19作コンプリート 15時間BOX』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">S1での奇跡の全記録！本郷愛の全19作品を15時間に完全収録した、ファン永久保存版のメモリアル引退コンプリートBOX！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dofje00593&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでS1全19作引退コンプリート15時間BOXを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『【VR】可愛い、優しい、エロい。至近距離で見つめながらご奉仕 【顔面特化】 本郷愛』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">本郷愛の顔面美貌を至近距離で独占！じ～っくり見つめられながら即尺口淫を受ける、最高の顔面特化主観VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsivr00331&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで顔面特化至近距離ご奉仕VRを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">③『本郷愛 FALENOセックスクイーンの軌跡16時間ベスト』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">FALENOでの輝かしい軌跡！本郷愛の極上セックスシーンを16時間贅沢に凝縮した、ファン永久保存版のメモリアルベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1fcdss00043&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでFALENO16時間ベストを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>本郷愛</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン） / FALENO</td></tr>
    <tr><td>主要属性</td><td>独占配信・顔面国宝・S1引退BOX・VR・単体作品</td></tr>
    <tr><td>顔面美貌・国宝級</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>愛嬌・ご奉仕</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>本郷愛は、国宝級の美貌と最高の愛嬌でファンを魅了した至高のヒロイン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ofje00593/ofje00593pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ofje00593/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ofje00593/ofje00593jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dofje00593&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "顔面国宝", "S1引退BOX", "VR", "単体作品"],
    "actresses": ["本郷愛"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "本郷愛", "S1", "SEO特化"]
}

# 3. 女優特集: 西宮ゆめ
p3 = {
    "id": "feature-nishimiya-yume-v2",
    "hinban": "SPECIAL-NISHIMIYAYUME-V2",
    "title": "【2026年最新版】西宮ゆめ 圧倒的スタイル＆1st VR BEST！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】最高級スタイリッシュ美貌＆1st VR BEST！『西宮ゆめ』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>モデル顔負けのスレンダー美脚スタイル、透明感溢れるルックス、そしてアイデアポケット専属として数々のヒット作を飛ばす人気女優<strong>『西宮ゆめ』</strong>。「西宮ゆめ おすすめ」「西宮ゆめ 1st VR BEST」「西宮ゆめ 別れさせ屋」「西宮ゆめ 保育園先生アプリ」「西宮ゆめ 泥酔おかわり」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女のスタイリッシュな美貌と濃密エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 西宮ゆめが「スタイリッシュ美貌の最高峰」として愛される理由</h3>
<p>西宮ゆめ最大の魅力は、脚長スレンダーな完璧プロポーションと、ドラマ作品で見せる小悪魔的かつ情熱的な演技力にある。</p>

<h3>2. 【神作厳選】西宮ゆめの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【VR】西宮ゆめ 1st VR BEST 最高級画質と最先端画角でお届け 西宮ゆめ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">西宮ゆめのVRの全魅力！最高級画質と最先端画角で彼女の美しいプロポーションとエロスを体感する、ファン必携の1st VR BEST！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dipvr00113&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで1st VR BESTを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『成功率100％の別れさせ屋の凄腕テク美女が返り討ち！？ 西宮ゆめ』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">凄腕の別れさせ屋・西宮ゆめが返り討ちに遭い、イカされまくって完堕ち！プロの女が快楽に負ける圧巻の大ヒット名作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dipzz00892&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで別れさせ屋返り討ち作を見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>西宮ゆめ</td></tr>
    <tr><td>所属メーカー</td><td>IDEAPOCKET（アイデアポケット）</td></tr>
    <tr><td>主要属性</td><td>独占配信・スレンダー・美脚・1st VR BEST・単体作品</td></tr>
    <tr><td>スタイル・美脚</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>演技力・小悪魔感</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>西宮ゆめは、スタイリッシュな美貌と濃密な演技でファンを熱狂させるアイデアポケット最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/ipvr00113/ipvr00113pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=ipvr00113/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/ipvr00113/ipvr00113jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dipvr00113&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "スレンダー", "美脚", "1st VR BEST", "単体作品"],
    "actresses": ["西宮ゆめ"],
    "maker": "アイデアポケット",
    "date": "2026-08-19 00:00:00",
    "labels": ["女優特集", "西宮ゆめ", "アイデアポケット", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
