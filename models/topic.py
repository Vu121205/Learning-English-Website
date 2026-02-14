from . import db

class Topic(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)      # Tiếng Việt
    name_en = db.Column(db.String(255), nullable=False)   # Tiếng Anh
    image = db.Column(db.String(255))                     # Tên file ảnh

    vocabularies = db.relationship("Vocabulary", backref="topic", lazy=True)

    def __repr__(self):
        return f"<Topic {self.name}>"