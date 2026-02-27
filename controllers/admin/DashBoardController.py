from flask import Blueprint, Flask, app, render_template

from models.topic import Topic
from models.vocabulary import Vocabulary

dashBoard_bp = Blueprint('dashboard', __name__)

@dashBoard_bp.route('/admin')
def home():
    vocab_count = Vocabulary.query.count()
    topic_count = Topic.query.count()
    return render_template('admin/dashboard.html', vocab_count=vocab_count, topic_count=topic_count)