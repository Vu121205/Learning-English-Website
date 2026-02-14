from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import tất cả model để SQLAlchemy nhận diện
from .topic import Topic
from .vocabulary import Vocabulary