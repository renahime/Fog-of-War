from flask import Blueprint, redirect,request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import db, Thread,User, Category, SubCategory
from app.forms import ThreadForm, EditThreadForm
from .auth_routes import validation_errors_to_error_messages



thread_routes = Blueprint('thread', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


#Route to get all categories
@thread_routes.route('/<category_name>', methods = ["GET"])
def get_thread_by_category(category_name):
    #Query database
    threads = Thread.query.all()
    all_threads = {}

    for thread in threads:
        for category in thread.categories:
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

@thread_routes.route('/<int:id>/view', methods = ["PUT"])
def add_view(id):
    thread = Thread.query.get(id)
    if not thread:
        return {'errors': "could not find thread"}
    else:
        thread.views = thread.views + 1
        db.session.commit()
        return {'views': thread.views}


@thread_routes.route('/<category_name>/<int:subcategory_id>/new', methods=['GET','POST'])
@login_required
def create_thread(category_name,subcategory_id):
    user = User.query.get(current_user.id)

    form = ThreadForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        category = Category.query.filter_by(name=category_name).one()
        subcategory = SubCategory.query.get(subcategory_id)
        new_thread=Thread(
            subject=form.data["subject"],
            text=form.data["text"],
            views=0,
            user=user,
            categories=[category],
            subcategories=[subcategory]
        )
        db.session.add(new_thread)
        db.session.commit()
        return new_thread.to_dict()
    elif form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@thread_routes.route('/<int:id>', methods=['GET','PUT'])
@login_required
def edit_thread(id):
    thread_to_edit = Thread.query.get(id)

    if current_user.id != thread_to_edit.user_id:
      return {"errors":"you do not own this board"}

    form = EditThreadForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        if form.data["subject"]:
            thread_to_edit.subject = form.data["subject"]
        if form.data["text"]:
            thread_to_edit.text = form.data["text"]

        db.session.commit()
        return thread_to_edit.to_dict()
    elif form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@thread_routes.route('/<int:id>', methods=['DELETE'])
def delete_thread(id):
    thread = Thread.query.get(id)
    if not thread:
        return {'errors': "could not find thread"}

    db.session.delete(thread)
    db.session.commit()

    return {"success": "thread was deleted"}
