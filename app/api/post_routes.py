from flask import Blueprint, redirect,request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import db, Thread,User, Category, Post
from app.forms import ThreadForm



post_routes = Blueprint('post', __name__)

@post_routes.route('/thread/<int:thread_id>', methods=['GET','POST'])
@login_required
def create_post(thread_id):
    user = User.query.get(current_user.id)

    form = ThreadForm
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        thread = Thread.query.get(thread_id)
        new_post = Post(
            subject=form.data["subject"],
            text=form.data["text"],
            user=user
            )
        db.session.add(new_post)
        thread.posts.append(new_post)
        db.session.commit()
        return new_post.to_dict()

@post_routes.route('/<int:id>', methods=['GET','PUT'])
@login_required
def edit_post(id):
    post_to_edit = Post.query.get(id)

    form = ThreadForm
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if form.data["subject"]:
            post_to_edit.subject = form.data["subject"]
        if form.data["text"]:
            post_to_edit.subject = form.data["text"]

        db.session.commit()
        return post_to_edit.to_dict()

@post_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_post(id):
    post = Post.query.get(id)
    if not post:
        return {'errors': "could not find thread"}

    db.session.delete(post)
    db.session.commit()
