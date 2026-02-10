from flask import Blueprint, Flask, app, jsonify, render_template, request

from models.vocabulary import Vocabulary

homePage_bp = Blueprint('homePage', __name__)

@homePage_bp.route('/')
def home():
    return render_template('client/homepage/show.html')

@homePage_bp.route("/api/dictionary")
def dictionary_api():
    word = request.args.get("word")

    vocab = Vocabulary.query.filter_by(word=word).first()

    if not vocab:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "word": vocab.word,
        "meaning": vocab.meaning,
        "phonetic": vocab.phonetic
    })
