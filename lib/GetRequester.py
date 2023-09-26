import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        reponse = requests.get(url)
        return reponse.content

    def load_json(self):
        employees = []

        employees_list = json.loads(self.get_response_body())
        for employee in employees_list:
            employees.append(employee)
        return employees