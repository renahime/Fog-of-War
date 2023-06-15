from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Thread,User, Category


thread_routes = Blueprint('thread', __name__)

#Route to get all categories
@thread_routes.route('/:category_name', methods = ["GET"])
def get_thread_by_category(category_name):
    #query database
    threads = Thread.query.all()
    all_threads = {}

    for thread in threads:
        for category in thread.category:
            if category.name == category_name:
                all_threads[thread.id] = thread.to_dict()

    return all_threads

@thread_routes('/<int:id>', methods=['GET'])
def get_thread_by_id(id):
    thread = Thread.query.get(id)
    if not thread:
        return {'errors': "could not find thread"}
    else:
        return thread.to_dict_with_txt()
