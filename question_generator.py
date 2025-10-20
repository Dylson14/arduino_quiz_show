import os
os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script

questions_list = [] # [("question", True/False)] list contains questions and their respective answers
questions_list.append(("question1", True))
questions_list.append(("question2", False))

user_action = input("To add a question, type add: ")
user_action = user_action.strip()

while True:
    match user_action:
        case 'add':
            print("You've entered the add case")
            
            user_question = input("Write your question: ").strip()
            boolean_answer = input("Is your question True or False").strip()
            
            questions_list.append((user_question, boolean_answer))
            
            