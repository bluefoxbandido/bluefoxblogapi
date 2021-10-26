from flask import Response, request
from database.models import Blog
from flask_restful import Resource

class BlogsApi(Resource):
    def get(self):
        blogs = Blog.objects().to_json()
        return Response(blogs, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        blog = Blog(**body).save()
        id = blog.id
        return {'id': str(id)}, 200

class BlogApi(Resource):
    def get(self, id):
        blog = Blog.objects.get(id=id).to_json()
        return Response(blog, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Blog.objects.get(id=id).update(**body)
        return 'Blog Updated', 200
    
    def delete(self, id):
        Blog.objects.get(id=id).delete()
        return 'Blog Deleted', 200
