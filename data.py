import requests

NUM = 10  # number of questions, can be 1-50
DIFFICULTY = 'easy'  # quiz difficulty, can be 'easy'/'medium'/'hard', None stands for questions of any difficulty
TYPE = None  # type of questions, 'boolean' for True/False questions, 'multiple' for multiple choice questions, None stands for mixing questions of both types

parameters = {
    'amount': NUM,
    'difficulty': DIFFICULTY,
    'type': TYPE
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
