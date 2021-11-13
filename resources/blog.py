from flask import Response, request
from flask_cors.decorator import cross_origin
from database.models import Blog
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from bson import ObjectId

# _________________________________________________________________________

# Public Consumption -----------------------------------------------------
# _________________________________________________________________________

class BlogsApi(Resource):
    @cross_origin()
    def get(self):
        blogs = Blog.objects().to_json()
        response = Response(blogs, mimetype="application/json", status=200)
        return response


class BlogApi(Resource):
    def get(self, id):
        blog = Blog.objects.get(id = ObjectId(id)).to_json()
        return Response(blog, mimetype="application/json", status=200)
# _________________________________________________________________________
# _________________________________________________________________________

# Authentication Required ------------------------------------------------
# _________________________________________________________________________
class BlogsAdmin(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        image = request.files['file']
        blog = Blog(**body)
        blog.image.put(image, filename=image.filename)
        blog.save()
        id = ObjectId(blog.id)
        return {'id': str(id)}, 200

    @jwt_required()
    def delete(self):
        Blog.objects().delete()
        return 'All blogs deleted', 200


class BlogAdmin(Resource):
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        image = request.files['file']
        blog = Blog.objects.get(id=ObjectId(id))
        blog.update(**body)
        blog.put(image, filename=image.filename)

        return 'Blog Updated', 200

    @jwt_required()
    def delete(self, id):
        Blog.objects.get(id=ObjectId(id)).delete()
        return 'Blog Deleted', 200
# _________________________________________________________________________
# _________________________________________________________________________
