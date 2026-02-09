from flask import Blueprint, Flask, app, flash, redirect, render_template, request, url_for
from models import db
from models.vocabulary import Vocabulary

vocabulary_bp = Blueprint('vocabulary', __name__)

@vocabulary_bp.route('/admin/vocabulary')
def getVocabularyPage():
    vocabularies = Vocabulary.query.all()
    return render_template('admin/vocabulary/view.html', vocabulary_list=vocabularies)

@vocabulary_bp.route('/admin/vocabulary/create')
def getCreateVocabularyPage():
    return render_template('admin/vocabulary/create.html')

@vocabulary_bp.route("/admin/vocabulary/create", methods=["GET", "POST"])
def createVocabulary():
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

@vocabulary_bp.route("/admin/vocabulary/update/<int:id>", methods=["GET", "POST"])
def updateVocabulary(id):
    vocab = Vocabulary.query.get_or_404(id)

    if request.method == "POST":
        vocab.word = request.form["word"]
        vocab.meaning = request.form["meaning"]
        vocab.phonetic = request.form.get("phonetic")
        vocab.word_type = request.form.get("word_type")

        db.session.commit()
        return redirect(url_for("vocabulary.getVocabularyPage"))

    return render_template("admin/vocabulary/update.html", vocab=vocab)


@vocabulary_bp.route("/admin/vocabulary/delete/<int:id>", methods=["GET","POST"])
def deleteVocabulary(id):
    vocab = Vocabulary.query.get_or_404(id)

    if request.method == "POST":
        db.session.delete(vocab)
        db.session.commit()
        return redirect(url_for("vocabulary.getVocabularyPage"))

    return render_template("admin/vocabulary/delete.html", id=id, vocab=vocab)
