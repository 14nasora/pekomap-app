from typing import Dict, List

# 質問データ
QUESTIONS: List[Dict[str, str]] = [
    {"question": "カフェでまったりしたい？", "yesType": "healing", "noType": "power"},
    {"question": "スタミナ満点のご飯で元気出したい？", "yesType": "volume", "noType": "healing"},
    {"question": "スイーツで幸せチャージしたい？", "yesType": "sweet", "noType": "volume"},
    {"question": "静かな空間で落ち着きたい？", "yesType": "healing", "noType": "volume"},
    {"question": "お肉でテンション上げたい？", "yesType": "niku", "noType": "power"},
    {"question": "ピリッと辛さでリフレッシュしたい？", "yesType": "spicy", "noType": "sweet"},
    {"question": "さっぱりしたものが食べたい？", "yesType": "sappari", "noType": "volume"}
]

# タイプ対応ジャンル
TYPE_TO_CATEGORY: Dict[str, str] = {
    "healing": "カフェ",
    "power": "中華",
    "volume": "ラーメン",
    "niku": "焼肉",
    "sweet": "スイーツ",
    "spicy": "激辛",
    "sappari": "うどん・そば"
}

# エリア選択肢
AREAS: List[str] = [
    "現在地","北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県",
    "栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県","新潟県","富山県","石川県",
    "福井県","山梨県","長野県","岐阜県","静岡県","愛知県","三重県","滋賀県","京都府",
    "大阪府","兵庫県","奈良県","和歌山県","鳥取県","島根県","岡山県","広島県","山口県",
    "徳島県","香川県","愛媛県","高知県","福岡県","佐賀県","長崎県","熊本県","大分県",
    "宮崎県","鹿児島県","沖縄県"
]