from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta



class ThreadImage(db.Model):
    __tablename__ = 'thread_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    threadId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('threads.id')))
    url = db.Column(db.String)

    thread = db.relationship('Thread', back_populates='image')

    def to_dict(self):
        return {
            'id': self.id,
            'threadId': self.threadId,
            'url': self.url
            }

class PostImage(db.Model):
    __tablename__ = 'post_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('posts.id')))
    url = db.Column(db.String)

    post = db.relationship('Post', back_populates='image')

    def to_dict(self):
        return {
            'id': self.id,
            'postId': self.postId,
            'url': self.url
            }
