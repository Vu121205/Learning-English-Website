from .import db

class Vocabulary(db.Model):
    __tablename__ = "vocabularies"

    id = db.Column(db.Integer, primary_key=True)

    word = db.Column(db.String(255), nullable=False, unique=True)
    meaning = db.Column(db.Text, nullable=False)
    phonetic = db.Column(db.String(100))
    word_type = db.Column(db.String(50))

    # Cho phép NULL vì từ API không có topic
    topic_id = db.Column(db.Integer, db.ForeignKey("topics.id"), nullable=True)

    # phân loại nguồn từ điển: "manual" (thủ công), "api" (tự động từ API)
    source = db.Column(db.String(20), default="manual")

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Vocabulary {self.word}>"