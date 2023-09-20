from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New User - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as file :
        writer = csv.writer(file)
        writer.writerow(infos.values())
    return