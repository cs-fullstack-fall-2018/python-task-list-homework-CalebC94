my_file = open("Task List.py", "w+")

class userList():
    def __init__(self, task = ["groceries"]):
        self.task = task

def main():
    person = userList()
    print("hello")

    while True:
        taskList = input("What would you like to do next? \n 'Add' \n 'Remove' \n 'Check' \n 'End'").lower()
        if taskList != "add" and taskList != "remove" and taskList != "check" and taskList != "end":
            print("Please enter 'add', 'remove', 'check', or 'end'")
            continue
        elif taskList == 'add':
            person.task.append(input("What would you like to add?"))
            continue
        elif taskList == 'remove':
            person.task.remove(input("What would you like to remove?"))
            continue
        elif taskList == 'check':
            print(person.task)
            continue
        elif taskList == 'end':
            break
        else:
            print("Error occurred, self destruct activated")
            break

if __name__ == '__main__':
    main()













# Create a task list

# The text below should show when you run your program:


# print("Congratulations! You're running Caleb's Task List program.")
#
# print("What would you like to do next?")
# print("2. Add a task to the list.")
# print("3. Delete a task.")
# print("4. To quit the program")
#
# class listOptions():

# print()


# Create a different function for selection 1, 2 or 3.

#### Extra Credit. Output the data to a text file. When the program is run again, input that text file.


#### Only use the information below if necessary
#
# To list all items in an array:
#     ```
# To add an item to an array
# ```python
# arrayOfTasks.append(newTask)
# ```python
# for itemInArray in arrayOfTasks:"1. List all tasks.")
# print
# ```
# To check if an item is in an array
# ```python
# if deleteTask in arrayOfTasks:
#     ```
# To delete a task
# ```python
# arrayOfTasks.remove(deleteTask)
