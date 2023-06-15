from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta
from .category import thread_categories


class Thread(db.Model):
    __tablename__ = 'threads'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    categories = db.relationship('Category', secondary= thread_categories, back_populates='threads',cascade="all, delete", passive_deletes=True)
    user = db.relationship('User', back_populates='threads')
    posts = db.relationship('Post', back_populates='thread')

    def to_dict_with_txt(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'views': self.views,
            'text': self.text,
            'user': self.user.to_dict(),
            'category': self.category.to_dict(),
            'posts': self.posts.to_dict()
        }


    def to_dict(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'views': self.views,
            'user': self.user.to_dict(),
            'category': self.category.to_dict(),
            'post_count': len(self.posts.to_dict())
        }
