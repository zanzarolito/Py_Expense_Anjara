from PyInquirer import prompt, print_json
import csv


def get_users():
    users = []
    with open('users.csv', newline='') as users_file:
        reader = csv.reader(users_file)
        for user in reader:
            users.append(user[0])
    return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Who is the Spender ?: ",
        "choices": get_users(),
    },
]

def get_payback(spender):
    users = []
    with open('users.csv', newline='') as users_file:
        reader = csv.reader(users_file)
        for user in reader:
            if user[0] == spender :
                users.append({'name' : user[0], 'checked' : True})
            else :
                users.append({'name' : user[0]})
    payback = [
     {
        "type":"checkbox",
        "name":"payback",
        "message":"New Expense - Who are the people involved ?: ",
        "choices": users,
        'validate': lambda answer: 'You must choose at least one person.'
            if len(answer) == 0 else True
    },
    ]
    answer = prompt(payback)
    return answer



def new_expense(*args):
    infos = prompt(expense_questions)
    payback_answer = get_payback(infos['spender'])

    answer_list = list(infos.values())
    answer_list.append(payback_answer["payback"])
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'w', newline='') as file :
        writer = csv.writer(file)
        writer.writerow(answer_list)
    return True


