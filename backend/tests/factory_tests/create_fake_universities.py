import requests

endpoint = 'http://brasa-pre.herokuapp.com/api/mentees'
json1 = dict(
    city="Marília",
    cycle_id=1,
    financial_aid=True,
    mentor_id=2,
    state="SP",
    username ="brandon40"
    )

r = requests.post(endpoint, json=json1)

print (r, r.content)


if __name__ == "__main__":

    mentee_creator = MenteeCreator()
    mentee_creator.create_fake_mentees(n=1)
