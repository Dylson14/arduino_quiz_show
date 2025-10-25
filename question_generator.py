import os
os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script

def get_questions(filepath):
    with open(filepath,'r') as file:
                questions_list_local = file.readlines() # returns list
                return questions_list_local

def write_questions(filepath, questions):
    with open(filepath,'w') as file:
                file.writelines(questions) # performs write() method on each list item

while True:
    user_action = input("Type add, show, remove, exit or start: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            user_question = input("Write your question: ").strip()
            boolean_answer = input("Is your question True or False: ").strip()
            
            questions_list = get_questions('questions_list.txt')
            
            questions_list.append(str((user_question, boolean_answer)))
            
            write_questions('questions_list.txt', questions_list)
                
        case 'show':
            questions_list = get_questions('questions_list.txt')
                
            print(questions_list) 
            
        case 'start':
            questions_list = get_questions('questions_list.txt')
            
        case 'exit':
            print('leaving quiz, thanks for playing')
            break
        
        case _:
            print("Your command is invalid, try again")
    

    
            
            