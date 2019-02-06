from flask import Blueprint
from flask_restplus import Api

from .exam_schedules import ns as ns_exam_schedules
from .exams import ns as ns_exams
from .mentees import ns as ns_mentees
from .mentors import ns as ns_mentors
from .uploads import ns as ns_uploads
from .users import ns as ns_users
from .universities import ns as ns_universities
from .university_applications import ns as ns_university_applications

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns_exam_schedules)
api.add_namespace(ns_exams)
api.add_namespace(ns_mentees)
api.add_namespace(ns_mentors)
api.add_namespace(ns_uploads)
api.add_namespace(ns_users)
api.add_namespace(ns_universities)
api.add_namespace(ns_university_applications)