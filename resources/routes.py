from .blog import BlogsApi, BlogApi, BlogsAdmin, BlogAdmin
from .user import UsersAdmin, UserLogin


def initialize_routes(api):
# Public Routes----------------------------------------
    # Blog --------------------------------------------
    api.add_resource(BlogsApi, '/api/blogs', methods=['GET'])
    api.add_resource(BlogApi, '/api/blogs/<id>', methods=['GET'])

    # User --------------------------------------------
    api.add_resource(UserLogin, '/api/admin/login', methods=['POST'])


# Authenticated Routes --------------------------------
    # Blog Routes -------------------------------------
    api.add_resource(BlogsAdmin, '/blogs/admin')
    api.add_resource(BlogAdmin, '/blogs/admin/<id>')

    # User Routes -------------------------------------
    api.add_resource(UsersAdmin, '/users/admin')

