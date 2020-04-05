from flask import Response, request
from database.models import Category, Event
from flask_restful import Resource
from datetime import datetime, timedelta
import json


class CategoriesApi(Resource):
    def get(self):
        categories = Category.objects().to_json()
        return Response(categories, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        category = Category(**body).save()
        id = category.id
        return {'id': str(id)}, 201


class CategoryApi(Resource):
    def get(self, id):
        timefilter = datetime.now() - timedelta(hours=2)
        category = Category.objects.get(id=id)
        response = json.loads(category.to_json())
        events = json.loads(Event.objects(__raw__={'category_id': category.id, 'endtime': {'$gt': timefilter}, 'img_src': {'$ne':''}, 'is_public': {'$eq': True}}).order_by('+starttime').to_json())
        response["events"] = events
        return Response(json.dumps(response), mimetype="application/json", status=200)
