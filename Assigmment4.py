
class Todo_Item:
    priority_options = ["High", "Medium", "Low"]

    def __init__(self,task:str,priority:str = None,done:bool = False):
        if type(task) == str:
            if task:
                self.task = task
            else:
                raise Exception("Task should not be empty")
        else:
            raise Exception("Task needs to be a string")

        if type(done) == bool:
            self.done = done
        else:
            raise Exception("Done argument needs to be a boolean")

        if priority:
            if priority in Todo_Item.priority_options:
                self.priority = priority
            else:
                raise Exception(f"priority setting should be one of {Todo_Item.priority_options}")
        else:
            self.priority = None

    def __str__(self):
        return f'[{"x" if self.done else "o"}] - {self.priority if self.priority else "None"} : {self.task}'

    def finish(self):
        self.done = True

    def raise_priority(self):
        if not self.priority:
            return

        if self.priority == "Low":
            self.priority = "Medium"
        if self.priority == "Medium":
            self.priority = "High"


class Todo_List:
    def __init__(self,owner:str, todo_list:list = []):

        for item in todo_list:
            if type(item) != Todo_Item:
                raise Exception(f"Expected Todo Item got {type(item)}")

        self.todo_items = todo_list

        if type(owner) == str:
            if owner:
                self.owner = owner
            else:
                raise Exception("Owner name should not be empty")
        else:
            raise Exception("Owner name needs to be a string")

    def __str__(self):
        output = f"{self.owner}'s ToDo List\n"

        for item in self.todo_items:
            output += str(item) + "\n" # For each item, it calls str(item), which in turn calls the __str__ method of the Todo_Item class

        return output

    def info(self):
        pending_tasks = {"High": 0, "Medium": 0, "Low": 0}
        finished_tasks = 0

        for item in self.todo_items:
            if item.done:
                finished_tasks += 1
            else:
                if item.priority:
                    pending_tasks[item.priority] += 1

        pending_summary = ", ".join([f"{priority} - {count}" for priority, count in pending_tasks.items()])

        print(f"{self.owner}'s Todo list\n\nPending Tasks: {len(self.todo_items) - finished_tasks} \n{pending_summary}\nFinished Tasks: {finished_tasks}\n------------")

    def add_todo_item(self, todo_item):
        if type(todo_item) == Todo_Item:
            self.todo_items.append(todo_item)
        else:
            raise Exception(f"ToDo item must be of datatype Todo_Item not {type(todo_item)}")

    def create_todo_item(self,task:str,priority:str = None,done:bool = False):
        item = Todo_Item(task, priority,done)
        self.todo_items.append(item)

    # output of this function should be the tofo items filtered based on the query
    def search_todo_item(self, query):
        output = []
        count=0
        for items in self.todo_items:
            if items.task.lower() in query.lower():
                count+=1
                # print(items)
                output.append(str(items))
        if count !=0:
            return f"{output}\n"
        else:
            return "No task was found"
        
    def list_todo_items(self,priority: str=None, done :bool=None,sort:bool=True):
        
        output1=[]
        for item in self.todo_items:
            if done == True and item.done:
                output1.append(item)
            elif done == False and item.done == False:
                output1.append(item)
            elif done==None:
                output1.append(item)
        output2=[]

        if priority == "All":
            output2 =output1
        else:
            for item in output1:
                if priority == item.priority:
                    output2.append(item)
        return output2
      
                     
                    
a = Todo_Item("Prepare for TCS interview",priority="Low")
b = Todo_Item("complete registration of PGCET",priority="High")
c = Todo_Item("Watch T20 worldcup",priority="Low")
d = Todo_Item("complete your homework",priority="High")


my_list = Todo_List("pranay",[a,b,c,d])

#print(my_list)
# my_list.info()
d.finish()

#my_list.info()
#print(my_list.search_todo_item("Prepare for TCS interview"))
#for item in 

r=my_list.list_todo_items(priority="High",done=False)
for i in r:
    print(i)


