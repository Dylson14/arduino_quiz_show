import os
os.system('cls' if os.name == 'nt' else 'clear')

def get_todos():
    with open("revisions/example.txt", "r") as file:
        todos_local = file.readlines()
    return todos_local

while True: 
    user_action = input("Type add, show, edit, complete or exit: ") # returns str
    user_action = user_action.strip() 
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n" # returns str
            
            todos = get_todos()
            
            todos.append(todo) # adds user_input to todos list
            
            with open("revisions/example.txt", "w") as file:
                file.writelines(todos)
            
        case 'show':
            todos = get_todos()
            
            for index, item in enumerate(todos): 
                item = item.strip('\n') # newly added - strips breaklines from item
                row = f"{index + 1}-{item}" 
                print(row)
            
        case 'edit':
            number = int(input("Number of the todo to edit: ")) 
            number = number - 1
            
            todos = get_todos()
            
            new_todo = input("Enter a new todo: ") + "\n"
            todos[number] = new_todo
            
            with open("revisions/example.txt", "w") as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            
            todos = get_todos()
            
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            
            with open("revisions/example.txt", "w") as file:
                file.writelines(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
                
        case 'exit':
            break # exits the while loop immediately, skips any remaining code
        case _:
            print("Command is not valid")
        
print("Bye")