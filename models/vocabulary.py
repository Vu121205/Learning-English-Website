from .import db

class Vocabulary(db.Model):
    __tablename__ = "vocabularies"

    id = db.Column(db.Integer, primary_key=True)

    word = db.Column(db.String(255), nullable=False)
    meaning = db.Column(db.String(255), nullable=False)
    phonetic = db.Column(db.String(100))
    word_type = db.Column(db.String(20), nullable=False)

    topic_id = db.Column(db.Integer, db.ForeignKey("topics.id"), nullable=False)
    def __repr__(self):
        return f"<Vocabulary {self.word}>"