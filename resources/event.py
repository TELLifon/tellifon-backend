from flask import Response, request
from database.models import Event, Category
from database.s3 import session
from flask_restful import Resource, reqparse, inputs
import json

class EventsApi(Resource):
    def get(self, id):
        event = Event.objects.get(id=id).to_json()
        return Response(event, mimetype="application/json", status=200)

class EventImageApi(Resource):
    def get(self, id):
        s3 = session.client
        image = s3.get_object(
            Bucket="devbucket0",
            Key=id
        )
        return Response(image['Body'], mimetype=image['ContentType'], status=200)

class EventApi(Resource):
    def __init__(self):
        # workaround to properly parse booleans
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('is_public', type=inputs.boolean, location='form')
        super(EventApi, self).__init__()
    def post(self, id):
        body = request.form
        args = self.reqparse.parse_args()
        event = Event(**body)
        event.is_public = args['is_public']
        event.category_id = Category.objects().get(id=id).id
        event.save()
        if 'image' in request.files:
            file = request.files['image']
            s3 = session.client
            s3.put_object(
                Body=file,
                Bucket="devbucket0",
                ContentType=file.content_type,
                Key=str(event.id))
            event.img_src = '/api/events/{}/image'.format(str(event.id))
            event.save()
        return {'id': str(event.id)}, 200