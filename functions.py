import json

def get_questions(filepath):
    with open(filepath,'r') as file:
                questions_list_local = json.load(file) # returns list
                return questions_list_local

def write_questions(filepath, questions):
    with open(filepath,'w') as file:
                json.dump(questions, file) # performs write() method on each list item