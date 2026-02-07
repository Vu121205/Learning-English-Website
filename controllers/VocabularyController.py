from flask import Blueprint, Flask, app, redirect, render_template, request, url_for
from models import db
from models.vocabulary import Vocabulary

vocabulary_bp = Blueprint('vocabulary', __name__)

@vocabulary_bp.route('/admin/vocabulary')
def getVocabularyPage():
    return render_template('admin/vocabulary/view.html')

@vocabulary_bp.route('/admin/vocabulary/create')
def getCreateVocabularyPage():
    return render_template('admin/vocabulary/create.html')

@vocabulary_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        word = request.form.get("word")
        meaning = request.form.get("meaning")
        phonetic = request.form.get("phonetic")
        word_type = request.form.get("word_type")

        vocab = Vocabulary(
            word=word,
            meaning=meaning,
            phonetic=phonetic,
            word_type=word_type,
        )

        db.session.add(vocab)
        db.session.commit()

        return redirect(url_for("vocabulary.getVocabularyPage"))

    return render_template("admin/vocabulary/create.html")