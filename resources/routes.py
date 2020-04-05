from .category import CategoriesApi, CategoryApi
from .event import EventApi, EventsApi, EventImageApi

def initialize_routes(api):
    api.add_resource(CategoriesApi, '/api/categories')
    api.add_resource(CategoryApi, '/api/categories/<string:id>')
    api.add_resource(EventsApi, '/api/events/<string:id>')
    api.add_resource(EventImageApi, '/api/events/<string:id>/image')
    api.add_resource(EventApi, '/api/categories/<string:id>/events')