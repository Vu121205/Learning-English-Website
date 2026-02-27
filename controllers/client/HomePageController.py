from flask import Blueprint, jsonify, render_template, request
import requests
from sqlalchemy import or_

from models.topic import Topic
from models.vocabulary import Vocabulary

homePage_bp = Blueprint('homePage', __name__)

@homePage_bp.route("/")
def home():
    keyword = request.args.get("q")
    search_type = request.args.get("type", "en_vi")
    results = []

    if keyword:
        vocab = process_dictionary_search(keyword, search_type)
        if vocab:
            results = [vocab]

    topics = Topic.query.all()

    return render_template(
        "client/homepage/show.html",
        topics=topics,
        results=results,
        keyword=keyword
    )

def fetch_dictionary_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    try:
        phonetic = ""
        if data[0].get("phonetics"):
            phonetic = data[0]["phonetics"][0].get("text", "")

        word_type = data[0]["meanings"][0]["partOfSpeech"]
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]

        return {
            "phonetic": phonetic,
            "word_type": word_type,
            "definition": definition
        }
    except:
        return None


def translate_to_vi(text):
    url = "https://api.mymemory.translated.net/get"
    try:
        response = requests.get(url, params={
            "q": text,
            "langpair": "en|vi"
        }, timeout=5)

        if response.status_code != 200:
            return text

        data = response.json()
        return data["responseData"]["translatedText"]
    except:
        return text

def process_dictionary_search(keyword, search_type="en_vi"):
    keyword = keyword.strip().lower()

    # ===== 1. Tìm trong database trước =====
    if search_type == "en_vi":
        vocab = Vocabulary.query.filter_by(word=keyword).first()
    else:  # vi_en
        vocab = Vocabulary.query.filter(
            Vocabulary.meaning.ilike(f"%{keyword}%")
        ).first()

    if vocab:
        return vocab

    # ===== 2. Nếu là Việt -> Anh mà DB không có thì thôi =====
    if search_type == "vi_en":
        return None

    # ===== 3. Nếu là Anh -> Việt thì gọi Free Dictionary =====
    data = fetch_dictionary_data(keyword)
    if not data:
        return None

    # KHÔNG dịch nữa, giữ nguyên definition tiếng Anh
    translated_meaning = translate_to_vi(keyword)

    new_vocab = Vocabulary(
        word=keyword,
        meaning=translated_meaning,
        phonetic=data["phonetic"],
        word_type=data["word_type"],
        topic_id=None,
        source="api"
    )

    from app import db   # import tạm để tránh circular
    db.session.add(new_vocab)
    db.session.commit()

    return new_vocab

@homePage_bp.route('/topic/<int:id>')
def vocabularyByTopic(id):
    topic = Topic.query.get_or_404(id)
    vocabularies = Vocabulary.query.filter_by(topic_id=id).all()

    return render_template(
        'client/homepage/topic.html',
        topic=topic,
        vocabularies=vocabularies
    )
