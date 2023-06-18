
from flask import Blueprint, redirect,request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import db, Thread,User, Category, Post, Image
from app.forms import ImageForm
from .auth_routes import validation_errors_to_error_messages
from .AWS_helpers import get_unique_filename, upload_file_to_s3

image_routes = Blueprint('image', __name__)

@image_routes.route("/post", methods=["GET", "POST"])
# @login_required
def create_post_image(id):
    form = ImageForm()
    user = User.query.get(current_user.id)
    if not user:
        return {"errors": "Couldn't find user"}
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():
        data = form.data
        find_post = Post.query.get(id)

        post_image = data["image"]
        post_image.filename = get_unique_filename(post_image.filename)
        s3_upload = upload_file_to_s3(post_image)

        if "url" not in s3_upload:
            return {"errors": validation_errors_to_error_messages(s3_upload)}

        new_image = Image(
            image = s3_upload["url"],
            post=find_post,
        )

        db.session.add(new_image)
        db.session.commit()
        return new_image.to_dict()
    # if the form has issues send the error messages back to the user
    return {"errors": validation_errors_to_error_messages(form.errors)}, 401

@image_routes.route("/thread", methods=["GET", "POST"])
# @login_required
def create_thread_image(id):
    form = ImageForm()
    user = User.query.get(current_user.id)
    if not user:
        return {"errors": "Couldn't find user"}
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():
        data = form.data
        find_thread = Thread.query.get(id)

        thread_image = data["image"]
        thread_image.filename = get_unique_filename(thread_image.filename)
        s3_upload = upload_file_to_s3(thread_image)

        if "url" not in s3_upload:
            return {"errors": validation_errors_to_error_messages(s3_upload)}

        new_image = Image(
            image = s3_upload["url"],
            thread=find_thread,
        )

        db.session.add(new_image)
        db.session.commit()
        return new_image.to_dict()
    # if the form has issues send the error messages back to the user
    return {"errors": validation_errors_to_error_messages(form.errors)}, 401
