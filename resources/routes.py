from .blog import BlogsApi, BlogApi

def initialize_routes(api):
    api.add_resource(BlogsApi, '/api/blogs')
    api.add_resource(BlogApi, '/api/blogs/<id>')