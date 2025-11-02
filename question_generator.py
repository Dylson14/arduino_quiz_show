import os
import functions
import random
import serial
import time

os.system('cls' if os.name == 'nt' else 'clear') # clears terminal when running Python Script
arduino = serial.Serial('COM8', 9600, timeout=1)
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
            """ Here is where I need to send data to arduino """
            questions_list = functions.get_questions('questions_list.txt')
            random_question = random.choice(questions_list) 
            
            arduino.write((random_question[0] + '\n').encode()) # sends data to Arduino in bytes
            
            print("Waiting for answer...")
            
            # wait for user to press a btn and Arduino to send answer back
            # data = arduino.readline() # receives data from Arduino in bytes b'True\n' (bytes)
            # data = data.decode() # converts data into string; 'True\n' (string)
            # data = data.strip() # removes the '\n'; 'True'
            # The above code can be chained together to give:
            
            # Wait for and read Arduino's response
            user_answer = arduino.readline().decode().strip()
            
            print(f"User answered: {user_answer}")
            print(f"Correct answered: {random_question[1]}")
            
            # Compare answers
            if user_answer == random_question[1]:
                arduino.write(b'Correct!\n')
                print("Correct!")
            else:
                arduino.write(b'Wrong!\n')
                print("Wrong!")
            
            
        case 'exit':
            print('leaving quiz, thanks for playing')
            time.sleep(0.5) 
            arduino.close()
            break
        
        case _:
            print("Your command is invalid, try again")
    