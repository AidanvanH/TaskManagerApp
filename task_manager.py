#=====importing libraries===========
from datetime import datetime
#====Login Section====

usernames = []
passwords = []

with open('user.txt', 'r') as users:

    for line in users:
        line_split = line.strip('\n').split(', ')   # Strips the newline character from passwords
        usernames.append(line_split[0])     # Appends each username to list
        passwords.append(line_split[1])     # Appends each password to list


while True:

    username = input('Enter your username: ')

    if username.strip() != '':      # Checks to see if the username entered is whitespace or not
        if username in usernames:   

            while True:

                try:    # Checks to see if password is in the password list, if not asks user to try again
                    password = input('Enter your password: ')
                    if password.strip() != '':
                        # Finds the username's index to see if the password they entered has corresponding indices
                        username_index = usernames.index(username) 
                        password_index = passwords.index(password)
                        if password in passwords and username_index == password_index:  
                            print('Access granted')
                            break
                        else:
                            print('Password is incorrect. Try again')
                    else:
                        print('Please enter a valid password')
                except ValueError:
                    print('Password is incorrect')
            break
        else:
            print(username + ' does not exist. Please enter valid username')
    else:
        print('Please enter a valid username')

def register_user():


    while username == 'admin':      # If user is not admin, it prevents them from registering a new user

        while True:     # Repeatedly asks admin to enter a new username if they enter empty space

            new_user = input('Please enter new username: ')
            if new_user.strip() != '':

                while True:
                    new_password = input("Enter new user's password: ")
                    if new_password.strip() != '':

                        while True:
                            confirm_new_password = input("Confirm new user's password: ")
                            if confirm_new_password.strip() != '':
                                if confirm_new_password == new_password:
                                    usernames.append(new_user)
                                    passwords.append(new_password)

                                    with open('user.txt', 'a') as f:
                                        f.write('\n'+new_user+', ')
                                        f.write(new_password)

                                    print('New user successfully added')
                                    break
                                else:
                                    print('Passwords do not match')
                            else:
                                print()
                        break
                    else:
                        print('You have not entered a password')
                break
            else:
                print('You have not entered a username')
        break

def add_task():

        
    while True:
    
        name_task = input('Who are you assigning the following task to: ')
        if name_task not in usernames:
            print("That user doesn't exist")
        else:
            break

    while True:

        title_task = input('What is the title of the task that you would like to assign to ' + name_task +': ')

        if title_task.strip() == '':
            print('You left the title empty')
        else:
            break
    
    while True:

        description_task = input('Enter a description for the task: ')

        if description_task.strip() == '':
            print("You left the task's description empty")
        else:
            break

    cdt = datetime.now()
    current_date_task = cdt.strftime('%d %b %Y')    # Getting today's current date for 'task assigned' section

    while True:

        due_date_task = input('What is the due date for this task: ')

        if due_date_task.strip() == '':
            print("You left the task's due date empty")
        else:
            break

    def assign_task(name=name_task, title=title_task, description=description_task, current_date=current_date_task, due_date=due_date_task, completed='No'):
        

        with open('tasks.txt', 'a') as t:
            t.write('\n'+name+', ')
            t.write(title+', ')
            t.write(description+', ')
            t.write(current_date+', ')
            t.write(due_date+', ')
            t.write(completed)
        
    assign_task()

def view_all():


    # Assigning empty variables which will later contain all the tasks information
    user_task = ''
    user_name = ''
    user_date = ''
    user_due_date = ''
    user_complete = ''
    user_description = ''
    
    with open('tasks.txt', 'r') as t:
        for line in t:
            # Preventing the newline character from adding empty lines between sections
            all_info = line.strip().split(', ')    
        
            user_task += 'Task:\t\t\t' + all_info[1]
            print('\n'+user_task)
            user_task = ''      # Emptying the string so that the previous lines info is not carried over

            user_name += 'Assigned to:\t\t' + all_info[0]
            print(user_name)
            user_name = ''

            user_date += 'Date assigned:\t\t' + all_info[3]
            print(user_date)
            user_date = ''

            user_due_date += 'Due date:\t\t' + all_info[4]
            print(user_due_date)
            user_due_date = ''

            user_complete +=  'Task complete?\t\t' + all_info[-1]
            print(user_complete)
            user_complete = ''

            user_description += 'Task description:\t' + all_info[2]
            print(user_description+'\n')
            user_description = ''

def view_my():

        
    user_task_2 = ''
    user_name_2 = ''
    user_date_2 = ''
    user_due_date_2 = ''
    user_complete_2 = ''
    user_description_2 = ''
    
    with open('tasks.txt', 'r') as t:
        for line in t:
            info = line.strip().split(', ')
            # Checking to see if the user's username matches the name who the task has been assigned to
            if info[0] == username:     

                user_task_2 += 'Task:\t\t\t' + info[1]
                print('\n'+user_task_2)
                user_task_2 = ''

                user_name_2 += 'Assigned to:\t\t' + info[0]
                print(user_name_2)
                user_name_2 = ''

                user_date_2 += 'Date assigned:\t\t' + info[3]
                print(user_date_2)
                user_date_2 = ''

                user_due_date_2 += 'Due date:\t\t' + info[4]
                print(user_due_date_2)
                user_due_date_2 = ''

                user_complete_2 +=  'Task complete?\t\t' + info[-1]
                print(user_complete_2)
                user_complete_2 = ''

                user_description_2 += 'Task description:\t' + info[2]
                print(user_description_2+'\n')
                user_description_2 = ''  

            else:
                pass

def statistics():

    
    with open('tasks.txt', 'r') as t:
        total_tasks = []   
        for line in t:
            '''Splits the tasks in tasks.txt at their respective newline characters and appends
              it to empty list in order to get the total tasks'''          
            total_tasks.append(line.split('\n')) 
        print('\nThere are a total of ' + str(len(total_tasks)) + ' tasks in the system')

    with open('user.txt', 'r') as u:
        total_users = []
        for line in u:
            '''Splits the users in user.txt at their respective newline characters and appends
              it to empty list in order to get the total users''' 
            total_users.append(line.split('\n'))
        
        if len(total_users) <= 1:
            print('There is a total of ' + str(len(total_users)) + ' user in the system')
        else:
            print('There are a total of ' + str(len(total_users)) + ' users in the system')
        
def exit_():


    print('Goodbye!!!')
    exit()


while username != 'admin':      # This menu is provided to all non-admin users

    menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()      # Converts all input to lower case
    
    if menu == 'r':

        register_user()

    elif menu == 'a':

        add_task()


    elif menu == 'va':

        view_all()


    elif menu == 'vm':

        view_my()

    elif menu == 'e':

        exit_()

    else:
        print("You have made entered an invalid input. Please try again")



while username == 'admin':      # This menu is provided to the admin
    
    menu_admin = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - view statistics 
e - exit
: ''').lower()
    
    if menu_admin == 'r':

        register_user()

    elif menu_admin == 'a':

        add_task()

    elif menu_admin == 'va':

        view_all()

    elif menu_admin == 'vm':

        view_my()

    elif menu_admin == 's':

        statistics()

    elif menu_admin == 'e':

        exit_()

    else:

        print('You have made entered an invalid input. Please try again')




# I needed to do additional research on how to prevent the user from entering whitespace in the various inputs provided
# and this article helped me to do that. I got the idea for using the .strip() method along with while loops to repeatedly
# ask users to provide input if they haven't before.
# https://stackoverflow.com/questions/2405292/check-if-string-contains-only-whitespace

# I made additional research on how to access the index of values in lists and I used this knowledge to make sure that
# the user's username in the username list was situated at the same index as the user's password in the password list.
# This would prevent users from potentially acquiring the passwords of their fellow users by logging in with their own
# username and repeatedly throwing guesses at the system in an attempt to guess others' passwords correctly.
# https://www.programiz.com/python-programming/methods/list/index

# Lastly, I used the datetime module to get the current date for the section in tasks.txt that required the date that
# the task was assigned. I made use of the following article.
# https://docs.python.org/3/library/datetime.html