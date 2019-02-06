from database import db
from database.models import User, Role, Mentee, Mentor, Uploads, Exams, ExamSchedule, University, UniversityApplication
from restful_api.Exceptions import RoleNotAllowedException


def create_user(data):
    username = data.get('username')
    email = data.get('email')
    role_name = data.get('role_name')

    user = User(username=username, email=email,
                role_name=role_name)
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

def check_role_name_valid(role_name):

    allowed_role_names = [i.role_name for i in Role.query.all()]

    if role_name not in allowed_role_names:
        raise RoleNotAllowedException('Not allowed role {}'.format(role_name),
                                      'Allowed roles: {}'.format(allowed_role_names))


def update_user(user_id, data):
    user = User.query.filter(User.id == user_id).one()

    user.username = get_default(data, user, 'username')
    user.email = get_default(data, user, 'email')
    user.role_name = get_default(data, user, 'role_name')

    check_role_name_valid(user.role_name)

    User.query.session.add(user)
    User.query.session.commit()

def update_university(id, data):

    university = University.query.filter(University.id == id).one()

    university.name = get_default(data, university, 'name')
    university.city = get_default(data, university, 'city')

    university.state = get_default(data, university, 'state')
    university.country_iso_code = get_default(data, university, 'country_iso_code')

    University.query.session.add(university)
    University.query.session.commit()


def delete_user(user_id):
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()

def create_university(data):

    name = data.get('username')
    city = data.get('city')
    state = data.get('state')
    country_iso_code = data.get('country_iso_code')

    university = University(name=name,
                            city=city,
                            state=state,
                            country_iso_code=country_iso_code)

    db.session.add(university)
    db.session.commit()


def create_university_application(data):

    mentee_id = data.get('mentee_id')
    university_id = data.get('university_id')

    university_application = UniversityApplication(mentee_id=mentee_id,
                            university_id=university_id)

    db.session.add(university_application)
    db.session.commit()

def create_mentor(data):

    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    cycle_id = data.get('cycle_id')

    mentor = Mentor(username=username, first_name=first_name,
                    last_name=last_name, cycle_id=cycle_id)

    db.session.add(mentor)
    db.session.commit()

# ToDo - improve query, probably update mentee
def create_university_application_for_mentee(mentee_id, university_ids):
    # get mentee
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

def create_mentee(data):

    mentor_id = data.get('mentor_id')
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    city = data.get('city')
    state = data.get('state')
    financial_aid = data.get('financial_aid')
    cycle_id = data.get('cycle_id')

    mentee = Mentee(mentor_id=mentor_id,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    city=city,
                    state=state,
                    financial_aid=financial_aid,
                    cycle_id=cycle_id)

    db.session.add(mentee)
    db.session.commit()

def create_upload(data):

    link = data.get('link')
    username = data.get('username')

    upload = Uploads(link=link,
                    username=username)

    db.session.add(upload)
    db.session.commit()

def create_exam(data):

    category = data.get('category')
    subcategory = data.get('subcategory')

    exam = Exams(category=category,
                    subcategory=subcategory)

    db.session.add(exam)
    db.session.commit()

def update_exam(id, data):
    exam = Exams.query.filter(Exams.id == id).one()

    exam.category = get_default(data, exam, 'category')
    exam.subcategory = get_default(data, exam, 'subcategory')

    Exams.query.session.add(exam)
    Exams.query.session.commit()

def update_university_application(id, data):
    university_application = UniversityApplication.query.filter(UniversityApplication.id == id).one()

    university_application.mentee_id = get_default(data, university_application, 'mentee_id')
    university_application.university_id = get_default(data, university_application, 'university_id')

    UniversityApplication.query.session.add(university_application)
    UniversityApplication.query.session.commit()


def create_exam_schedule(data):

    realization_date = data.get('realization_date')
    mentee_id = data.get('mentee_id')
    exam_id = data.get('exam_id')
    score = data.get('score')

    exam_schedule = ExamSchedule(realization_date=realization_date,
                                 mentee_id=mentee_id,
                                 exam_id=exam_id,
                                 score=score)

    db.session.add(exam_schedule)
    db.session.commit()

def update_exam_schedule(id, data):
    exam_schedule = ExamSchedule.query.filter(ExamSchedule.id == id).one()

    exam_schedule.realization_date = get_default(data, exam_schedule, 'realization_date')

    exam_schedule.mentee_id = get_default(data, exam_schedule, 'mentee_id')
    exam_schedule.exam_id = get_default(data, exam_schedule, 'exam_id')
    exam_schedule.score = get_default(data, exam_schedule, 'score')

    ExamSchedule.query.session.add(exam_schedule)
    ExamSchedule.query.session.commit()

def get_default(data, obj,param):
    return data.get(param) if data.get(param) else obj.__getattribute__(param)

def update_mentee(id, data):
    mentee = Mentee.query.filter(Mentee.id == id).one()

    mentee.mentor_id = get_default(data, mentee, 'mentor_id')
    mentee.first_name = get_default(data, mentee, 'first_name')
    mentee.last_name = get_default(data, mentee, 'last_name')
    mentee.city = get_default(data, mentee, 'city')
    mentee.state = get_default(data, mentee, 'state')
    mentee.financial_aid = get_default(data, mentee, 'financial_aid')
    mentee.cycle_id = get_default(data, mentee, 'cycle_id')

    Mentee.query.session.add(mentee)
    Mentee.query.session.commit()

def update_mentor(id, data):
    mentor = Mentor.query.filter(Mentor.id == id).one()

    mentor.first_name = get_default(data, mentor, 'first_name')
    mentor.last_name = get_default(data, mentor, 'last_name')
    mentor.cycle_id = get_default(data, mentor, 'cycle_id')

    Mentor.query.session.add(mentor)
    Mentor.query.session.commit()

def update_upload(id, data):
    upload = Uploads.query.filter(Uploads.id == id).one()

    upload.link = get_default(data, upload, 'link')

    Uploads.query.session.add(upload)
    Uploads.query.session.commit()

def delete_from_table(class_var, id):
    db.session.query(class_var).filter(class_var.id == id).delete()
    db.session.commit()