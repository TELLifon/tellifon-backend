import os
from flask import Flask
from database.db import initialize_db
from database.s3 import initialize_s3
from flask_restful import Api
from resources.routes import initialize_routes
from cfenv import AppEnv

app = Flask(__name__)
api = Api(app)

env = AppEnv()
mongodb = env.get_service(label='mongodbent')
s3_service = env.get_service(label='dynstrg')

s3_creds['accessHost'] = 'https://{}'.format(s3_service.credentials['accessHost'])
db_uri = mongodb.credentials["database_uri"] if mongodb is not None else 'mongodb://localhost/versusvirus'

app.config['MONGODB_SETTINGS'] = {'host': db_uri}
app.config['S3'] = s3_creds

port = int(os.getenv('PORT', '3000'))

initialize_db(app)
initialize_s3(app)
initialize_routes(api)

app.run(host='0.0.0.0', port=port)