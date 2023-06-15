from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta


class Post(db.Model):
    __tablename__ = 'posts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('threads.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user = db.relationship('User', back_populates='posts')
    thread = db.relationship('Thread', back_populates='posts')

    def to_dict(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'text': self.text,
            'user': self.user.to_dict(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
