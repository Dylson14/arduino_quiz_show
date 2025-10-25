import os
import random
import json

os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script

def get_questions(filepath):
    with open(filepath,'r') as file:
                questions_list_local = json.load(file) # returns list
                return questions_list_local

def write_questions(filepath, questions):
    with open(filepath,'w') as file:
                json.dump(questions, file) # performs write() method on each list item

while True:
    user_action = input("Type add, show, remove, exit or start: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            user_question = input("Write your question: ").strip().title()
            boolean_answer = input("Is your question True or False: ").strip().title()
            
            questions_list = get_questions('questions_list.txt')
            
            questions_list.append([user_question, boolean_answer])
            
            write_questions('questions_list.txt', questions_list)
                
        case 'show':
            questions_list = get_questions('questions_list.txt')
                
            print(questions_list) 
            
        case 'start':
            questions_list = get_questions('questions_list.txt')
            random_question = random.choice(questions_list) 
            print(random_question[0])
            
            user_answer = input("Is this statement true or false? ").strip().title()
            
            if user_answer == random_question[1]:
                print("CORRECT! You're amazing!")
            else:
                print("WRONG! Better luck next time!")
                
        case 'remove':
            """ Next case I'll need to work on """   
            
        case 'exit':
            print('leaving quiz, thanks for playing')
            break
        
        case _:
            print("Your command is invalid, try again")
    
""" Main functionality of code works, I know need to send this information 
to the Arduino and set up a basic answering board."""

    
            
            