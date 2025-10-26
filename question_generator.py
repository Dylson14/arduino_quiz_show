import os
import functions
import random
import serial
import time

os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

print("Connected to Arduino!")

while True:
    user_action = input("Type add, show, remove, exit or start: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            user_question = input("Write your question: ").strip().title()
            boolean_answer = input("Is your question True or False: ").strip().title()
            
            questions_list = functions.get_questions('questions_list.txt')
            
            questions_list.append([user_question, boolean_answer])
            
            functions.write_questions('questions_list.txt', questions_list)
                
        case 'show':
            questions_list = functions.get_questions('questions_list.txt')
                
            print(questions_list) 
            
        case 'start':
            questions_list = functions.get_questions('questions_list.txt')
            random_question = random.choice(questions_list) 
            print(random_question[0])
            
            user_answer = input("Is this statement true or false? ").strip().title()
            
            if user_answer == random_question[1]:
                print("CORRECT! You're amazing!")
            else:
                print("WRONG! Better luck next time!")
        
        case 'exit':
            print('leaving quiz, thanks for playing')
            break
        
        case _:
            print("Your command is invalid, try again")
    
""" Main functionality of code works, I know need to send this information 
to the Arduino and set up a basic answering board."""

    
            
            