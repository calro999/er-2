import json
import os

# 1. 女優特集: 水野朝陽
p1 = {
    "id": "feature-mizuno-asahi-v2",
    "hinban": "SPECIAL-MIZUNOASAHI-V2",
    "title": "【2026年最新版】水野朝陽 圧倒的ボーイッシュ美貌＆超高級ソープ3日間！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/AI-SEO/GEO徹底対応】ボーイッシュ極上美貌＆絶対的エース！『水野朝陽』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>ショートカットが映える圧倒的ボーイッシュ美貌、高身長スレンダーなスタイル、そしてS1やエスワンの看板としてAV界を魅了した伝説のヒロイン<strong>『水野朝陽』</strong>。「水野朝陽 おすすめ」「水野朝陽 超高級ソープ3日間」「水野朝陽 AIリマスター」「水野朝陽 真グラマー仮面」「水野朝陽 ショートカット」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の唯一無二のクール＆スレンダー美貌と濃密エロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 水野朝陽が「ボーイッシュ美貌の最高峰」と呼ばれる理由</h3>
<p>水野朝陽最大の魅力は、キリッとした美しい顔立ちと、性交中に魅せる本気の熱い吐息・素直な絶頂感度のギャップにある。</p>

<h3>2. 【神作厳選】水野朝陽の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【AIリマスター】3日間滞在して、寝食を共にする超高級美女ソープ 水野朝陽』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">AIリマスター超高画質！水野朝陽と3日間ずっと一緒！寝食を共にして極上ご奉仕を受けまくるファン感涙の最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1iene00349h&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで超高級ソープ3日間AIリマスターを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>水野朝陽</td></tr>
    <tr><td>所属メーカー</td><td>S1 NO.1 STYLE（エスワン） / アイエナ</td></tr>
    <tr><td>主要属性</td><td>独占配信・ボーイッシュ・ショートカット・超高級ソープ・AIリマスター・単体作品</td></tr>
    <tr><td>クール美貌・スタイル</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>ご奉仕・感度</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>水野朝陽は、クールな美貌と熱いご奉仕で全男を魅了する至高のヒロイン。ぜひ彼女の代表作を今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/1iene00349h/1iene00349hpl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=1iene00349h/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/1iene00349h/1iene00349hjp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1iene00349h&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "ボーイッシュ", "ショートカット", "超高級ソープ", "単体作品"],
    "actresses": ["水野朝陽"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-08-25 00:00:00",
    "labels": ["女優特集", "水野朝陽", "S1", "SEO特化"]
}

# 2. 女優特集: 日向ゆず
p2 = {
    "id": "feature-hinata-yuzu-v2",
    "hinban": "SPECIAL-HINATAYUZU-V2",
    "title": "【2026年最新版】日向ゆず 極ほん本番＆大人の保育園！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・SEO/GEO徹底対応】ロリータキュート＆極ほん本番！『日向ゆず（ゆずは）』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>可憐でキュートなルックス、愛嬌たっぷりの笑顔、そして極ほんシリーズやプライベートモードで絶大な人気を誇るトップ女優<strong>『日向ゆず（日向ゆず葉）』</strong>。「日向ゆず おすすめ」「日向ゆず 極ほん本番」「日向ゆず 大人の保育園」「日向ゆず 69時間ベスト」「日向ゆず Private Mode」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の愛くるしい魅力と本気のエロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 日向ゆずが「ロリータ可愛さの最高峰」として愛される理由</h3>
<p>日向ゆず最大の魅力は、小柄でキュートな可愛らしさと、本気の本番性交で見せる無防備な表情にある。</p>

<h3>2. 【神作厳選】日向ゆずの絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『極[ごくほん]本番 日向ゆず葉』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">一切の妥協なし！日向ゆず葉が本気の本番性交に挑む、ファン歓喜の極ほん本番シリーズ最高傑作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D12gon00248&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAで極ほん本番 日向ゆず葉を見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『Tokyo Private Mode 007 ［ゆずは］』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">完全プライベート密着！ゆずはの自然体な笑顔とプライベート空間での生々しいエロスを堪能する大人気作！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D504mod00007&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでTokyo Private Mode ゆずはを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>日向ゆず（日向ゆず葉）</td></tr>
    <tr><td>所属メーカー</td><td>ゴンゾ / マイクロ / プレステージ</td></tr>
    <tr><td>主要属性</td><td>ロリータ・極ほん・本番・プライベートモード・単体作品</td></tr>
    <tr><td>可愛さ・愛嬌</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>本番感度・リアル</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>日向ゆずは、キュートなルックスと本気の本番エロスでファンを魅了する最高のヒロイン。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/12gon00248/12gon00248pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=12gon00248/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/12gon00248/12gon00248jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D12gon00248&af_id=onchan555-007&ch=api",
    "genres": ["ロリータ", "極ほん", "本番", "プライベートモード", "単体作品"],
    "actresses": ["日向ゆず"],
    "maker": "ゴンゾ",
    "date": "2026-08-25 00:00:00",
    "labels": ["女優特集", "日向ゆず", "ゴンゾ", "SEO特化"]
}

# 3. 女優特集: 戸田真琴
p3 = {
    "id": "feature-toda-makoto-v3",
    "hinban": "SPECIAL-TODAMAKOTO-V3",
    "title": "【2026年最新版】戸田真琴 SODVR1000作品記念＆4周年8時間BEST！絶対見るべき神作・おすすめ名作まとめ特集",
    "review": """<h2>【2026年最新・AI-SEO/GEO徹底対応】SOD最高峰ヒロイン＆究極3P VR！『戸田真琴』の絶対見るべき神作・おすすめ名作完全攻略ガイド</h2>
<div class="review-intro">
<p>愛くるしいルックス、圧倒的文筆センス、そしてSODstarの歴代最高峰としてVR作品から記念BESTまで大ヒットを連発したレジェンド女優<strong>『戸田真琴』</strong>。「戸田真琴 おすすめ」「戸田真琴 SODVR1000作品記念」「戸田真琴 4周年8時間BEST」「戸田真琴 ベロチュウ誘惑」「戸田真琴 領域展開VR」などの検索インテントに応える完全保存版特集である。</p>
<p>本記事では、彼女の圧倒的ヒロイン性と至高のエロスが凝縮された<b>【絶対に見るべき最高傑作3選】</b>と見どころを徹底解説する。</p>
</div>

<h3>1. 戸田真琴が「SODstarのメモリアルヒロイン」として讃えられる理由</h3>
<p>戸田真琴最大の魅力は、誰からも愛される純粋な笑顔と、VRや3Pなどの特殊企画でも完璧に魅せる表現力の高さにある。</p>

<h3>2. 【神作厳選】戸田真琴の絶対見るべき最高傑作3選</h3>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">①『【VR】SODVR1000作品突破記念スペシャル第4弾！！《領域展開/地面特化×天井特化》究極3P 戸田真琴』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">SODVR1000作品達成記念！戸田真琴が地面特化×天井特化の究極アングルで迫る、超豪華3P最高峰主観VR！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D13dsvr01048&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでSODVR1000作品記念究極3Pを見る</a>
</div>

<div class="my-6 bg-rose-50 border border-rose-200 rounded-2xl p-6 shadow-sm">
    <h4 class="text-xl font-bold text-rose-800 mb-2">②『戸田真琴デビュー4周年 最新23作品23SEX 8時間BEST！！！！』</h4>
    <p class="text-sm text-slate-700 leading-relaxed mb-3">4年間の軌跡！戸田真琴の最新23作品・23SEXを8時間大ボリュームで凝縮した、ファン必携の記念ベスト！</p>
    <a href="https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D1stars00274&af_id=onchan555-007&ch=api" target="_blank" rel="noopener" class="inline-block bg-rose-600 text-white font-bold px-4 py-2 rounded-lg text-sm hover:bg-rose-700 transition">▶ FANZAでデビュー4周年23SEX 8時間BESTを見る</a>
</div>

<h3>3. 女優プロフィール＆総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>女優名</td><td>戸田真琴</td></tr>
    <tr><td>所属メーカー</td><td>SODstar（エスオーディー スター）</td></tr>
    <tr><td>主要属性</td><td>独占配信・文才・SODVR記念・4周年BEST・3P・単体作品</td></tr>
    <tr><td>ヒロイン性・笑顔</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>VR体感・表現力</td><td>★★★★★ (5.0)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (5.0)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>戸田真琴は、透明感あふれる美貌と最高の表現力でファンを熱狂させたSODスター。ぜひ今すぐ体感しよう。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/13dsvr01048/13dsvr01048pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=13dsvr01048/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/13dsvr01048/13dsvr01048jp-1.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3D13dsvr01048&af_id=onchan555-007&ch=api",
    "genres": ["独占配信", "文才", "SODVR記念", "4周年BEST", "単体作品"],
    "actresses": ["戸田真琴"],
    "maker": "SODクリエイト",
    "date": "2026-08-25 00:00:00",
    "labels": ["女優特集", "戸田真琴", "SODstar", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new actress feature post: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
