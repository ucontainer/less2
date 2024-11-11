print("Welcome to the Task Menu!")
tasks = []

def viewTask():
    
    if len(tasks) == 0:
        print("\nThere are no tasks to view.\n")
    else:
        print("\n====Task List====")
        for line in tasks:
            print(line)
    
    # for line in tasks:
    #     print(line)
        
    # if len(tasks) == 0:
    #     print("There are no tasks to view.")
            
        
    
    
def addTask():
    prompt = input("Enter a new task: ")
    prompt = str(prompt)
    prompt = prompt.rstrip()
    if prompt == 'quit':
        exit
    else:
        tasks.append(prompt)
        print(f"You have successfully added {prompt}")
        
        

def delTask():

        prompt = input("Enter task to delete: ")
        prompt = prompt.rstrip()
        prompt = prompt.lower()
        if prompt == 'quit':
            exit

        for line in tasks: 
            if line == prompt:
                tasks.remove(line)
                print(f"{prompt} has been deleted")
                break
            else:
                print(f"{prompt} does not exist")
                break
            
   
while True:
    query = input("What would you like to do?\nEnter 'view', 'add', 'delete', or 'quit': ")
    query = query.lower()
    query = query.rstrip()
    if query == 'add':
        addTask()
    elif query == 'view':
        viewTask()
    elif query == 'delete':
        delTask()
    elif query == 'quit':
        break
    else:
        print("Try again..")
     