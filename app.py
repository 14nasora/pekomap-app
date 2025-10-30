import logging
from typing import Dict, List, Optional
from urllib.parse import quote

from flask import Flask, render_template, request, redirect, url_for, abort
from config import QUESTIONS, TYPE_TO_CATEGORY, AREAS

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def get_result_type(answers: str) -> str:
    """回答から結果のタイプを決定する（重み付け対応）"""
    try:
        answers_list = answers.split(",") if answers else []
        
        if not answers_list:
            return "healing"  # デフォルトタイプ
        
        # 重み付きスコア計算
        scores: Dict[str, float] = {}
        
        for idx, answer_type in enumerate(answers_list):
            if answer_type in TYPE_TO_CATEGORY and idx < len(QUESTIONS):
                weight = QUESTIONS[idx].get("weight", 1)
                scores[answer_type] = scores.get(answer_type, 0) + weight
        
        if not scores:
            return "healing"
        
        # 最高スコアのタイプを取得
        result_type = max(scores, key=scores.get)
        
        # 特別ルール：肉タイプが高スコアまたは2回以上選ばれていれば優先
        if "niku" in scores:
            niku_count = answers_list.count("niku")
            if niku_count >= 2 or scores["niku"] >= max(scores.values()) * 0.8:
                return "niku"
        
        return result_type
        
    except Exception as e:
        logger.error(f"結果タイプの決定中にエラーが発生: {e}")
        return "healing"  # エラー時はデフォルトタイプを返す

def create_maps_url(area: str, category: str) -> str:
    """Google Maps検索用のURLを生成する"""
    query = f"{area} {category}" if area != "現在地" else category
    return f"https://www.google.com/maps/search/{quote(query)}"

@app.route("/", methods=["GET", "POST"])
def index():
    """トップページ処理"""
    try:
        if request.method == "POST":
            area = request.form.get("area", "現在地")
            if area not in AREAS:
                abort(400)
            return redirect(url_for("quiz", step=0, area=area, answers=""))
        return render_template("index.html", areas=AREAS)
    except Exception as e:
        logger.error(f"トップページでエラーが発生: {e}")
        return render_template("error.html", message="予期せぬエラーが発生しました"), 500

@app.route("/quiz/<int:step>", methods=["GET", "POST"])
def quiz(step: int):
    """クイズページ処理"""
    try:
        if step < 0 or step >= len(QUESTIONS):
            abort(404)

        area = request.args.get("area", "現在地")
        if area not in AREAS:
            abort(400)

        answers = request.args.get("answers", "")

        if request.method == "POST":
            answer = request.form.get("answer")
            if not answer or answer not in TYPE_TO_CATEGORY:
                abort(400)

            answers = f"{answers},{answer}" if answers else answer
            next_step = step + 1

            if next_step >= len(QUESTIONS):
                return redirect(url_for("result", area=area, answers=answers))
            return redirect(url_for("quiz", step=next_step, area=area, answers=answers))

        return render_template("quiz.html", 
                            question=QUESTIONS[step],
                            step=step,
                            total_steps=len(QUESTIONS),
                            area=area,
                            answers=answers)

    except Exception as e:
        logger.error(f"クイズページでエラーが発生: {e}")
        return render_template("error.html", message="予期せぬエラーが発生しました"), 500

@app.route("/result")
def result():
    """結果ページ処理"""
    try:
        area = request.args.get("area", "現在地")
        if area not in AREAS:
            abort(400)

        answers = request.args.get("answers", "")
        result_type = get_result_type(answers)
        category = TYPE_TO_CATEGORY[result_type]
        map_url = create_maps_url(area, category)

        return render_template("result.html",
                           category=category,
                           map_url=map_url,
                           area=area)

    except Exception as e:
        logger.error(f"結果ページでエラーが発生: {e}")
        return render_template("error.html", message="予期せぬエラーが発生しました"), 500

@app.errorhandler(404)
def not_found_error(error):
    """404エラーハンドラー"""
    return render_template("error.html", message="ページが見つかりません"), 404

@app.errorhandler(400)
def bad_request_error(error):
    """400エラーハンドラー"""
    return render_template("error.html", message="不正なリクエストです"), 400

@app.errorhandler(500)
def internal_error(error):
    """500エラーハンドラー"""
    return render_template("error.html", message="サーバーエラーが発生しました"), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
