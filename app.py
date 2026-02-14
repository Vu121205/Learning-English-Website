from flask import Flask
from controllers.admin.DashBoardController import dashBoard_bp
from controllers.admin.VocabularyController import vocabulary_bp
from controllers.client.HomePageController import homePage_bp
from controllers.admin.TopicController import topic_bp
from models import db
import models


app = Flask(__name__)
app.register_blueprint(dashBoard_bp)
app.register_blueprint(vocabulary_bp)
app.register_blueprint(homePage_bp)
app.register_blueprint(topic_bp)
# config db
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:123456@localhost:3306/learn_english_website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db.init_app(app)

if __name__ == "__main__":
    # create table
    with app.app_context():
        db.create_all()
    app.run(debug=True)
