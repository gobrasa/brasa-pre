import datetime
import json

import requests

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


endpoint = 'http://brasa-pre.herokuapp.com/api/mentees'
#endpoint = 'http://localhost:5000/api/mentees'

json1 = dict(
    cycle_start=datetime.datetime(2019,2,18),
    cycle_end=datetime.datetime(2019,8,18),
    region='USA',
    summary='Ciclo USA 1/2019'
    )

mentor = dict(
    cycle_id=1,
    first_name="John",
    last_name="Lennon",
    username="brandon40"
)

mentee = dict(
    username="rparker",
         financial_aid=1
)

r = requests.post(endpoint, data=json.dumps(mentee, cls=DateTimeEncoder),
                  headers={'Content-type': 'application/json'})

print (r, r.content)

