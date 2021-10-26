from .blog import BlogsApi, BlogApi, BlogsAdmin, BlogAdmin

def initialize_routes(api):
    api.add_resource(BlogsApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<id>')

    api.add_resource(BlogsAdmin, '/api/blogs/admin')
    api.add_resource(BlogAdmin, '/api/blogs/admin/<id>')
