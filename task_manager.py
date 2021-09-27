import os
import sys
# Create a program to help a small business manage tasks assigned to team members.
# Use the lower() function throughout the program to avoid case sensitive errors.

# Import pretty printing to help with formatting, exit to exit the program and datetime for the generate report function.
from pprint import pprint
from sys import exit 
import datetime

# open the user text file in read mode to create a login program for all registered users.
with open (os.path.join(sys.path[0],"user.txt"), "r+") as login_file:
# Create a while loop to allow or deny access for users.
# Create a boolean that is false.
# Check if the username and password matches the saved ones in the user text file.
    login = False

    while not login:
        login_username = input("Please enter your Username: ").lower() 
        login_password = input("Please enter your Password: ").lower()
        login = False

# Run through the file line by line.
# Assign username and password to the line in text file.
        for line in login_file:
            username, password = line.strip().split(", ")

# Use the boolean to allow access for correct username and password. 
            if login_username == username and login_password == password:
                login = True
                print ("Welcome " + login_username + "!")

# Use the boolean again if username and password don't match.
# The loop will continue until username and password do match.
# Seek function tells the program to start reading from the top of the file again.
        if login == False:
            print ("Something went wrong. You have entered either an invalid username or an invalid password.")

        login_file.seek(0)


# This function will print out with correct login and the user can pick an action. 
def main_menu():

    print("""
    MENU:
    r - register a user
    a - add a task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - exit
    """)


# Create a function to prevent admin from registering the same user twice.
def reg_user():

# Open user text file in read mode.
    login_file = open (os.path.join(sys.path[0],"user.txt"), "r+")

# Use if/else boolean to allow only admin access.
    if login_username == "admin" and login_password == "adm1n":
        login = True
        register = login_file.read().split('\n')

# Run a while loop that requests username and prevents duplicates.
        ok = False
        while not ok:
            username = input("Please enter the name of the user you would like to register:\n")
            ok = True
            for line in register:
# Check the username against the 1st index of the list.
                if username == line.split(', ')[0]:
                    print("Sorry, that username is taken. Try a different one.")
                    ok = False

# Double check that the passwords match.
        password = input("Please enter a password to register:\n")
        passcheck = input("Please re-enter your password:\n")

# Allow admin to try again if the password doesn't match.
        if password != passcheck:
            print("Your password doesn't match. Please re-enter your password.")
        else:
            print("Thank you. You've successfully registered a new user")

# Write the new user and their password to the user text file and close the file.
        username = login_file.write("\n" + username + ", " + password)
        login_file.close()

# Let all users other than admin that this is a restricted access.
    else: 
        print ("Restricted access!")


# Create a function that adds details of a task to be done and write it to task file.
def add_task():
# Ask the user to input the details. Date fomat is specified to match the format of datetime funcion.     
    tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "a")
    user = input("Enter the user that you are assigning this task to: ").lower()
    task = input("Enter the title of the task: ")
    desc = input("Enter the description of the task: ")
    start_date = input("Enter the start date (Please format the date as: 00-00-0000): ")
    end_date = input("Enter the completion date (Please format the date as: 00-00-0000): ")
    is_fin = input("Is the task completed: ").lower()
    print ("Thank you. You have successfully loaded a task for " + user + ".")
# Format and write the details to tasks text file on separate lines for easy reading. Don't forget to close the file.
    tasks_file.write(f"\n{user}, {task}, {desc}, {start_date}, {end_date}, {is_fin}")
    tasks_file.close()



# Create a function that will allow all registered users to view all tasks that have been assigned.
def view_all():
# Open task_file and print the formatted information onto the screen.
    tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "r+")
    for line in tasks_file:
# Split the line that has all of the info and format to display it on separate lines.
        user, task, desc, start_date, end_date, is_fin = line.strip().split(", ")
        print(f"""
        User: {user}
        Task: {task}
        Desc: {desc}
        Start Date: {start_date}
        End Date: {end_date}
        Completed: {is_fin}
        """)
    tasks_file.close()


# This function will show the tasks for a specified user and allow the user to edit certain areas of the task.
def view_mine():
    username = input("Please verify your username: ").lower()
    tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "r+")
    num_task = 0
    
    for line in tasks_file:
        user, task, desc, start_date, end_date, is_fin = line.strip().split(", ")  
        num_task += 1

# Use the input variable to print out the tasks of the desired user.        
        if user == username:
            print(f"""
            Task Number: {num_task}
            User: {user}
            Task: {task}
            Desc: {desc}
            Start Date: {start_date}
            End Date: {end_date}
            Completed: {is_fin}
            """)
    tasks_file.close()
   
# Change the info in the file to dictionary data. The columns will be the keys for the values in the lines of the task file.
    tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "r+")
    data = []
# Use variables to store and user the users input.    
    
    columns = ['User', 'Task', 'Desc', 'Start Date', 'End Date', 'Completed']

    for line in tasks_file:
        data.append(dict(zip(columns, line.strip().split(', '))))
        
    for task in data:
        task_edit = input("If you would you like to edit a task enter 'edit' or '-1' to return to main menu. ").lower()
        if task_edit == "edit":
            num_edit = int(input("Which task number would you like to edit? "))

# The lines in the file count from zero so -1 from the task number to match it to the correct line.
            num_num_edit = data[num_edit-1]
            complete_edit = input("Would you like to Mark This Task as Complete? 'yes' Or would you like to Edit the task? 'edit' ").lower()

# This will change the no to a yes in the task file and mark it as complete.       
            if complete_edit == "yes":
                data[num_edit-1]['Completed'] = complete_edit
                print ("Thank you, your task has been marked as complete.")

# If the user doesn't want to mark as complete, then the user if offered to edit the user and due-date of the task.       
            elif complete_edit == 'edit':
                user_edit = input("Which user would you like to assign Task " + str(num_edit) + " to? ").lower()
# This will change the user that the task is assigned to.
                data[num_edit-1]['User'] = user_edit
# This will change the due date of the task.
                due_date_edit = input("Which date is this task due? (Please format the date as: 00-00-0000) ").lower()
                data[num_edit-1]['End Date'] = due_date_edit
                print ("Thank you, task " + str(num_edit) + " has been edited.")
            else:
                main_menu()
# Close the file in read mode.
        tasks_file.close()


#   tasks_file.close()
        tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "w+")
#    for task in data:
        text = '\n'.join(', '.join(record.values()) for record in data)       
        tasks_file.write(text)
        tasks_file.close()


# This function will open the user and task text files and use the information.
# Then once the stats have been created, it will write the stat information to user_overview and task_overview text files.
def generate_reports():
# Open the task file in read mode and store the inormation as a dictionary.
    tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "r+")
    data = []
    columns = ['User', 'Task', 'Desc', 'Start Date', 'End Date', 'Completed']

    for line in tasks_file:
        data.append(dict(zip(columns, line.strip().split(', '))))

# Start the counters at zero
    task_count = len(data)
    task_yes_count = 0
    task_no_count = 0
    task_overdue_count = 0

# Gather the information to calculate percentages.
    for task in data:
        
        if task['Completed'] == 'yes':
            task_yes_count += 1
        
        elif task['Completed'] == 'no':
            task_no_count += 1

# Use the datetime function to calculate overdue tasks.
            if datetime.datetime.strptime(task['End Date'], "%d-%m-%Y").date() < datetime.date.today():
                task_overdue_count += 1

# Calculate the percentages.    
    task_no_percentage = round((task_no_count/task_count)*100, 2)
    task_overdue_percentage = round((task_overdue_count/task_count)*100, 2)

# Create and open the task_overview text file in write mode.
    task_overview_file = open ("task_overview.txt", "w+")
# Write the formatted stats to the task_overview file.
    task_overview_file.write(f"""
Total number of tasks: {task_count}
Total number of completed tasks: {task_yes_count}
Total number of incomplete tasks: {task_no_count}
Total number of overdue tasks: {task_overdue_count}
Total percentage of incomplete tasks: {task_no_percentage}%
Total percentage of overdue tasks: {task_overdue_percentage}%
""")

# Close both files.
    task_overview_file.close()
    tasks_file.close()

# Ask admin for the user they would like to generate stats for.
# Open the tasks file in read mode and store the information as a dictionary.
    username = input("Please enter the name of the user to generate their report: ").lower()
    tasks_file = open (os.path.join(sys.path[0],"tasks.txt"), "r+")
    data = []
    columns = ['User', 'Task', 'Desc', 'Start Date', 'End Date', 'Completed']
    
    for line in tasks_file:
        data.append(dict(zip(columns, line.strip().split(', '))))
# Start the counters at zero.
    task_count = len(data)
    user_yes_count = 0
    user_no_count = 0
    user_overdue_count = 0
    num_user_count = 0

# Gather the information to calculate percentages.
    for user in data:
        if user['User'] == username:       
            num_user_count += 1
            if user['Completed'] == "yes":
                user_yes_count += 1
            elif user['Completed'] == 'no':
                user_no_count += 1

# Use the datetime function to calculate overdue tasks.                   
                if datetime.datetime.strptime(user['End Date'], "%d-%m-%Y").date() < datetime.date.today():
                    user_overdue_count += 1

# Calculate the percentages.
    tasks_user_percentage = round((num_user_count/task_count)*100, 2)
    tasks_yes_percentage = round((user_yes_count/num_user_count)*100, 2)
    tasks_no_percentage = round((user_no_count/num_user_count)*100, 2)
    user_overdue_incomplete = round(((user_overdue_count + user_no_count)/ task_count)*100, 2)

# Open the user task file in read mode to get the number of users.
    login_file = open (os.path.join(sys.path[0],"user.txt"), "r+")
    data = []
    columns = ['username', 'password']
    for line in login_file:
        data.append(dict(zip(columns, line.strip().split(', '))))
        user_count = len(data)

# Create and open the user_overview text file in write mode.
    user_overview_file = open ("user_overview.txt", "w+")
# Write the formatted information to the user_overview text file.
    user_overview_file.write(f"""                
Total number of registered users: {user_count}
Total number of tasks: {task_count}
Total number of tasks for: {num_user_count}
Total percentage of tasks assigned to user: {tasks_user_percentage}%
Total percentage of complete tasks for user: {tasks_yes_percentage}%
Total percentage of incomplete tasks for user: {tasks_no_percentage}%
Total percentage of incomplete and overdue tasks for user: {user_overdue_incomplete}%
""")

# Close all the files
    user_overview_file.close()
    tasks_file.close()
    login_file.close()

# This function will read the information from the user_overview and task_overview text files and display is neatly on the screen.
def display_stats():
# Open the task_overview text file in read mode to give admin some stats.
    task_overview_file = open ("task_overview.txt", "r+")
    user_overview_file = open ("task_overview.txt", "r+")

    if login_username == "admin":
        print ("TASK OVERVIEW:")
        lines = task_overview_file.readlines()
        for line in lines:
            print (line)

        print ("USER OVERVIEW")
        lines = user_overview_file.readlines()
        for line in lines:
            print (line)

# Let all other users know this section is not available to them.
    else:
        print ("Restricted access!")

    task_overview_file.close()
    user_overview_file.close()


# Login is open, so call the menu and start the while loop.
# The user will be able to continually run through the menu until exit is pressed.
main_menu()

while True:
    main_menu = input("Please enter your menu option: ").lower()
    if main_menu == "r":
        reg_user()

    elif main_menu == "a":
        add_task()

    elif main_menu == "va":
        view_all()
    
    elif main_menu == "vm":
        view_mine()
    
    elif main_menu == "gr":
        generate_reports()

    elif main_menu == "ds":
        display_stats()

    elif main_menu == "e":
        exit()


