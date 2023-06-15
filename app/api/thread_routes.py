from flask import Blueprint, redirect,request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import db, Thread,User, Category
from app.forms import ThreadForm



thread_routes = Blueprint('thread', __name__)

#Route to get all categories
@thread_routes.route('/<category_name>', methods = ["GET"])
def get_thread_by_category(category_name):
    #query database
    threads = Thread.query.all()
    all_threads = {}

    for thread in threads:
        for category in thread.category:
            if category.name == category_name:
                all_threads[thread.id] = thread.to_dict()

    return all_threads

@thread_routes.route('/<int:id>', methods = ["GET"])
def get_thread_by_id(id):
    thread = Thread.query.get(id)
    if not thread:
        return {'errors': "could not find thread"}
    else:
        return thread.to_dict_with_txt()

@thread_routes.route('/<category_name>/new', methods=['GET','POST'])
@login_required
def create_thread(category):
    user = User.query.get(current_user.id)

    form = ThreadForm
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        category = Category.query.filter_by(name=category)
        new_thread=Thread(
            subject=form.data["subject"],
            text=form.data["text"],
            views=0,
            user=user,
            categories=category,
            posts=[]
        )

        db.session.add(new_thread)
        db.session.commit()
        return new_thread.to_dict()

@thread_routes.route('/<int:id>', methods=['GET','PUT'])
@login_required
def edit_thread(id):
    thread_to_edit = Thread.query.get(id)

    if current_user.id != thread_to_edit.owner_id:
      return {"errors":"you do not own this board"}

    form = ThreadForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if form.data["subject"]:
            thread_to_edit.subject = form.data["subject"]
        if form.data["text"]:
            thread_to_edit.subject = form.data["text"]

        db.session.commit()
        return thread_to_edit.to_dict()


@thread_routes.route('/<int:id>', methods=['DELETE'])
def delete_thread(id):
    thread = Thread.query.get(id)
    if not thread:
        return {'errors': "could not find thread"}

    db.session.delete(thread)
    db.session.commit()
