import os
os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script

questions_list = [] # [("question", True/False)] list contains questions and their respective answers


while True:
    user_action = input("Type add, show, remove, exit or start ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            user_question = input("Write your question: ").strip()
            boolean_answer = input("Is your question True or False: ").strip()
            
            questions_list.append((user_question, boolean_answer))
        case 'show':
            print(questions_list)
        case 'exit':
            print('leaving quiz, thanks for playing')
            break
        case _:
            print("Your command is invalid, try again")
    

    
            
            