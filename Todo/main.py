from todo import Todo_Item, Todo_List, sample_todo
import os



def save_todo_list(todo_list):
    with open(f"./todo_data/{todo_list.owner.lower()}.txt","w") as f:
        lines = []

        for item in todo_list.todo_items:
            if item.priority:
                priority = item.priority
            else:
                priority = "None"

            if item.done:
                done = "True"
            else:
                done = "False"

            task = item.task.replace(","," ")

            line = ",".join([priority,done,task])
            lines.append(line)

        f.write("\n".join(lines))
            


print("Welcome to TODO APP")

while True:
    owner_name = input("Hello, Please enter your name:")
    if owner_name:
        break
    else:
        print("Owner Name cant be empty...")


# try to find the owner
PATH = f"./todo_data/{owner_name.lower()}.txt"
try:
    with open(PATH, "x") as f:
        print(f"Welcome {owner_name} to our TODO app")
        user_list = Todo_List(owner_name)
except:
    print(f"Welcome Back")

    with open(PATH, "r") as f:
        todo_data = f.readlines()
        todo_items = []
        for line in todo_data:
            line = line.replace("\n","")
            priority, done, task = line.split(",")

            if done == "True":
                done = True
            else:
                done = False

            if priority == "None":
                priority = None

            todo_item = Todo_Item(task, priority, done)
            todo_items.append(todo_item)

        user_list = Todo_List(owner_name, todo_items)


while True:
    print("""\n\nWhat do you want to do?
    
    1. Create a new task
    2. View existing task
    3. Mark a task as done
    4. Edit a old task 
    5. Delete a task
    6. Exit

    """)

    while True:
        choice = input("Enter a number (1-6) : ")

        try:
            choice = int(choice)
            if (choice >= 1) and (choice <=6):
                break
            else:
                print("Choice must be between 1-6 ")
        except:
            print("Choice must be a valid number")

    
    # quitting the app
    if choice == 6:
        # saving
        quit()

    # creating new todo item
    elif choice == 1:

        while True:
            task = input("\nTask: ")
            if task:
                break
            else:
                print("Task must not be empty!")

        while True:
            priority = input("\nPriority: ")

            if priority:
                priority = priority.lower().title()

                if priority in ["High", "Medium", "Low"]:
                    break
                else:
                    print("Priority must be one of",["High", "Medium", "Low"])
            else:
                priority = None
                break

        while True:
            done = input("\nDone? (y/N) :")

            if done:
                done = done.lower()
                if done in ["y", "yes"]:
                    done = True
                    break
                elif done in ["n", "no"]:
                    done = False
                    break
                else:
                    print("Done must be one of y / n")
            else:
                done = False
                break
        
        created_item = Todo_Item(task,priority,done)
        print("\nNew task created")
        print(created_item)

        user_list.add_todo_item(created_item)
        save_todo_list(user_list)
    # printing out all the todo items in the owner's todo list
    elif choice == 2:
    #    Todo_List.list_todo_items(priority="All",done=None,sort=False)
        print(f"\n{user_list}")
        pass
    # option to mark task as done
    elif choice == 3:
        value=int(input("Enter your task number to mark done : "))
       # user_list.finish_todo_item(value)
       # save_todo_list(user_list)
        pass
    else:
        print(f"Choice : {choice}")

