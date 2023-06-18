from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta
from .category import thread_categories, thread_sub_categories


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
    posts = db.relationship('Post', back_populates='thread', cascade='all, delete-orphan')
    subcategories = db.relationship('SubCategory', secondary=thread_sub_categories, back_populates='threads', cascade="all, delete", passive_deletes=True)
    image = db.relationship('Image', back_populates='thread', cascade='all, delete-orphan')

    def find_youngest_post(self):
        if len(self.posts) == 0:
            return {
                'username': self.user.username,
                'subject': self.subject,
                'created_at': self.created_at
            }

        sorted_posts = sorted(self.posts, key=lambda x: x.created_at, reverse=True)
        return {
            'username': sorted_posts[0].user.username,
            'subject': self.subject,
            'created_at':sorted_posts[0].created_at,
        }



    def to_dict_with_txt(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'views': self.views,
            'user': self.user.to_dict(),
            "post_count":len([post.id for post in self.posts]),
            'posts': [post.to_dict() for post in self.posts],
            "latest_post": self.find_youngest_post(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


    def to_dict(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'views': self.views,
            'user': self.user.to_dict(),
            "post_count":len([post.id for post in self.posts]),
            'posts': [post.to_dict() for post in self.posts],
            "latest_post": self.find_youngest_post(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
