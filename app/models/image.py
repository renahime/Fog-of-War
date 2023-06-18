from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta



class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table__args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('posts.id')), nullable=False)
    threadId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('threads.id')), nullable=False)
    url = db.Column(db.String)

    post = db.relationship('Post', back_populates='image')
    thread = db.relationship('Thread', back_populates='image')

    def to_dict(self):
        return {
            'id': self.id,
            'postId': self.postId,
            'threadId': self.threadId,
            'url': self.url
            }
