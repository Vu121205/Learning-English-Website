import os
from werkzeug.utils import secure_filename
from flask import Blueprint, Flask, app, current_app, flash, redirect, render_template, request, url_for
from sqlalchemy.orm import joinedload
from models import db, Topic, Vocabulary

topic_bp = Blueprint('topic', __name__)

@topic_bp.route('/admin/topic')
def getTopicPage():
    topics = Topic.query.all()
    return render_template("admin/topic/view.html", topics=topics)

@topic_bp.route("/admin/topic/create", methods=["GET", "POST"])
def createTopic():
    if request.method == "POST":
        name = request.form.get("name")
        name_en = request.form.get("name_en")

        file = request.files.get("image")

        filename = None
        if file and file.filename != "":
            filename = secure_filename(file.filename)

            upload_path = os.path.join(
                current_app.root_path,
                "static/uploads/topics",
                filename
            )
            file.save(upload_path)

        topic = Topic(
            name=name,
            name_en=name_en,
            image=filename
        )

        db.session.add(topic)
        db.session.commit()

        return redirect(url_for("topic.getTopicPage"))

    return render_template("admin/topic/create.html")