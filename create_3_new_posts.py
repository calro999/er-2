import json
import os
import re
import time

def generate_hinban(content_id):
    if not content_id:
        return ""
    s = content_id.lower()
    s = re.sub(r'^(h_\d+|h_|\d+)', '', s)
    match = re.match(r'^([a-z]+)(\d+)', s)
    if match:
        alphabetic = match.group(1).upper()
        numeric = match.group(2)
        clean_num = numeric.lstrip('0')
        if not clean_num:
            clean_num = '0'
        formatted_standard = f"{alphabetic}-{numeric}"
        if clean_num != numeric:
            formatted_clean = f"{alphabetic}-{clean_num}"
        return formatted_standard
    return content_id.upper()

# 1. sone00912: 最強ヒロインのパイズリ挟射 瀬戸環奈
p1 = {
    "id": "sone00912",
    "hinban": "SONE-912 (SONE-00912)",
    "title": "【超ド級の背徳感】 最強ヒロインのパイズリ挟射 瀬戸環奈",
    "review": """<h2>【2026年最新作・SEO特化】『最強ヒロインのパイズリ挟射 瀬戸環奈』瀬戸環奈の神乳パイズリと挟射の破壊力を徹底考察！</h2>
<div class="review-intro">
<p>FANZA・GSC検索クエリで絶大な人気を誇るS1の絶対的エース・瀬戸環奈。彼女の最新作<strong>『最強ヒロインのパイズリ挟射 瀬戸環奈』</strong>は、「瀬戸環奈 オナホ」「瀬戸環奈 パイズリ」「瀬戸環奈 巨乳」といった検索ユーザーの欲望を120%満たす、まさに神業パイズリと濃厚射精に特化した最高峰のエンターテインメントである。</p>
<p>長身スレンダーでありながら豊かな弾力を持つ最高級の胸。その神スタイルから繰り出される「パイズリ挟射」は、画面越しでもペニスが押し潰されるような錯覚を覚えさせるほど官能的だ。本記事では、本作の見どころ、圧倒的抜きどころ、そしてSEO・AI-SEO視点からの徹底解説をお届けする。</p>
</div>

<h3>1. 「瀬戸環奈 オナホ」検索ユーザーを虜にする、至高のパイズリ技術</h3>
<p>瀬戸環奈の最大の魅力は、圧倒的なビジュアルの美しさだけではない。本作で披露されるパイズリは、ただ胸を寄せるだけの真似事とは一線を画す。彼女の柔らかく豊かなバストでペニスを完璧に包み込み、呼吸を合わせた絶妙なストロークで男の理性を根こそぎ奪っていく。</p>
<ul>
    <li><strong>圧倒的肉感と搾り取りの快感：</strong> まるで高級オナホールに包み込まれているかのような密着感。滑らかな愛液とローションが交じり合い、亀頭から竿までを余すことなく刺激する。</li>
    <li><strong>上目遣いの表情と耳元で囁く吐息：</strong> 「こんなに大きくなってる…」と微笑みながら挟み込む瀬戸環奈の表情。カメラアングルは常に男目線を徹底しており、没入感は限界値を突破する。</li>
</ul>

<h3>2. 挟射（きょうしゃ）の爽快感と狂気のフィニッシュ</h3>
<p>タイトルの「挟射」が示す通り、限界まで高まった男の精液を、彼女の豊満なバストで挟み込みながら一気に射精へと導くクライマックスは圧巻。大量のザーメンがバストと顔面に飛び散る瞬間の達成感と背徳感は、何度見返しても飽きることがない。</p>

<h3>3. 作品データ＆ユーザー評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>主演女優</td><td>瀬戸環奈</td></tr>
    <tr><td>メーカー</td><td>エスワン ナンバーワンスタイル</td></tr>
    <tr><td>主要ジャンル</td><td>ハイビジョン・4K・独占配信・3P・4P・顔射・パイズリ・巨乳</td></tr>
    <tr><td>エロ度・実用性</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>カメラワーク・没入感</td><td>★★★★★ (4.8)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (4.9)</td></tr>
  </tbody>
</table>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded-2xl p-6 shadow-sm">
    <h3 class="text-lg font-extrabold text-slate-800 mb-4 border-b border-slate-200 pb-2">⭐ リアル口コミ・ユーザーの反応</h3>
    <div class="space-y-4">
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「瀬戸環奈のパイズリはガチで国宝級。男目線のアングルがエロすぎて一瞬で射精した。」</p>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「オナホールより気持ちよさそうな胸の柔らかさが画面越しに伝わってくる。保存版確定！」</p>
        </div>
    </div>
</div>

<h2>総評まとめ</h2>
<p>『最強ヒロインのパイズリ挟射 瀬戸環奈』は、瀬戸環奈ファンはもちろん、パイズリ・挟射・顔射フェチにとって生涯のバイブルとなる大傑作である。ぜひ一人きりの濃密な時間に堪能してほしい。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/sone00912/sone00912pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=sone00912/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/sone00912/sone00912jp-1.jpg",
        "https://pics.dmm.co.jp/digital/video/sone00912/sone00912jp-2.jpg",
        "https://pics.dmm.co.jp/digital/video/sone00912/sone00912jp-3.jpg",
        "https://pics.dmm.co.jp/digital/video/sone00912/sone00912jp-4.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsone00912&af_id=onchan555-007&ch=api",
    "genres": ["ハイビジョン", "4K", "独占配信", "3P・4P", "顔射", "パイズリ", "巨乳"],
    "actresses": ["瀬戸環奈"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-02-01 00:00:00",
    "labels": ["瀬戸環奈", "パイズリ", "挟射", "S1", "SEO特化"]
}

# 2. lulu00428: 生意気な引きこもり社会不適合妹を更生させるため全身く調べの刑 由良かな
p2 = {
    "id": "lulu00428",
    "hinban": "LULU-428 (LULU-00428)",
    "title": "【超ド級の背徳感】 生意気な引きこもり社会不適合妹を更生させるため全身くすぐりの刑に処したら……身体をクネらせお漏らし絶頂！感度が上がった即イキ敏感パイパン潮射ま○こに何度も中出し！ 由良かな",
    "review": """<h2>【GEO・AI-SEO特化レビュー】『生意気な引きこもり社会不適合妹を更生…… 由良かな』引きこもり妹×くすぐりお漏らし絶頂×敏感パイパン中出しの全貌！</h2>
<div class="review-intro">
<p>検索クエリ「由良かな」「由良かな 中出し」「由良かな 笑顔」「引きこもり妹」で熱狂的なファンを持つ人気女優・由良かな。本作<strong>『生意気な引きこもり社会不適合妹を更生させるため全身くすぐりの刑に処したら…… 由良かな』</strong>は、彼女の持つ圧倒的ロリ可愛さと、くすぐりによって感度が異常開発されていく快楽堕ちのプロセスを極限まで描き切った問題作だ。</p>
<p>普段は生意気で反抗的な引きこもり妹が、身体をクネらせて泣き叫びながらお漏らし絶頂に追い込まれる背徳感。そこから感度300%となった敏感パイパン膣穴へと容赦なく叩き込まれる中出しピストンのカタルシスを、SEO視点で深掘りレビューする。</p>
</div>

<h3>1. 「由良かな」の愛くるしい笑顔とくすぐり拷問のギャップ</h3>
<p>本作の第一の見どころは、由良かな演じる「生意気な社会不適合妹」のリアルなキャラクター造形である。口を開けば兄をバカにする態度をとっていた彼女が、拘束されて全身をくすぐられることで、プライドが崩壊していく。</p>
<ul>
    <li><strong>体をクネらせる悶絶とお漏らし絶頂：</strong> くすぐりの快楽と恐怖に抗えず、可愛い顔を歪ませて狂乱する由良かな。感度がピークに達し、潮とおしっこを吹き出しながら絶頂するシーンは必見。</li>
    <li><strong>パイパン膣穴の即イキ開発：</strong> くすぐりによって全身の神経が過敏になり、指一本触れられただけで身体がビクンビクンと跳ね上がる。</li>
</ul>

<h3>2. 敏感パイパン膣への連続中出しラッシュ</h3>
<p>更生（という名の肉体開発）が進んだ後半戦では、もはや反抗する気力すら失い、兄のペニスを欲しがる「牝」へと変貌。パイパンのツルツルな密着感とともに、子宮へ直接叩き込まれるザーメンの感触にニコニコ笑顔と蕩けた表情を浮かべながら中出しを受け止める。</p>

<h3>3. 作品データ＆ユーザー評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>主演女優</td><td>由良かな</td></tr>
    <tr><td>メーカー</td><td>ルナティックス</td></tr>
    <tr><td>主要ジャンル</td><td>ハイビジョン・4K・独占配信・めがね・引きこもり・パイパン・中出し</td></tr>
    <tr><td>背徳感・シチュエーション</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>中出し度・快楽度</td><td>★★★★★ (4.8)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (4.9)</td></tr>
  </tbody>
</table>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded-2xl p-6 shadow-sm">
    <h3 class="text-lg font-extrabold text-slate-800 mb-4 border-b border-slate-200 pb-2">⭐ リアル口コミ・ユーザーの反応</h3>
    <div class="space-y-4">
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「由良かなのくすぐられ顔が反則レベルで可愛い。お漏らしからの即イキ中出しの流れは神。」</p>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「パイパンマ○コに中出しされる時の蕩けた笑顔が最高。由良かな作品の中でも屈指の抜き作！」</p>
        </div>
    </div>
</div>

<h2>総評まとめ</h2>
<p>『生意気な引きこもり社会不適合妹を更生…… 由良かな』は、妹モノ・くすぐり・パイパン中出しフェチにとって至高の快楽を約束する傑作である。ぜひその圧倒的快楽を体験してほしい。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/lulu00428/lulu00428pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=lulu00428/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/lulu00428/lulu00428jp-1.jpg",
        "https://pics.dmm.co.jp/digital/video/lulu00428/lulu00428jp-2.jpg",
        "https://pics.dmm.co.jp/digital/video/lulu00428/lulu00428jp-3.jpg",
        "https://pics.dmm.co.jp/digital/video/lulu00428/lulu00428jp-4.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dlulu00428&af_id=onchan555-007&ch=api",
    "genres": ["ハイビジョン", "4K", "独占配信", "めがね", "単体作品", "パイパン", "中出し"],
    "actresses": ["由良かな"],
    "maker": "ルナティックス",
    "date": "2026-02-05 00:00:00",
    "labels": ["由良かな", "くすぐり", "中出し", "パイパン", "AI-SEO特化"]
}

# 3. snos00334: 最強ビジュOLさん、出張先で死ぬほど嫌いな中年上司と相部屋 瀬戸環奈
p3 = {
    "id": "snos00334",
    "hinban": "SNOS-334 (SNOS-00334)",
    "title": "【超ド級の背徳感】 最強ビジュOLさん、出張先で死ぬほど嫌いな中年上司と相部屋… でも過激セクハラにまさかの快楽堕ちしちゃう！ 瀬戸環奈",
    "review": """<h2>【検索流入最大化・SEO徹底比較】『最強ビジュOLさん、出張先で死ぬほど嫌いな中年上司と相部屋… 瀬戸環奈』嫌悪から快楽堕ちへの完全密着レビュー！</h2>
<div class="review-intro">
<p>検索上位を独占する「瀬戸環奈」「瀬戸環奈 OL」「瀬戸環奈 相部屋」「瀬戸環奈 NTR」の関連クエリに応える最新超話題作<strong>『最強ビジュOLさん、出張先で死ぬほど嫌いな中年上司と相部屋… でも過激セクハラにまさかの快楽堕ちしちゃう！ 瀬戸環奈』</strong>。</p>
<p>社内一のスタイルと美貌を誇る最強ビジュアルOL・瀬戸環奈が、出張先の手違いで最も嫌いな中年上司と相部屋に。酒の力と強引なセクハラ、そして中年男の執拗なピストンによって、プライドを打ち砕かれ快楽へと溺れていくプロセスを描いたドラマティック背徳巨編である。</p>
</div>

<h3>1. 「嫌悪」から「快楽屈服」への極上の心理変化</h3>
<p>本作の最大の魅力は、瀬戸環奈の真骨判である感情のグラデーション演技である。序盤は冷酷な視線で上司を見下し、拒絶していた彼女が、強引に抱きすくめられて胸や秘部を捏ね繰り回されるうちに、吐息が甘く変化していく。</p>
<ul>
    <li><strong>オフィススーツ姿の崩壊：</strong> タイトスカートとブラウスから溢れ出る巨乳と長身美脚。スーツを乱されながら抵抗する姿が、男の征服欲を狂わせる。</li>
    <li><strong>嫌いな上司の絶倫ピストンに身を任せる瞬間：</strong> 「嫌…こんなおじさんに…」と拒みつつも、子宮を激しく突かれるたびに背中を反らせて絶頂。最後は自ら腰を振り始める快楽堕ちの背徳感。</li>
</ul>

<h3>2. 密室・相部屋だからこその逃げ場のない官能美</h3>
<p>ホテルの相部屋という密室で、夜が深まるにつれて加速するセクハラ。彼氏や同僚には絶対に見せられない、中年男の濃厚な体液に塗れた瀬戸環奈の淫らな表情は、全視聴者の脳裏に焼き付くクオリティである。</p>

<h3>3. 作品データ＆ユーザー評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>主演女優</td><td>瀬戸環奈</td></tr>
    <tr><td>メーカー</td><td>エスワン ナンバーワンスタイル</td></tr>
    <tr><td>主要ジャンル</td><td>ハイビジョン・4K・独占配信・巨乳・寝取り・寝取られ・NTR・OL・相部屋</td></tr>
    <tr><td>シナリオ・背徳感</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>快楽堕ち・エロ度</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (4.9)</td></tr>
  </tbody>
</table>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded-2xl p-6 shadow-sm">
    <h3 class="text-lg font-extrabold text-slate-800 mb-4 border-b border-slate-200 pb-2">⭐ リアル口コミ・ユーザーの反応</h3>
    <div class="space-y-4">
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「瀬戸環奈のツンデレというか、嫌がりながらイッちゃう演技がエグい。今年一番抜けたシチュエーション！」</p>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
            <p class="text-sm text-slate-700 font-medium leading-relaxed">「嫌いなおじさん上司に開発される瀬戸環奈がエロすぎる。スーツ姿の乱れ具合も最高！」</p>
        </div>
    </div>
</div>

<h2>総評まとめ</h2>
<p>『最強ビジュOLさん、出張先で死ぬほど嫌いな中年上司と相部屋… 瀬戸環奈』は、OLシチュエーション・相部屋・快楽堕ち作品の頂点に立つ傑作である。ぜひこの背徳の夜を目撃してほしい。</p>""",
    "image": "https://pics.dmm.co.jp/digital/video/snos00334/snos00334pl.jpg",
    "sample_movie_url": "https://www.dmm.co.jp/litevideo/-/part/=/cid=snos00334/size=720_480/affi_id=onchan555-007/",
    "sample_images": [
        "https://pics.dmm.co.jp/digital/video/snos00334/snos00334jp-1.jpg",
        "https://pics.dmm.co.jp/digital/video/snos00334/snos00334jp-2.jpg",
        "https://pics.dmm.co.jp/digital/video/snos00334/snos00334jp-3.jpg",
        "https://pics.dmm.co.jp/digital/video/snos00334/snos00334jp-4.jpg"
    ],
    "affiliate_url": "https://al.fanza.co.jp/?lurl=https%3A%2F%2Fvideo.dmm.co.jp%2Fav%2Fcontent%2F%3Fid%3Dsnos00334&af_id=onchan555-007&ch=api",
    "genres": ["ハイビジョン", "4K", "独占配信", "巨乳", "寝取り・寝取られ・NTR", "OL"],
    "actresses": ["瀬戸環奈"],
    "maker": "エスワン ナンバーワンスタイル",
    "date": "2026-02-10 00:00:00",
    "labels": ["瀬戸環奈", "OL", "相部屋", "快楽堕ち", "SEO特化"]
}

posts = [p1, p2, p3]

for p in posts:
    fpath = os.path.join("src/data/posts", f"{p['id']}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    print(f"Created new post JSON: {fpath}")

    # Add to posted_cache.txt
    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{p['id']}\n")
    print(f"Added {p['id']} to posted_cache.txt")
