from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .threads import following_threads
from datetime import datetime, timedelta


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    about = db.Column(db.String(500))
    signature = db.Column(db.Text)
    profile_image = db.Column(db.String(255))
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    threads = db.relationship('Thread', back_populates='user', cascade="delete-orphan,all")  #added cascade delete
    posts = db.relationship('Post', back_populates='user', cascade="delete-orphan,all")  #added cascade delete
    followed_threads = db.relationship('Thread', secondary=following_threads, back_populates='threads_followed')
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def sort_activity(self):
         all_activity = []
         for thread in self.threads:
              all_activity.append({
                'id': thread.id,
                'subject': thread.subject,
                'text': thread.text,
                'created_at': thread.created_at,
                'category': thread.get_category(),
                'subcategory': thread.get_subcategory()
              })
         for post in self.posts:
             all_activity.append({
                 'id': post.id,
                 'subject': post.subject,
                 'text': post.text,
                 'thread_subject': post.thread.subject,
                 'category': post.get_category(),
                 'subcategory':post.get_subcategory(),
                 'thread_id': post.thread_id,
                 'created_at': post.created_at
             })
         sorted_activity = sorted(all_activity, key=lambda x: x["created_at"], reverse=True)
         return sorted_activity

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile_image': self.profile_image,
            'thread_count': len([thread for thread in self.threads]),
            'post_count' : len([post for post in self.posts]),
            'followed_threads': [thread.to_dict() for thread in self.followed_threads],
            'all_activity': self.sort_activity(),
            'created_at': self.created_at,
            'last_login': self.last_login
        }
