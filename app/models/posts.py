from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta

reply = db.Table(
    "reply",
    db.Column(
        "replyer",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("posts.id")),
        primary_key=True
    ),
    db.Column(
        "replied",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("posts.id")),
        primary_key=True
    )
)

if environment == "production":
    reply.schema = SCHEMA



class Post(db.Model):
    __tablename__ = 'posts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('threads.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', back_populates='posts')
    thread = db.relationship('Thread', back_populates='posts')
    image = db.relationship('PostImage', back_populates='post', cascade='all, delete-orphan')
    replies = db.relationship(
        "Post",
        secondary="reply",
        primaryjoin=reply.c.replied == id,
        secondaryjoin=reply.c.replyer == id,
        backref='replyer',
        lazy='dynamic'
    )

    def get_subcategory(self):
        if(len(self.thread.subcategories) > 0):
            return {"name":self.thread.subcategories[0].name, "id":self.thread.subcategories[0].id}
        else:
            return ""

    def get_category(self):
        if(len(self.thread.categories) > 0):
            return {"name":self.thread.categories[0].name, 'id': self.thread.categories[0].id}

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
            'text': self.text,
            'thread_subject': self.thread.subject,
            'thread_id': self.thread_id,
            'user': self.user_to_dict(),
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'subcategory': self.get_subcategory(),
            'category': self.get_category()
        }
