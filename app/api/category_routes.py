from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Category

category_routes = Blueprint('category', __name__)

#Route to get all categories
@category_routes.route('/', methods = ["GET"])
def get_categories():
    #query database
    categories = Category.query.all()
    all_categories = {}

    print(categories[1].threads[0].find_youngest_post())

    #normalize output
    for category in categories:
        all_categories[category.id] = category.to_dict()

    #return all categories
    return all_categories
