from typing import NamedTuple, List, Callable

import flask
from flask import request

from database.models import Mentee, UniversityApplication
from database import db

RoutesEndpointsDef = NamedTuple('routes_endpoints_def',
                                [('url', str), ('methods', List), ('function', Callable)])

def return_routes_for_logic_endpoints():
    """
    Defines routes structure for logic endpoints, which will then be registered in the main
    Flask app.
    :return:
    """
    return [
        RoutesEndpointsDef(url='/university_application_for_mentee',
                           methods=['POST'],
                           function=define_university_application_for_mentee),
    ]

def define_university_application_for_mentee():
    # get mentee

    request_json = request.get_json()
    mentee_id = request_json['mentee_id']
    university_ids = request_json['university_ids']

    print('mentee_id {}, university_ids {}'.format(mentee_id, university_ids))

    mentee = Mentee.query.filter(Mentee.id == mentee_id).one()

    # delete all mappings, push
    for univ_app in mentee.university_applications:
        db.session.delete(univ_app)
        db.session.commit()

    # add university applications

    mentee = Mentee.query.filter(Mentee.id == mentee_id).one()
    for univ_id in university_ids:
        mentee.university_applications.append(
            UniversityApplication(
                mentee_id=mentee_id,
                university_id=univ_id))

    # post
    Mentee.query.session.add(mentee)
    Mentee.query.session.commit()

    return 'University applications from mentee {} successfully updated'.format(mentee_id), 200

class EndpointLogicConfigurator:

    def __init__(self, routes_endpoint_def = return_routes_for_logic_endpoints()):
        self.routes_endpoints_def = routes_endpoint_def

    def configure_logic_endpoints(self, app: flask.app):

        for url,methods,function in self.routes_endpoints_def:
            app.add_url_rule(url, view_func=function, methods=methods)

        return app
