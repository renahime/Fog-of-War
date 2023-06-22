from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta


thread_categories = db.Table(
    "thread_categories",
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('categories.id')),
    ),
    db.Column(
        "thread_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('threads.id')),
    )
)

thread_sub_categories = db.Table(
    "thread_sub_categories",
     db.Column(
        "sub_category_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('subcategories.id')),
    ),
    db.Column(
        "thread_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('threads.id')),
    )
)


if environment == "production":
    thread_categories.schema = SCHEMA

if environment == "production":
    thread_sub_categories.schema = SCHEMA


class Category(db.Model):
    __tablename__ = 'categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    threads = db.relationship('Thread', secondary=thread_categories, back_populates='categories', cascade="all, delete", passive_deletes=True,)
    subcategories = db.relationship('SubCategory', back_populates='categories', cascade="all, delete", passive_deletes=True)

    def normalize_subcategory(self):
        all_subcategories = {}
        for subcategory in self.subcategories:
                    all_subcategories[subcategory.id] = subcategory.to_dict()
        return all_subcategories
    
    def find_youngest_post(self):
         post_list = []
         for thread in self.threads:
              for post in thread.posts:
                   post_list.append(post)
        
         sorted_posts = sorted(post_list, key=lambda x: x.created_at, reverse=True)
         if(len(sorted_posts) == 0):
              return {}
         else:
              return sorted_posts[0].to_dict()


    def to_dict(self):
        return{
            'id': self.id,
            'name':self.name,
            'subcategories': self.normalize_subcategory(),
            'thread_count': len([{thread.id} for thread in self.threads]),
            'youngest_post': self.find_youngest_post()
        }

class SubCategory(db.Model):
    __tablename__ = 'subcategories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    categoryId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')), nullable=False)
    name = db.Column(db.String)

    threads = db.relationship('Thread', secondary=thread_sub_categories, back_populates='subcategories', passive_deletes=True)
    categories = db.relationship('Category', back_populates='subcategories',cascade="all, delete", passive_deletes=True)

    def normalize_threads(self):
        all_threads = {}
        for thread in self.threads:
                    all_threads[thread.id] = thread.to_dict()
        return all_threads

    def find_youngest_post(self):
         post_list = []
         for thread in self.threads:
              for post in thread.posts:
                   post_list.append(post)
        
         sorted_posts = sorted(post_list, key=lambda x: x.created_at, reverse=True)
         if(len(sorted_posts) == 0):
              return {}
         else:
              return sorted_posts[0].to_dict()


    def to_dict(self):
        return{
            'id': self.id,
            'name':self.name,
            'threads': self.normalize_threads(),
            'thread_count': len([{thread.id} for thread in self.threads]),
            'youngest_post': self.find_youngest_post()
        }
