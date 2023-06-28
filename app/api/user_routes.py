from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Thread
from app.models import db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)

    return user.to_dict()

@user_routes.route('/<int:id>/followed_threads')
@login_required
def get_followed_threads(id):
    user = User.query.get(id)
    if len(user.followed_threads) == 0:
        return []
    else:
        return [thread.to_dict() for thread in user.followed_threads]

@user_routes.route('/<int:id>/follow_thread/<int:thread_id>', methods=['POST'])
@login_required
def follow_thread(id, thread_id):
    user = User.query.get(id)
    thread = Thread.query.get(thread_id)
    if not thread:
        return {'error':'could not find thread'}
    else:
        user.followed_threads.append(thread)
        db.session.commit()
        return thread.to_dict()


@user_routes.route('<int:id>/unfollow_thread/<int:thread_id>', methods=['DELETE'])
@login_required
def unfollow_thread(id, thread_id):
    user = User.query.get(id)
    for thread in user.followed_threads:
        if thread.id == thread_id:
            user.followed_threads.remove(thread)
            db.session.commit()
            return {'success':'thread has been removed'}
