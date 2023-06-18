from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta


thread_categories = db.Table(
    "thread_categories",
    db.Column(
        "thread_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('threads.id')),
    ),
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('categories.id')),
    )
)

thread_sub_categories = db.Table(
    "thread_sub_categories",
    db.Column(
        "thread_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('threads.id')),
    ),
    db.Column(
        "sub_category_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('subcategories.id')),
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

    threads = db.relationship('Thread', secondary=thread_categories, back_populates='categories', passive_deletes=True)
    subcategories = db.relationship('SubCategory', back_populates='categories', passive_deletes=True)

    def to_dict(self):
        return{
            'id': self.id,
            'name':self.name,
            'subcategories': [subcategory.to_dict() for subcategory in self.subcategories]
        }

class SubCategory(db.Model):
    __tablename__ = 'subcategories'

    if environment == "production":
        __table__args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    categoryId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')), nullable=False)
    name = db.Column(db.String)

    threads = db.relationship('Thread', secondary=thread_sub_categories, back_populates='subcategories', passive_deletes=True)
    categories = db.relationship('Category', back_populates='subcategories',cascade="all, delete", passive_deletes=True)

    def to_dict(self):
        return{
            'id': self.id,
            'name':self.name,
            'threads':  [thread.to_dict() for thread in self.threads],
        }
