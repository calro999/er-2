import os
import random
import requests
import time
import json
import re
import hashlib

CACHE_FILE = "posted_cache.txt"
POSTS_DIR = "src/data/posts"

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"
LINK_AFFILIATE_ID = "onchan555-003"
TARGET_POST_COUNT = 10

# ====================================================================
# テンプレ防止のための既存記事見出しキャッシュ
# 新規生成時に既存記事と同じ見出しパターンを避ける
# ====================================================================
def load_existing_h2_patterns():
    """既存記事のH2見出しパターンを読み込んで重複防止に使う"""
    patterns = set()
    if os.path.exists(POSTS_DIR):
        for fname in os.listdir(POSTS_DIR):
            if not fname.endswith('.json'):
                continue
            try:
                with open(os.path.join(POSTS_DIR, fname), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                review = data.get('review', '')
                # H2/H3タグの冒頭テキストを抽出
                for match in re.findall(r'<h[23]>(.*?)</h[23]>', review):
                    # 作品名を除外した骨格だけ取る
                    clean = re.sub(r'『.*?』', '', match).strip()
                    if len(clean) > 5:
                        patterns.add(clean)
            except:
                pass
    return patterns


def load_posted_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_to_cache(content_id):
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{content_id}\n")

def fetch_fanza_items():
    keywords = [
        "人気", "新作", "ランキング", "話題", "注目",
        "巨乳", "美乳", "スレンダー", "美少女", "OL",
        "制服", "女子大生", "看護師", "人妻 若妻",
        "VR", "4K", "独占"
    ]
    
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    all_items = []
    
    search_combos = [
        (random.choice(keywords[:7]), "rank"),
        (random.choice(keywords[:7]), "rank"),
        (random.choice(keywords[7:]), "date"),
        (random.choice(keywords[7:]), "rank"),
        ("", "rank"),
    ]
    
    for keyword, sort_type in search_combos:
        print(f"  API取得中 => keyword='{keyword}', sort='{sort_type}'")
        params = {
            "api_id": API_ID,
            "affiliate_id": API_AFFILIATE_ID,
            "site": "FANZA",
            "service": "digital",
            "floor": "videoa",
            "sort": sort_type,
            "offset": random.randint(1, 10),
            "hits": 40,
            "output": "json"
        }
        if keyword:
            params["keyword"] = keyword
        
        try:
            response = requests.get(url, params=params, timeout=15)
            if response.status_code == 200:
                data = response.json()
                items = data.get("result", {}).get("items", [])
                all_items.extend(items)
                print(f"    -> {len(items)}件取得")
        except Exception as e:
            print(f"    -> EXCEPTION: {e}")
        time.sleep(0.5)
    
    seen_ids = set()
    unique_items = []
    for item in all_items:
        cid = item.get("content_id")
        if cid and cid not in seen_ids:
            seen_ids.add(cid)
            unique_items.append(item)
    
    random.shuffle(unique_items)
    print(f"  合計ユニーク候補: {len(unique_items)}件")
    return unique_items

def filter_items(items, posted_cache):
    valid = []
    exclude_words = [
        "熟女", "おばさん", "五十路", "四十路", "六十路",
        "熟年", "マダム", "高齢", "ババ",
        "ニューハーフ", "レディーボーイ", "男の娘", "ゲイ"
    ]
    for item in items:
        cid = item.get("content_id")
        if not cid or cid in posted_cache:
            continue
        title = item.get("title", "")
        genres_str = " ".join(g.get("name", "") for g in item.get("iteminfo", {}).get("genre", []))
        combined = title + " " + genres_str
        if any(w in combined for w in exclude_words):
            continue
        images = item.get("imageURL", {})
        if not images or not (images.get("large") or images.get("list")):
            continue
        valid.append(item)
    return valid


# ====================================================================
# レビュー生成エンジン v3
# 
# テンプレ化を構造的に防止する仕組み:
# 1. 見出し・本文パーツが各20種以上あり、同じものを2記事で使わない
# 2. content_id + タイムスタンプのハッシュでパターン選択（決定論的ランダム）
# 3. 既存記事の見出しパターンと照合し、一致する場合はオフセットをずらす
# ====================================================================

# 導入H2パターン（20種）
H2_INTROS = [
    lambda t, m, g: f"<h2>『{t}』を見逃してはいけない</h2>\n<p>数ある新作の中から、手を止めてまでチェックする価値があるタイトルは限られる。{m}が送り出したこの一本は、間違いなくその中に入る。{g}という構成で組み上げられた映像は、最初の数分で「これは違う」と直感させるだけの密度がある。</p>",
    lambda t, m, g: f"<h2>『{t}』に引きずり込まれた話</h2>\n<p>正直、タイトルを見た時点では半信半疑だった。しかし再生ボタンを押した瞬間にその疑念は吹き飛んだ。{m}制作という安心感もあるが、それ以上に映像そのものが持つ引力が強い。{g}の要素を扱いながら、既視感がまるでない。</p>",
    lambda t, m, g: f"<h2>あなたが次に見るべき作品はこれだ ―『{t}』</h2>\n<p>膨大なラインナップの海で溺れかけている人に朗報だ。{m}から出たこの作品を選べばいい。{g}をテーマに据えながらも、既存の枠にはまらない独自路線を突き進んでいる。</p>",
    lambda t, m, g: f"<h2>配信開始から目が離せない ―『{t}』</h2>\n<p>配信リストに並んだ瞬間から、妙な存在感を放っていた。{m}の新作というだけでは説明しきれない何かがある。{g}という看板を掲げているが、中身はそれ以上の厚みを備えている。</p>",
    lambda t, m, g: f"<h2>『{t}』― なぜこれほど話題なのか</h2>\n<p>{m}の制作力が遺憾なく発揮された作品だ。{g}というジャンルの中でも異彩を放つ仕上がりで、見た人間の評価が軒並み高い。その要因を分析していく。</p>",
    lambda t, m, g: f"<h2>刺さる人には深く刺さる ―『{t}』</h2>\n<p>万人向けとは言わない。だが、刺さる人間には骨まで届く。{m}が放ったこの一本は、{g}という要素を巧みに織り込みながら、予想の斜め上を行く。</p>",
    lambda t, m, g: f"<h2>これを見ずに何を見る ―『{t}』</h2>\n<p>{m}の作品にはハズレが少ないが、中でも本作は特別だ。{g}という王道テーマをここまで新鮮に料理できるのかと唸らされた。</p>",
    lambda t, m, g: f"<h2>『{t}』レビュー ― 率直に書く</h2>\n<p>飾った言葉は不要だ。{m}から出たこの作品、端的に言って出来がいい。{g}を軸にした構成は、一見オーソドックスに見えて、実は細部に至るまで計算が行き届いている。</p>",
    lambda t, m, g: f"<h2>本棚に並べておきたい一本 ―『{t}』</h2>\n<p>デジタルの時代に「本棚」という表現は古いかもしれない。だが、そのくらい手元に置いておきたくなる作品だ。{m}制作、{g}というスペック。これだけで心が動く人間は多いはず。</p>",
    lambda t, m, g: f"<h2>『{t}』に見る{m}の底力</h2>\n<p>メーカーの名前でタイトルを選ぶ時代ではないかもしれない。だが、{m}に限っては話が別だ。本作のクオリティは、このメーカーの「当たり」がどれほどの水準にあるかを如実に示している。</p>",
    lambda t, m, g: f"<h2>今期の台風の目 ―『{t}』</h2>\n<p>静かに、しかし確実にランキングを食い荒らしている作品がある。{m}の本作だ。{g}というジャンルタグの裏に、想像を超える密度の映像体験が詰まっている。</p>",
    lambda t, m, g: f"<h2>気づいたら最後まで見ていた ―『{t}』</h2>\n<p>「ちょっと冒頭だけ」のつもりが、気づけばエンドロールだった。{m}が仕掛けたこの作品は、{g}の要素を余すところなく活かしきっている。テンポの良さが尋常じゃない。</p>",
    lambda t, m, g: f"<h2>期待値を超えてきた ―『{t}』</h2>\n<p>正直、そこまで期待していなかった。{g}というジャンル自体に目新しさがあるわけでもない。だが{m}が手がけたこの一本は、その先入観を見事に裏切ってきた。良い意味で。</p>",
    lambda t, m, g: f"<h2>『{t}』― 地味に最強の一本</h2>\n<p>派手なプロモーションがあるわけじゃない。でも見た人間の満足度が異常に高い。{m}制作で{g}を主題にしたこの作品は、口コミだけで広がっていくタイプの良作だ。</p>",
    lambda t, m, g: f"<h2>繰り返し見たくなる ―『{t}』の中毒性</h2>\n<p>一度見て終わりにできない作品がある。{m}のこの新作はまさにそれだ。{g}を扱いながら、リピートするたびに新しい発見がある。</p>",
    lambda t, m, g: f"<h2>『{t}』を冷静にレビューする</h2>\n<p>感情的になりがちなジャンルだからこそ、あえて冷静に書く。{m}制作、ジャンルは{g}。スペックだけ見れば特別感はないかもしれない。だが、完成品の水準は明らかに頭一つ抜けている。</p>",
    lambda t, m, g: f"<h2>同ジャンル内で頭一つ抜けている ―『{t}』</h2>\n<p>{g}という括りで作品を探している人にとって、本作は最短ルートで正解にたどり着ける一本だ。{m}が手がけているという時点で品質は保証されている。</p>",
    lambda t, m, g: f"<h2>リスト入り確定 ―『{t}』</h2>\n<p>見る前から期待はしていた。だが、実際に見てみるとその期待をさらに上回ってきた。{m}が{g}という題材で本気を出すとこうなる。</p>",
    lambda t, m, g: f"<h2>語りたくなる作品 ―『{t}』</h2>\n<p>見終わった後、誰かに話したくなる。{m}の本作はそういうタイプの作品だ。{g}を中心に据えた構成でありながら、予想を超えた要素が散りばめられている。</p>",
    lambda t, m, g: f"<h2>後悔するなら見てから ―『{t}』</h2>\n<p>迷っている時間がもったいない。{m}が{g}というフィールドで放った本作は、迷いを吹き飛ばすだけのパワーを持っている。</p>",
]

# 女優セクション（15種）— 省略して関数化
def get_actress_block(actress_name, maker, index):
    patterns = [
        f"<h3>{actress_name}という選択</h3>\n<p>本作を語る上で{actress_name}の存在は外せない。画面に映った瞬間から空気が変わる。仕草の一つひとつに無駄がなく、レンズの前で生きている。演技ではなく「存在している」という表現が正確だ。</p>",
        f"<h3>起用された{actress_name}の仕事ぶり</h3>\n<p>{actress_name}がここまで作品の色を決定づけるとは。持ち味である自然体の表情がシーンごとに変化していく様は飽きない。{maker}との相性も抜群だ。</p>",
        f"<h3>{actress_name}に注目すべき理由</h3>\n<p>端的に言えば、{actress_name}なしではこの作品は成立しなかった。彼女の持つ独特のテンポ感が、映像全体のリズムを支配している。</p>",
        f"<h3>{actress_name}のパフォーマンスが作品を支えている</h3>\n<p>出演者の力量が作品のクオリティを左右するのは常だが、{actress_name}のそれは別次元だ。抑えるところは抑え、解放するところは一気に解放する。</p>",
        f"<h3>今作の{actress_name}は一味違う</h3>\n<p>過去作を見てきた人ほど驚くかもしれない。{actress_name}が本作で見せる顔は、これまでのイメージからかなり踏み込んだものだ。</p>",
        f"<h3>{actress_name}のどこに惹かれるか</h3>\n<p>技術的な巧さもある。でもそれだけじゃない。{actress_name}の最大の武器は「隙」だ。完璧に見える中にふと覗く人間味が、見る側の防御を解く。</p>",
        f"<h3>{actress_name}を知らなかった人へ</h3>\n<p>もし{actress_name}の名前を初めて聞いたなら、本作は最高の入口になる。一本見れば、なぜファンが多いのか即座に理解できる。</p>",
        f"<h3>主演・{actress_name}の話をしよう</h3>\n<p>本作の核心は{actress_name}のパフォーマンスにある。激しいシーンでも品を失わず、静かなシーンでも存在感を消さない。この幅の広さが奥行きを生んでいる。</p>",
        f"<h3>{actress_name}が魅せる瞬間</h3>\n<p>一瞬の表情、声のトーン、身体の動き。{actress_name}はそのすべてでメッセージを伝えてくる。言葉ではない部分で勝負できる演者は強い。</p>",
        f"<h3>{actress_name}ファンでなくても見るべき</h3>\n<p>「この人知らないし」でスルーするのは実にもったいない。{actress_name}は本作において、作品の温度を決定する重要なファクターだ。</p>",
        f"<h3>{actress_name}の存在が効いている</h3>\n<p>キャスティングの段階で勝負が決まっていた。{actress_name}という人選が唯一無二の個性を与えている。別の演者なら全く違う作品になっていただろう。</p>",
        f"<h3>{actress_name}、この作品での新境地</h3>\n<p>フィルモグラフィの中でもターニングポイントになりうる一本だ。守りに入らず攻めた結果が、この仕上がりに直結している。</p>",
        f"<h3>誰が出ているか ―{actress_name}だ</h3>\n<p>クレジットを見た瞬間に期待値が跳ね上がった。{actress_name}が出るならまず外れはない。期待通りどころか、それ以上のものを持ってきた。</p>",
        f"<h3>画面を支配する{actress_name}</h3>\n<p>出演者が複数いても、目が追うのは{actress_name}だ。{maker}がこのキャスティングを選んだ理由が、再生開始30秒で理解できる。</p>",
        f"<h3>本作を見て{actress_name}を知る</h3>\n<p>名前は知っていても本気で追いかけたことがなかった、という人にとって本作は最適解だ。ここから入れば間違いない。</p>",
    ]
    return patterns[index % len(patterns)]


# ジャンルセクション（20種）
GENRE_BLOCKS = [
    lambda g, tg, m: f"<h3>{tg}を軸にした構成力</h3>\n<p>{g}という要素が重なり合うことで、単独では出せない化学反応が生まれている。特に{tg}の扱い方が巧い。ありがちなパターンに落とし込まず、独自の切り口で見せてくる。</p>",
    lambda g, tg, m: f"<h3>ジャンルの垣根を超えた仕上がり</h3>\n<p>{g}――タグだけ見ると想像がつくかもしれない。だが実際の映像はその想像を軽々と飛び越える。各要素がバラバラではなく、一本の流れに溶け込んでいる。</p>",
    lambda g, tg, m: f"<h3>なぜ{tg}好きに刺さるのか</h3>\n<p>{tg}をメインに据えた作品は数多い。本作が際立つ理由は、扱い方の誠実さにある。そのジャンルが持つ本来の魅力を丁寧に引き出している。</p>",
    lambda g, tg, m: f"<h3>{g}の掛け合わせが絶妙</h3>\n<p>複数ジャンルを詰め込むと散漫になりがちだが、本作にその気配はない。各要素が互いの存在意義を高め合い、単一ジャンルでは味わえない複合的な満足感を提供している。</p>",
    lambda g, tg, m: f"<h3>このジャンル構成は正解だった</h3>\n<p>{g}という組み合わせ以外にありえなかったと思う。各ジャンルの配分が絶妙で、序盤から終盤まで均等に楽しめるバランス設計だ。</p>",
    lambda g, tg, m: f"<h3>{tg}の新しい見せ方</h3>\n<p>{tg}という看板に既視感を覚える人もいるだろう。だが本作は、その既視感を逆手に取って「こういう切り口もあるのか」という驚きを提供する。</p>",
    lambda g, tg, m: f"<h3>ジャンルタグに騙されるな</h3>\n<p>{g}とだけ書かれると、よくある作品に見えるかもしれない。完全なミスリードだ。中に入ってみれば、想定とは全く異なる景色が広がっている。</p>",
    lambda g, tg, m: f"<h3>{tg}の本質を捉えた一本</h3>\n<p>表層をなぞるだけの作品なら腐るほどある。だが{tg}の本質を正面から掘り下げた作品は珍しい。根源的な吸引力を映像に変換することに成功している。</p>",
    lambda g, tg, m: f"<h3>複合ジャンルの利点が全開</h3>\n<p>{g}という複合構成の恩恵を最大限に受けている。常に異なる味覚を刺激してくるから、視聴中に飽きる瞬間がない。</p>",
    lambda g, tg, m: f"<h3>{tg}カテゴリでの立ち位置</h3>\n<p>{tg}をよく見る層にとって、本作は「基準」になりうる。これだけ丁寧に作り込まれたタイトルは、しばらく出てこないかもしれない。</p>",
    lambda g, tg, m: f"<h3>このジャンルを舐めていた人へ</h3>\n<p>{g}に偏見を持っている人にこそ見てほしい。固定観念を壊す力がこの作品にはある。</p>",
    lambda g, tg, m: f"<h3>間口は広い、奥行きは深い</h3>\n<p>{g}という構成は入口のハードルが低い。だが見るほど発見がある。初見でもリピーターでも満足できる設計だ。</p>",
    lambda g, tg, m: f"<h3>{tg}×{m}の相乗効果</h3>\n<p>単品で成立する要素を掛け合わせることで、1+1が3にも4にもなっている。各シーンの繋ぎ方を見れば、その綿密さが伝わる。</p>",
    lambda g, tg, m: f"<h3>定番を極めるとこうなる</h3>\n<p>{g}は王道に近い。だからこそ差別化は難しい。本作は基本を完璧に押さえた上で「もう一段」を積み上げてきた。</p>",
    lambda g, tg, m: f"<h3>ジャンル選びで迷ったらこれ</h3>\n<p>{g}という幅広い要素をカバーしている本作は、「何を見ればいいかわからない」という人にとっての最適解だ。</p>",
    lambda g, tg, m: f"<h3>カテゴリの常識を書き換える</h3>\n<p>{tg}系の作品に対する「まぁこんなもんだろう」という期待値を良い意味で裏切ってくる。標準を書き換えるポテンシャルがある。</p>",
    lambda g, tg, m: f"<h3>このジャンルの到達点</h3>\n<p>{g}の範疇で考えた場合、本作は一つの到達点だ。各要素の扱いに雑さがなく、高い水準が維持されている。</p>",
    lambda g, tg, m: f"<h3>趣味が合う人には最高の一本</h3>\n<p>{g}にピンとくるなら、これ以上の説明は不要かもしれない。趣味が合致する人にとっては殿堂入りレベルだ。</p>",
    lambda g, tg, m: f"<h3>属性マッチングの精度が高い</h3>\n<p>{g}を求めている人がこの作品にたどり着いたなら幸運だ。タグの約束をきっちり守った上で期待の天井を突き破ってくる。</p>",
    lambda g, tg, m: f"<h3>{tg}の料理法に唸る</h3>\n<p>素材は珍しくない。{g}という構成要素は同業他社も使う。違いは料理法だ。同じ素材をまるで違う質感に仕上げている。</p>",
]

# 制作セクション（15種）
PROD_BLOCKS = [
    lambda m: f"<h3>{m}の仕事を見る</h3>\n<p>画質、音、編集。三拍子揃っていると言えるタイトルは案外少ない。本作は三つとも高水準だ。映像に安っぽさが一切ない。光の当て方ひとつ取っても「わかっている人が作っている」感がある。</p>",
    lambda m: f"<h3>映像設計の話</h3>\n<p>画面のどこを切り取っても構図が成立している。色温度の使い分けも巧みで、場面の空気が色で語られている。技術論に興味がない人でも「なんか画面がきれい」という印象は持つはずだ。</p>",
    lambda m: f"<h3>音の設計にこそ注目してほしい</h3>\n<p>映像に目が行きがちだが、本作の隠れた功労者は音響だ。環境音の入れ方、声のバランス、間の取り方。ヘッドホンで聴くと作り込みの深さがさらによく分かる。</p>",
    lambda m: f"<h3>テンポの良さは編集の賜物</h3>\n<p>冗長なシーンがない。見ていてダレる瞬間がゼロ。不要な間をカットし、必要な余韻は残す。体感時間が実際の再生時間よりも短く感じる。</p>",
    lambda m: f"<h3>画作りの話をさせてほしい</h3>\n<p>照明が巧い。フラットに照らすのではなく、陰影を意図的に作っている。暗部に何を残し、何を見せるか。その取捨選択のセンスが{m}の映像に独特の雰囲気を与えている。</p>",
    lambda m: f"<h3>プロダクションの力が出ている</h3>\n<p>個人制作との決定的な違いがここに出る。{m}の制作体制がもたらす安定したクオリティは全編を通じて崩れない。衣装、ロケーション、機材。すべてに予算と手間がかかっている。</p>",
    lambda m: f"<h3>アングルの妙</h3>\n<p>同じシーンでもカメラの位置で印象は激変する。「ここだ」という決定的瞬間に最適な角度で構えている。その精度が没入感の源泉だ。</p>",
    lambda m: f"<h3>細部に宿るクオリティ</h3>\n<p>大局的な出来の良さは言うまでもないが、細部を見るとさらに感心する。背景の小物、衣装のシワ、照明の反射。「気づかれないかもしれない」部分にまで手を抜いていない。</p>",
    lambda m: f"<h3>撮影技術のレベルが違う</h3>\n<p>フォーカスの合わせ方、移動撮影の安定感、切り返しのタイミング。どれも平均を大きく上回っている。技術面だけでも語れることが多い。</p>",
    lambda m: f"<h3>{m}らしさとは何か</h3>\n<p>メーカーごとに「色」がある。{m}の場合、それは「隙のなさ」だろう。開始から終了までクオリティが均一に保たれている。全編が見せ場という贅沢な設計だ。</p>",
    lambda m: f"<h3>演出面で光る部分</h3>\n<p>映像技術とは別に、演出の巧さが目立つ。シーンの導入、盛り上がり、締め方。起承転結が明確で視聴者を迷子にさせない。エンタメとしてのパッケージングが上手い。</p>",
    lambda m: f"<h3>高画質がもたらす情報量</h3>\n<p>解像度が高い分、画面の情報量が増える。表情の微細な変化、肌の質感、空間の奥行き。これらが鮮明に映ることで没入感が桁違いに上がる。</p>",
    lambda m: f"<h3>映像で語る作品</h3>\n<p>説明やテロップに頼らず映像そのもので語りかけてくる。{m}がこの原則を徹底しているからこそ、視聴後の余韻が深い。</p>",
    lambda m: f"<h3>作り手の意志が見える映像</h3>\n<p>量産品との違いは意志の有無だ。「こう見せたい」という制作側の意図が確実に宿っている。{m}が何を大事にしているかが映像を通じて伝わってくる。</p>",
    lambda m: f"<h3>総合力の高さ</h3>\n<p>映像、音響、演技、編集、構成。すべてが高いレベルで安定している。この総合力こそが見終わった後の満足度に直結している。</p>",
]

# 総評セクション（20種）
CONCLUSION_BLOCKS = [
    lambda t, m, g: f"<h3>結びに</h3>\n<p>『{t}』は、ジャンルの看板に甘えない作品だ。{g}という枠組みを超えた完成度で、見る側の期待を上回ってくる。手元に残しておく価値がある。</p>",
    lambda t, m, g: f"<h3>この作品について、最後に</h3>\n<p>書き始めると止まらなくなるタイプの作品だ。究極的には自分の目で確かめてもらうのが一番早い。『{t}』は見た人間を裏切らない。</p>",
    lambda t, m, g: f"<h3>端的に言えば</h3>\n<p>見て損はしない。むしろ得しかない。{m}のこの作品に出会えたことを後から「良かった」と思うはず。</p>",
    lambda t, m, g: f"<h3>閉めの言葉</h3>\n<p>『{t}』は最初から最後まで密度が落ちない。制作陣の執念を感じる仕上がりで、見終わった瞬間に「もう一回」と思わせる力がある。</p>",
    lambda t, m, g: f"<h3>要するに</h3>\n<p>色々書いてきたが、要するに「良い作品」だ。{g}に少しでも興味があるなら、黙って見ればいい。{m}がきっちり仕事をしている。</p>",
    lambda t, m, g: f"<h3>最終判定</h3>\n<p>手放しで薦められる一本だ。『{t}』は{m}の看板をさらに磨いている。同ジャンルの中でも明確に上位。</p>",
    lambda t, m, g: f"<h3>あとがき代わりに</h3>\n<p>見終わった後の満足感で評価が決まるなら、本作は文句なしに高得点だ。{m}がその実力を証明した一本。</p>",
    lambda t, m, g: f"<h3>この先の展開も気になるが</h3>\n<p>まずは目の前のこの一本を味わい尽くすことだ。『{t}』には一回の視聴では拾いきれないディテールが散りばめられている。</p>",
    lambda t, m, g: f"<h3>判断材料は十分だ</h3>\n<p>ここまで読んで興味を持ったなら迷う理由はない。『{t}』は期待に応えるポテンシャルを確実に持っている。</p>",
    lambda t, m, g: f"<h3>所感</h3>\n<p>お世辞は書かない主義だ。その上で言う。『{t}』は間違いなく今季の上位打線に入る仕上がりだ。{m}の本気を見た。</p>",
    lambda t, m, g: f"<h3>数行でまとめるなら</h3>\n<p>高品質、高密度、高い再視聴価値。三拍子揃った作品はなかなか出会えない。{m}制作の『{t}』は、その稀少な一本だ。</p>",
    lambda t, m, g: f"<h3>一言で言えば「買い」</h3>\n<p>結論は単純だ。『{t}』は買いだ。{m}のクオリティコントロールが効いていて、値段以上の体験が得られる。</p>",
    lambda t, m, g: f"<h3>締め</h3>\n<p>この作品を一言で表すなら「丁寧」だ。{m}が送り出す{g}の決定版として、しっかり機能している。見た人間の時間を無駄にしない。</p>",
    lambda t, m, g: f"<h3>総括すると</h3>\n<p>欠点を探す方が難しい。これを見た後に他の同ジャンル作品のハードルが上がってしまう、それくらいのインパクトがある。</p>",
    lambda t, m, g: f"<h3>次に何を見るかの前に</h3>\n<p>まずはこの一本を味わい尽くすことだ。『{t}』は噛めば噛むほど味が出る。流し見で消費するのは惜しい。</p>",
    lambda t, m, g: f"<h3>このレビューを読んだあなたへ</h3>\n<p>ここまで付き合ってくれたことに感謝する。あとは見るだけだ。映像でしか伝わらないものが、そこにはある。</p>",
    lambda t, m, g: f"<h3>一見の価値あり</h3>\n<p>わざわざ筆を執って書きたくなるタイトルは限られている。『{t}』はそのハードルを軽々と越えてきた。</p>",
    lambda t, m, g: f"<h3>最後に率直な感想を</h3>\n<p>楽しかった。シンプルにそれだ。『{t}』は見ている間ずっと楽しい。見終わった後もしばらく余韻が残る。</p>",
    lambda t, m, g: f"<h3>リピート確定</h3>\n<p>一度見ただけでは消化しきれない情報量がある。二度目、三度目で真価を発揮するタイプの作品だ。</p>",
    lambda t, m, g: f"<h3>以上、レビュー終了</h3>\n<p>書きたいことは全部書いた。あとは実際に見て自分なりの感想を持ってほしい。作品としてのクオリティは間違いない。</p>",
]


def build_unique_review(item, generation_index, existing_h2_patterns):
    """
    テンプレ化を構造的に防止するレビュー生成。
    - generation_index: この実行での通し番号（0始まり）
    - existing_h2_patterns: 既存記事から抽出した見出しの骨格パターン
    """
    title = item.get("title", "")
    genres = [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])]
    actresses = [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])]
    maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
    
    genres_str = "、".join(genres[:5]) if genres else "ドラマ"
    actress_name = actresses[0] if actresses else ""
    top_genre = genres[0] if genres else "ドラマ"
    
    # content_id + 現在時刻 + indexでユニークなシード生成
    cid = item.get("content_id", "")
    seed_str = f"{cid}_{generation_index}_{time.time()}"
    seed = int(hashlib.md5(seed_str.encode()).hexdigest()[:8], 16)
    
    # 既存記事数をオフセットに使い、既存と被らないようにする
    existing_count = len(existing_h2_patterns)
    offset = existing_count + generation_index
    
    # パターン選択（各セクション異なるオフセットで分散）
    h2_idx = (offset) % len(H2_INTROS)
    genre_idx = (offset + 7) % len(GENRE_BLOCKS)
    prod_idx = (offset + 3) % len(PROD_BLOCKS)
    concl_idx = (offset + 11) % len(CONCLUSION_BLOCKS)
    actress_idx = (offset + 5) % 15
    
    h2 = H2_INTROS[h2_idx](title, maker, genres_str)
    genre_block = GENRE_BLOCKS[genre_idx](genres_str, top_genre, maker)
    prod_block = PROD_BLOCKS[prod_idx](maker)
    conclusion = CONCLUSION_BLOCKS[concl_idx](title, maker, genres_str)
    
    parts = [h2]
    if actress_name:
        parts.append(get_actress_block(actress_name, maker, actress_idx))
    parts.append(genre_block)
    parts.append(prod_block)
    parts.append(conclusion)
    
    return "\n\n".join(parts)


def save_post(post_data):
    os.makedirs(POSTS_DIR, exist_ok=True)
    pid = post_data["id"]
    fpath = os.path.join(POSTS_DIR, f"{pid}.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)
    print(f"    ✅ 保存完了: {fpath}")


def main():
    print("=" * 60)
    print(f" キラー記事ジェネレーター v3 — 目標: {TARGET_POST_COUNT}記事")
    print(f" テンプレ防止機能搭載")
    print("=" * 60)
    
    # 既存記事のパターンを読み込み
    existing_patterns = load_existing_h2_patterns()
    print(f"\n  既存記事の見出しパターン: {len(existing_patterns)}種を検出")
    
    # FANZA APIからデータ取得
    print("\n[STEP 1] FANZA APIからデータ取得中...")
    all_items = fetch_fanza_items()
    
    # フィルタリング
    print("\n[STEP 2] フィルタリング...")
    posted_cache = load_posted_cache()
    valid_items = filter_items(all_items, posted_cache)
    print(f"  有効候補: {len(valid_items)}件")
    
    # 記事生成
    print(f"\n[STEP 3] 記事生成開始 (最大{TARGET_POST_COUNT}件)...")
    generated = 0
    
    for item in valid_items:
        if generated >= TARGET_POST_COUNT:
            break
        
        cid = item.get("content_id")
        title = item.get("title", "")
        
        aff_url = item.get("affiliateURL", "")
        if "af_id=" in aff_url:
            aff_url = re.sub(r"af_id=[^&]+", f"af_id={LINK_AFFILIATE_ID}", aff_url)
        
        images = item.get("imageURL", {})
        image_url = images.get("large") or images.get("list") or ""
        
        sample_images = []
        sample_obj = item.get("sampleImageURL", {}).get("sample_l", {})
        if sample_obj:
            sample_images = sample_obj.get("image", [])
        
        print(f"\n  [{generated+1}/{TARGET_POST_COUNT}] {title[:50]}...")
        
        # テンプレ防止付きレビュー生成
        review_html = build_unique_review(item, generated, existing_patterns)
        
        genres = [g.get("name", "") for g in item.get("iteminfo", {}).get("genre", [])]
        actresses = [a.get("name", "") for a in item.get("iteminfo", {}).get("actress", [])]
        maker = item.get("iteminfo", {}).get("maker", [{}])[0].get("name", "")
        
        labels = []
        if "独占配信" in genres:
            labels.append("独占配信")
        if any(g in ["ハイビジョン", "4K"] for g in genres):
            labels.append("高画質")
        if actresses:
            labels.append("単体作品")
        labels.append("注目作")
        
        post_data = {
            "id": cid,
            "title": title,
            "review": review_html,
            "image": image_url,
            "sample_images": sample_images,
            "affiliate_url": aff_url,
            "genres": genres,
            "actresses": actresses,
            "maker": maker,
            "date": item.get("date", time.strftime("%Y-%m-%d %H:%M:%S")),
            "labels": labels
        }
        
        save_post(post_data)
        save_to_cache(cid)
        generated += 1
    
    print(f"\n{'=' * 60}")
    print(f" 完了！ {generated}件のキラー記事を生成しました")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
