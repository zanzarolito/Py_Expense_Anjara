from PyInquirer import prompt
import csv
import ast

user_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New User - Name: ",
    }
]

def get_status():
    # This function should synthesize who owes who
    infos = []
    with open('expense_report.csv', newline='') as file :
        reader = csv.reader(file)
        infos = next(reader)
    people_involved = ast.literal_eval(infos[-1])
    nb_people_involved = len(people_involved)
    spender = infos[2]
    total = infos[0]
    personal_debt = int(total) / nb_people_involved
    for i in range(nb_people_involved) :
        if people_involved[i] == spender :
            print(people_involved[i] + " owes nothing", end='\n' )
        else :
            print(people_involved[i] + " owes " + str(personal_debt) + "€ to " + spender, end='\n' )
    return