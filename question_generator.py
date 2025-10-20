import os
os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script

questions_list = [] # [("question", True/False)] list contains questions and their respective answers


while True:
    user_action = input("To add a question, type add or show: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            print("You've entered the add case")
            
            user_question = input("Write your question: ").strip()
            boolean_answer = input("Is your question True or False: ").strip()
            
            questions_list.append((user_question, boolean_answer))
            print(questions_list)
            
            print("Exiting case")
            break
        case 'show':
            print("Entered show case")
            continue
        case _:
            print("Your command is invalid, try again")
            continue
    
    print("End of While Loop")
    
print("We're outside the while loop")
            
            