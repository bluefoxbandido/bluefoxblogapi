from .blog import BlogsApi, BlogApi, BlogsAdmin, BlogAdmin
from .user import UsersAdmin, UserLogin

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

def initialize_routes(api):
    # Public Routes----------------------------------------
    api.add_resource(UserLogin, '/api/users/admin/login')

    # Blog --------------------------------------------
    api.add_resource(BlogsApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<id>')

    # User --------------------------------------------


# Authenticated Routes --------------------------------

    # Blog Routes -------------------------------------
    api.add_resource(BlogsAdmin, '/api/blogs/admin')
    api.add_resource(BlogAdmin, '/api/blogs/admin/<id>')

    # User Routes -------------------------------------
    api.add_resource(UsersAdmin, '/api/users/admin')

