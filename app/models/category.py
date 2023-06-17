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

if environment == "production":
    thread_categories.schema = SCHEMA


class Category(db.Model):
    __tablename__ = 'categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    threads = db.relationship('Thread', secondary=thread_categories, back_populates='categories', passive_deletes=True)

    def to_dict(self):
        return{
            'id': self.id,
            'name':self.name
        }
