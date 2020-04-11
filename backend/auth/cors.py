from flask import after_this_request


def allow_control_headers(**kw):
    @after_this_request
    def add_headers(response):
        print('entered add headers')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response


cors_preprocessor = {'GET': [allow_control_headers],
                     'POST': [allow_control_headers],
                     'PATCH': [allow_control_headers],
                     'DELETE': [allow_control_headers],
                     'PUT': [allow_control_headers]}
