import requests


def get_questions():
    parameters = {
        "amount": 10,
        # "category": 18,
        "type": "boolean"
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    data = response.json()["results"]
    return data


question_data = get_questions()
