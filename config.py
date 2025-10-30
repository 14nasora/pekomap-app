from typing import Dict, List, Any

# 質問データ（重みつきで精度向上）
QUESTIONS: List[Dict[str, Any]] = [
    {"question": "今日は「お肉」をガッツリ食べたい気分？", "yesType": "niku", "noType": "power", "weight": 3},
    {"question": "甘いスイーツで癒されたい？", "yesType": "sweet", "noType": "sappari", "weight": 2},
    {"question": "辛くて刺激的なものが食べたい？", "yesType": "spicy", "noType": "healing", "weight": 2},
    {"question": "おしゃれなカフェでゆったり過ごしたい？", "yesType": "healing", "noType": "volume", "weight": 2},
    {"question": "ボリューム満点のラーメンでお腹いっぱいにしたい？", "yesType": "volume", "noType": "sappari", "weight": 2},
    {"question": "あっさり・さっぱりしたものが食べたい？", "yesType": "sappari", "noType": "volume", "weight": 2},
    {"question": "中華料理でスタミナをつけたい？", "yesType": "power", "noType": "healing", "weight": 2},
    {"question": "落ち着いた雰囲気の静かな場所が良い？", "yesType": "healing", "noType": "niku", "weight": 1},
    {"question": "しっかり食べて満足感を得たい？", "yesType": "volume", "noType": "sweet", "weight": 1}
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