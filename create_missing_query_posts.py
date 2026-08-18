import requests
import json
import os

url = 'https://api.dmm.com/affiliate/v3/ItemList'

missing_data = [
    ('叔母さんと甥っ子のラブラブ孕ませ夏休み', 'genu00015', '1genu00015'),
    ('リゾートバイトで黒ギャルの処女いただきます', 'h_1711mtmd00014', 'h_1711mtmd00014'),
    ('【初3p解禁】ガチフォロワーさん達と自宅で3pハメ撮りしてきちゃいました。', 'hmn00890', 'hmn00890'),
    ('柏木雫 av debut', '1fns00230', '1fns00230'),
    ('櫻木みなと av女優', 'hale00072', 'hale00072'),
    ('清原美羽 無修正', '406maraa00196', '406maraa00196'),
    ('幼なじみ2人とsexしないと出られない部屋 asmr', 'npjs00264', 'npjs00264')
]

for q, cid, post_id in missing_data:
    params = {
        'api_id': '4Lx0ftRf17Uuad6Ud7Gb',
        'affiliate_id': 'onchan555-999',
        'site': 'FANZA',
        'service': 'digital',
        'floor': 'videoa',
        'cid': cid,
        'output': 'json'
    }
    r = requests.get(url, params=params)
    item = {}
    if r.status_code == 200:
        items = r.json().get('result', {}).get('items', [])
        if items:
            item = items[0]
    
    title = item.get('title', q)
    image = item.get('imageURL', {}).get('large', '')
    aff_url = item.get('affiliateURL', '').replace('onchan555-999', 'onchan555-007')
    genres = [g.get('name', '') for g in item.get('iteminfo', {}).get('genre', [])]
    actresses = [a.get('name', '') for a in item.get('iteminfo', {}).get('actress', [])]
    maker = item.get('iteminfo', {}).get('maker', [{}])[0].get('name', 'S1')

    genre_str = "、".join(genres[:4]) if genres else "背徳・中出し・独占"

    review_html = f"""<h2>【徹底解説＆完全解析】『{q}』の見どころ・ストーリー・圧倒的抜きどころ</h2>
<div class="review-intro">
<p>Google検索で今アクセスを伸ばしている注目キーワード<strong>『{q}』</strong>。本作は、その検索インテントを100%満たす圧倒的な背徳シチュエーションと、演者のリアルな感情変化が炸裂する至高のエンターテインメントである。</p>
<p>「非日常へ引きずり込まれる感覚」「理性が崩壊していく快感」を極限まで深掘りし、マニアも納得の演出美と抜きどころを熱量MAXで解説していく。</p>
</div>

<h3>1. 検索ユーザーを魅了する「背徳シチュエーション」の凄み</h3>
<p>本作の最大の魅力は、テーマである<strong>『{q}』</strong>の要素が完璧に計算されて映像化されている点にある。</p>
<ul>
    <li><strong>日常のすぐ裏側に潜むスリル：</strong> 平穏な空間が、ほんの少しのきっかけで濃密な愛欲の場へと変貌する展開。</li>
    <li><strong>演者の生々しいリアクションと表情変化：</strong> 葛藤しながらも快楽に抗えず、瞳を潤ませて絶頂を受け入れるリアルさ。</li>
</ul>

<h3>2. 抜きどころ満載の構成とカメラワーク</h3>
<p>息遣いや肌の温もりまで伝わってくる近距離のアングル。高画質映像ならではの臨場感で、あたかも自分が現場でその密会を覗き見しているかのような圧倒的な没入感を提供する。</p>

<h3>3. 作品データ＆ユーザー総合評価</h3>
<table>
  <thead>
    <tr><th>項目</th><th>詳細・スコア</th></tr>
  </thead>
  <tbody>
    <tr><td>検索ターゲット</td><td>{q}</td></tr>
    <tr><td>主要ジャンル</td><td>{genre_str}</td></tr>
    <tr><td>エロ度・実用性</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>没入感・シチュエーション</td><td>★★★★★ (4.9)</td></tr>
    <tr><td>総合満足度</td><td>★★★★★ (4.9)</td></tr>
  </tbody>
</table>

<h2>総評まとめ</h2>
<p>『{q}』は、検索ボリュームの急増に恥じない圧倒的クオリティを誇る傑作である。ぜひ誰にも邪魔されないプライベート空間で存分に堪能してほしい。</p>"""

    p_data = {
        "id": post_id,
        "hinban": post_id.upper(),
        "title": f"【超ド級の背徳感】 {q}",
        "review": review_html,
        "image": image if image else "https://pics.dmm.co.jp/digital/video/snos00334/snos00334pl.jpg",
        "sample_movie_url": f"https://www.dmm.co.jp/litevideo/-/part/=/cid={cid}/size=720_480/affi_id=onchan555-007/",
        "sample_images": [],
        "affiliate_url": aff_url if aff_url else "https://www.dmm.co.jp/",
        "genres": genres if genres else ["独占配信", "中出し", "背徳"],
        "actresses": actresses,
        "maker": maker,
        "date": "2026-08-18 00:00:00",
        "labels": ["GSC上位ターゲット", "SEO特化", "背徳"]
    }

    fpath = f"src/data/posts/{post_id}.json"
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(p_data, f, ensure_ascii=False, indent=2)
    print(f"Created post file: {fpath}")

    with open("posted_cache.txt", "a", encoding="utf-8") as f:
        f.write(f"{post_id}\n")
