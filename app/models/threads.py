from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta
from .category import thread_categories, thread_sub_categories

following_threads = db.Table(
    'liked_threads',
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column("thread_id", db.Integer, db.ForeignKey(add_prefix_for_prod('threads.id')), primary_key=True)
)

if environment == "production":
    following_threads.schema = SCHEMA
class Thread(db.Model):
    __tablename__ = 'threads'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    categories = db.relationship('Category', secondary= thread_categories, back_populates='threads', passive_deletes=True)
    user = db.relationship('User', back_populates='threads')
    posts = db.relationship('Post', back_populates='thread', cascade='all, delete-orphan')
    subcategories = db.relationship('SubCategory', secondary=thread_sub_categories, back_populates='threads',  passive_deletes=True)
    image = db.relationship('ThreadImage', back_populates='thread', cascade='all, delete-orphan')
    threads_followed = db.relationship('User', secondary=following_threads, back_populates='followed_threads')



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

    def normalize_posts(self):
        all_posts = {}
        for post in self.posts:
                    all_posts[post.id] = post.to_dict()
        return all_posts



    def get_subcategory(self):
        if(len(self.subcategories) > 0):
            return {"name":self.subcategories[0].name, "id":self.subcategories[0].id}
        else:
            return ""

    def get_category(self):
        if(len(self.categories) > 0):
            return {"name":self.categories[0].name, 'id': self.categories[0].id}
        else:
             return ""


    def to_dict_with_txt(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'views': self.views,
            'user': self.user_to_dict(),
            "post_count":len([post.id for post in self.posts]),
            'posts': self.normalize_posts(),
            "latest_post": self.find_youngest_post(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def user_to_dict(self):
         return {
              'id': self.user.id,
              'username': self.user.username,
              'thread_count': len([thread for thread in self.user.threads]),
              'post_count' : len([post for post in self.user.posts]),
         }


    def to_dict(self):
        return{
            'id': self.id,
            'subject': self.subject,
            'views': self.views,
            'text': self.text,
            'user': self.user_to_dict(),
            "post_count":len([post.id for post in self.posts]),
            'posts': self.normalize_posts(),
            "latest_post": self.find_youngest_post(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'subcategory': self.get_subcategory(),
            'category': self.get_category()
        }
