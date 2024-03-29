from flask import jsonify
from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity_exception import HttpUnprocessableEntityException


def handle_errors(error: Exception):
    if isinstance(error,HttpUnprocessableEntityException):
        print('HTTP UNPROCESSABLE ENTITY EXCEPTION')
        http_response = HttpResponse({
            'status_code': error.status_code,
            'body': {
                'errors': [{
                    'title': error.name,
                    'detail': error.message
                    }]
                },
        }, error.status_code)
    else:
        http_response = HttpResponse({
            'body': {
                'status_code': 500,
                'errors': [{
                    'title': 'InternalServerError',
                    'detail': str(error)
                }]
            }
        }, 500)

    return jsonify(http_response.body), http_response.status_code
