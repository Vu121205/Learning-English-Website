from flask import Flask
from controllers.HomePageController import home_page_bp
from controllers.VocabularyController import vocabulary_bp
from models import db


app = Flask(__name__)
app.register_blueprint(home_page_bp)
app.register_blueprint(vocabulary_bp)
# config db
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:123456@localhost:3306/learn_english_website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db.init_app(app)
from models.vocabulary import Vocabulary

if __name__ == "__main__":
    # create table
    with app.app_context():
        db.create_all()
    app.run(debug=True)
