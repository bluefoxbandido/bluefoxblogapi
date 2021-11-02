from flask import Response, request
from flask_cors.decorator import cross_origin
from database.models import Blog
from flask_restful import Resource

from flask_jwt_extended import jwt_required

# _________________________________________________________________________

# Public Consumption -----------------------------------------------------
# _________________________________________________________________________

class BlogsApi(Resource):
    def get(self):
        blogs = Blog.objects().to_json()
        return Response(blogs, mimetype="application/json", status=200)


class BlogApi(Resource):
    def get(self, id):
        blog = Blog.objects.get(id=id).to_json()
        return Response(blog, mimetype="application/json", status=200)
# _________________________________________________________________________
# _________________________________________________________________________

# Authentication Required ------------------------------------------------
# _________________________________________________________________________
class BlogsAdmin(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        blog = Blog(**body).save()
        id = blog.id
        return {'id': str(id)}, 200

    @jwt_required()
    def delete(self):
        Blog.objects().delete()
        return 'All blogs deleted', 200


class BlogAdmin(Resource):
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        
        print(body)
        Blog.objects.get(id=id).update(**body)
        return 'Blog Updated', 200

    @jwt_required()
    def delete(self, id):
        Blog.objects.get(id=id).delete()
        return 'Blog Deleted', 200
# _________________________________________________________________________
# _________________________________________________________________________
