import mysql.connector
import datetime

#Connecting to mariadb
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="password", 
    database="taskrecordDUMP"
)

mycursor = mydb.cursor() #make the connection to execute SQL queries

def database(): #function that makes a database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS taskrecordDUMP")
      #use the created database
    mycursor.execute("USE taskrecordDUMP;")
        #create a table for category
    mycursor.execute("CREATE TABLE IF NOT EXISTS category (category_no INT(20) NOT NULL,category_name VARCHAR(20) NOT NULL, datecreated DATE, CONSTRAINT categorynopk PRIMARY KEY (category_no))")
        #create a table for task
    mycursor.execute("CREATE TABLE IF NOT EXISTS task (task_no INT(3) NOT NULL,category_no INT(20),task_name VARCHAR(50) NOT NULL,due_date DATE, datecreated DATE ,description VARCHAR(50),status VARCHAR(20) NOT NULL, CONSTRAINT tasktaskno PRIMARY KEY (task_no), CONSTRAINT takscategorynofk FOREIGN KEY(category_no) REFERENCES category(category_no))")

def PrintMenu (): #function that show menu, which shows different tasks that are available
    print("\nKindly enter a choice in the menu below") #print
    print("\n---------- Menu ----------") #print
    print("[1] Add a category") #print
    print("[2] Edit a category") #print
    print("[3] Delete a category") #print
    print("[4] View category") #print
    print("[5] Add a task to a category") #print
    print("[6] Edit a task") #print
    print("[7] Delete a task") #print
    print("[8] View all tasks") #print
    print("[9] Mark task as done") #print
    print("[10] View task today")
    print("[11] View task for this month")
    print("[0] Exit") #print
    print("--------------------------") #print

def EnterCategoryName(): #function that adds category name
    categoryname = input("\nEnter category name (Maximum of 50 characters): ") #input from the user
    if (len(categoryname)>50): #condition for the length of the category name
        print("\nCategory name entries shall only be up to 50 characters. Please try again.") #prompt
        categoryname = EnterCategoryName() #ask for another input of category name
    elif (categoryname == " "): #condition if the category name is null
        print("\nCategory name must not be null. Please try again.") #prompt
        categoryname = EnterCategoryName() #ask for another input of category name
    return categoryname #return the category name if the input is valid

def EnterCategoryNo(): #function that adds category number
    mycursor = mydb.cursor() #make the connection to execute SQL queries
    sql_command = "SELECT * FROM category" #sql command to select all columns in the category table
    mycursor.execute(sql_command) #excute the sql command above
    myresult = mycursor.fetchall() #returns all the row from the table category
    
    try: #if there are already categories
        mycursor = mydb.cursor() #make the connection to execute SQL queries
        sql_command = "SELECT MAX(category_no) as 'maximum' FROM category" #sql command to select the maximum value of category number in the category table
        mycursor.execute(sql_command) #excute the sql command above
        myresult = mycursor.fetchone() #returns the record of the maximum category number
        myresult = myresult[0] 
        myresult = myresult+1 #the value of the category number
        return myresult #returns the value of the category number
    except: #if there is no category
        return 1 #the first category number is 1

def EnterTaskName(): #function that adds task name
    taskname = input("\nEnter task name (Maximum of 50 characters): ") #input from the user
    if (len(taskname)>50): #condition for the length of the task name
        print("\nTask name entries shall only be up to 50 characters. Please try again.") #prompt
        taskname = EnterTaskName() #ask for another input of task name
    elif (taskname == " "): #condition if the task name is null
        print("\nTask name must not be null. Please try again.") #prompt
        taskname = EnterTaskName() #ask for another input of task name
    return taskname #return the task name if the input is valid

def EnterTaskDesc(): #function that adds description of the task
    description = input("\nEnter task description (Maximum of 50 characters): ") #input from the user
    if (len(description)>50): #condition for the length of the task description
        print("\nTask descriptions entries shall only be up to 50 characters. Please try again.") #prompt
        description = EnterTaskDesc() #ask for another input of task description
    elif(description == " "): #condition if the task description is null
        print("\nTask description must not be null. Please try again.") #prompt
        description = EnterTaskDesc() #ask for another input of task description
    return description #return the task description if the input is valid

def EnterTaskStatus(): #function that adds status on the task
    statuslist = ["not yet started", "ongoing", "done"] #list of possible values of status
    status = input("\nEnter task status (Status can only be one of the following: 'Not yet started', 'Ongoing', or 'Done'): ") #input from the user
    if (status.lower() not in statuslist): #the input status is not on the list of possible values
        print("\nTask status entries shall only be one of the following: 'Not yet started', 'Ongoing', or 'Done'. Please try again.") #prompt
        status = EnterTaskStatus() #ask for another input of task description
    return status #return the status of the task if the input is valid 

def EnterTaskCategory(): #function that adds task on the category
    mycursor = mydb.cursor() #make the connection to execute SQL queries
    print("\nThe following are the available categories created: ") #print
    sql_command = "SELECT category_no, category_name FROM category" #sql command to select the category number and name from the table category
    mycursor.execute(sql_command) #execute the sql command
    myresult = mycursor.fetchall() #returns all the rows from the column category number and name from the table category
    categorylist = [] #array
    for row in myresult: #for loop
        print('['+str(row[0])+']', row[1]) #printing list of category name
        categorylist.append(row[0]) #to record in a list 
    
    while(True): #while loop
        try:
            taskcategory = int(input("\nEnter the number of the category you would like to add the task to (Note: All tasks must be under a category): ")) #input from the user
            if taskcategory in categorylist: #condition if the selected category is in the list
                return taskcategory #returns the selected category 
            else:
                print("\nThe category you entered does not exist!") #prompt
        except:
            print("\nInvalid category number entry. Please try again.") #prompt

def EnterTaskNo():#function that adds a task number
    mycursor = mydb.cursor() #make the connection to execute SQL queries
    sql_command = "SELECT * FROM task" #sql command to select all the columns from the table task
    mycursor.execute(sql_command) #execute the sql command
    myresult = mycursor.fetchall() #returns all the rows from the table task
    
    try: #if there are already tasks
        mycursor = mydb.cursor() #make the connection to execute SQL queries
        sql_command = "SELECT MAX(task_no) as 'maximum' FROM task" #sql command to select the maximum value of task number in the task table
        mycursor.execute(sql_command) #execute the sql command
        myresult = mycursor.fetchone() #returns the value of the maximum task number
        myresult = myresult[0] 
        myresult = myresult+1 #the value of the task number
        return myresult #return the value of the task number
    except: #if there are no tasks
        return 1 #return 1

def EnterTaskDueDate(): #function that adds due date
    while(True): #condition
        try:
            duedate = input("\nEnter task due date (Use the format: YYYY/MM/DD): ") #input from the user
            duedate = datetime.datetime.strptime(duedate, "%Y-%m-%d") #change the format
            return datetime.datetime.strftime(duedate, "%Y-%m-%d") #return the formatted input
        except ValueError:
            print("\nInvalid date/time entry! Please use the following format: YYYY/MM/DD.")  #prompt

def EnterDateCreated(): #function that adds date created
    datecreated = datetime.datetime.now() #present date
    return datetime.datetime.strftime(datecreated, "%Y-%m-%d") #returning the present date in a new format

def PrintTasks(): #function that print tasks
    mycursor = mydb.cursor() #make the connection to execute SQL queries
    sql_command = "SELECT * FROM task" #sql command to select all the columns from the table task
    mycursor.execute(sql_command) #execute the sql command
    myresult = mycursor.fetchall() #returns all the rows from the table task
    if myresult == None: #if there is no task
        print("\nThere are no available tasks at the moment. Please add one first.") #prompt
        return 
    else: #if there are tasks
        tasklist = [] #array
        print("\nThe following are the available tasks created: ") #print
        for row in myresult: #for loop
            print("["+str(row[0])+"]", row[2]) #printing the task
            tasklist.append(row[0]) #to record in a list
        
        while(True): #while loop
            try:
                tasknumber = int(input("\nEnter the number of the task you would like to update/delete: ")) #input from the user
                if tasknumber in tasklist: #if the input is in the list
                    return tasknumber #returns the task number
                else: #if the input is not in the list
                    print("\nThe task number you entered does not exist!") #prompt
            except ValueError: #if the input is not valid
                print("\nInvalid task number entry. Please try again.") #prompt

def PrintCategories(): #function that prints categories
    mycursor = mydb.cursor() #make the connection to execute SQL queries
    sql_command = "SELECT * FROM category" #sql command
    mycursor.execute(sql_command) #execute sql command
    myresult = mycursor.fetchall() #returns the rows from category table
    if myresult == None: #if there is no category
        print("\nThere are no available categories at the moment. Please add one first.") #prompt
        AddCategory() #call the function to add category
    else:
        categorylist = [] #array
        print("\nThe following are the available categories created: ") #print
        for row in myresult: #loop
            print('['+str(row[0])+']', row[1]) #printing the categories
            categorylist.append(row[0]) #to record in a list
        
        while(True): #loop
            try:
                categorynumber = int(input("\nEnter the number of the category you would like to update/delete: ")) #input from the user
                if categorynumber in categorylist: #if the input is in the list
                    return categorynumber #return
                else: #if the input is not in the list
                    print("\nThe category number you entered does not exist!") #prompt
            except ValueError: 
                print("\nInvalid category number entry. Please try again.") #prompt

def AddCategory(): #function that adds category
    print("\n----- Adding a category -----") #print
    categoryno = EnterCategoryNo() #call the function to add category number
    categoryname = EnterCategoryName() #call the function to add category name
    datecreated = EnterDateCreated() #call the function to add date today

    sql_command = "INSERT INTO category (category_no, category_name, date_created) VALUES (%s, %s, %s)" #sql command
    query_vals = (categoryno, categoryname, datecreated) #values
    mycursor.execute(sql_command, query_vals) #execute the sql command
    mydb.commit() #confirm the changes
    print("----------------------------------------------")
    print("Category has been added successfully.") #prompt  
    print("----------------------------------------------") 

def AddTask(): #function that adds a task
    print("\n----- Adding/Creating a task -----") #print
    taskno = EnterTaskNo() #call the function that adds a task number
    categoryno = EnterTaskCategory() #call the function that adds task to a category
    taskname = EnterTaskName() #call the function to add task name
    duedate = EnterTaskDueDate() #call the function that adds due date
    datecreated = EnterDateCreated() #call the function to add date today
    description = EnterTaskDesc() #call the function to add description to the task
    status = EnterTaskStatus() #call the function that adds status to the task

    sql_command = "INSERT INTO task (task_no, category_no, task_name, due_date, date_created, description, status) VALUES (%s, %s, %s, %s, %s, %s, %s)" #sql command
    query_vals = (taskno, categoryno, taskname, duedate, datecreated, description, status) #values
    mycursor.execute(sql_command, query_vals) #execute the sql command
    mydb.commit() #confirm the changes
    print("----------------------------------------------") 
    print("Task has been added successfully.") #prompt
    print("----------------------------------------------")

def EditCategory(): #function that edits a category
    print("\n----- Editing a category -----") #prompt
    categorynumber = PrintCategories() #call the function that prints all the category
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    sql_command = "SELECT * FROM category WHERE category_no = %s" #sql command
    query_vals = (categorynumber,) # categorynumber needs to be of type list, tuple, or dictionary
    mycursor.execute(sql_command, query_vals) #execute the sql command
    myresult = mycursor.fetchone() #returns all the rows from the category table given that condition
    print("\nThe following are the details of the category you selected: ") #print
    print("\n--------------------------\n") #print
    print("Category no.: ", myresult[0]) #print
    print("Category name: ", myresult[1]) #print
    print("Date created: ", myresult[2]) #print
    print("\n--------------------------") #print

    print("\nBelow are the editable fields") #print
    print("[1] Category name") #print

    while(True): #loop
        try:
            categoryfield = int(input("\nSelect which field you would like to edit: ")) #input
            if categoryfield in range(1,2): #condition to check for the input
                if categoryfield == 1: # Edits the category name field
                    print("\nYou have selected to edit the category name field.") #print
                    print("\nThe current category name of the selected category is: ", myresult[1]) #print
                    print("\nPlease enter the new category name you wish to name the category as. ") #print
                    categoryname = EnterCategoryName() #call the function that adds category name
                    sql_command = "UPDATE category SET category_name = %s WHERE category_no = %s" #sql command
                    query_vals = (categoryname, categorynumber) #values
                    mycursor.execute(sql_command, query_vals) #execute the sql command
                    mydb.commit() #confirm the changes
                    print("\nThe category name field has been successfully updated.") #prompt
                    return         
            else:
                print("\nThe field you entered does not exist. Please try again.") #prompt
        except ValueError:
            print("\nInvalid field entry. Please try again.") #prompt

def EditTask(): #function that edits a task
    print("\n----- Editing a task -----") #print
    tasknumber = PrintTasks() #call the function that print the tasks
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    sql_command = "SELECT * FROM task WHERE task_no = %s" #sql command
    query_vals = (tasknumber,) #tasknumber needs to be of type list, tuple, or dictionary
    mycursor.execute(sql_command, query_vals) #execute the sql command
    myresult = mycursor.fetchone() #returns all the rows form task table given the condition    print("\nThe following are the details of the task you selected: ") #print
    print("\n--------------------------\n") #print
    print("Task no.: ", myresult[0]) #print
    print("Category no.: ", myresult[1]) #print
    print("Task name: ", myresult[2]) #print
    print("Task due date: ", myresult[3]) #print
    print("Task date created: ", myresult[4]) #print 
    print("Task description: ", myresult[5]) #print
    print("Task status: ", myresult[6]) #print
    print("\n--------------------------") #print 
    
    print("\nBelow are the editable fields") #print
    print("[1] Task name") #print
    print("[2] Task due date") #print
    print("[3] Task description") #print
    print("[4] Task status") #print

    while(True): #loop
        taskfield = int(input("\nSelect which field you would like to edit: ")) #input from the user
        try:
            if taskfield in range(1,6): #condition if the input is in the list
                if taskfield == 1: # Edits the task name field
                    print("\nYou have selected to edit the task name field.") #print
                    print("\nThe current task name of the selected task is: ", myresult[2]) #print
                    print("\nPlease enter the new task name you wish to name the task as. ") #print
                    taskname = EnterTaskName() #call the function to adds task name
                    sql_command = "UPDATE task SET task_name = %s WHERE task_no = %s" #sql command to update
                    query_vals = (taskname, tasknumber) #values
                    mycursor.execute(sql_command, query_vals) #execute the sql command
                    mydb.commit() #confir the changes
                    print("\nThe task name field has been successfully updated.") #prompt
                    return
                elif taskfield == 2: #Edits the task due date
                    print("\nYou have selected to edit the task due date field.") #print
                    print("\nThe current task due date of the selected task is: ", myresult[3]) #print
                    print("\nPlease enter the new task due date you wish to input. ") #print
                    duedate = EnterTaskDueDate() #call the functions that adds due date
                    sql_command = "UPDATE task SET due_date = %s WHERE task_no = '%s'" #sql command to update
                    query_vals = (duedate, tasknumber) #values
                    mycursor.execute(sql_command, query_vals) #execute the sql command
                    mydb.commit() #confirm the changes                     
                    print("\nThe task due date field has been successfully updated.") #prompt
                    return
                elif taskfield == 3: # Edits the task description field
                    print("\nYou have selected to edit the task description field.") #print
                    print("\nThe current task description of the selected task is: ", myresult[5]) #print
                    print("\nPlease enter the new task description you wish to input. ") #print
                    description = EnterTaskDesc() #call the function that adds task description
                    sql_command = "UPDATE task SET description = %s WHERE task_no = '%s'" #sql command to update
                    query_vals = (description, tasknumber) #values
                    mycursor.execute(sql_command, query_vals) #execute the sql command 
                    mydb.commit() #confirm the changes                    
                    print("\nThe task due date field has been successfully updated.") #prompt
                    return  
                else: # Edits the task status field
                    print("\nYou have selected to edit the task status field.") #print
                    print("\nThe current task status of the selected task is: ", myresult[6]) #print
                    print("\nPlease enter the new task status you wish to input. ") #print
                    status = EnterTaskStatus() #call the function that adds status to a task
                    sql_command = "UPDATE task SET status = %s WHERE task_no = '%s'" #sql command to update
                    query_vals = (status, tasknumber) #values
                    mycursor.execute(sql_command, query_vals) #execute the sql command
                    mydb.commit() #confirm the changes                      
                    print("\nThe task due date field has been successfully updated.") #prompt
                    return                                       
            else:
                print("\nThe field you entered does not exist. Please try again.") #prompt
        except ValueError:
            print("\nInvalid field entry. Please try again.") #prompt

def MarkTaskAsDone(): #function that changes the status to done
    print("\n----- Marking task as done -----") #print
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    sql_command = "SELECT COUNT(*) FROM task WHERE status LIKE 'Not yet started' OR status LIKE 'Ongoing'" #sql command
    mycursor.execute(sql_command) #execute sql command 
    count = mycursor.fetchone()  #returns all the rows from task table
    counter = int(0 if count[0] is None else count[0]) #counter
    if counter != 0: #condition
        print("\nThe following is a list of tasks that are either not yet started or ongoing") #print
        sql_command = "SELECT * FROM task WHERE status LIKE 'Not yet started' OR status LIKE 'Ongoing'" #sql command
        mycursor.execute(sql_command) #execute sql command 
        myresult = mycursor.fetchall() #returns all the rows from task table
        tasklist = [] #array
        for row in myresult: #loop
            print('['+str(row[0])+']', str(row[2])) #print
            tasklist.append(row[0]) #to record in a list
        
        tasknumber = int(input("\nEnter the number of the task you would like to mark as done: ")) #input from the user
        if tasknumber in tasklist: #if the input is in the list
            mycursor = mydb.cursor() #make the connection to excute SQL queries
            sql_command = "UPDATE task SET status = 'Done' WHERE task_no = %s" #sql command
            query_vals = (tasknumber,) #values
            mycursor.execute(sql_command, query_vals) #execute sql command 
            mydb.commit() #confirm the changes
            print("\nThe selected task has been successfully marked as done.") #prompt
            return
        else:
            print("\nThe task number you entered does not exist. Please try again.") #print
            MarkTaskAsDone() #call the function mark as done  
    else: 
        print("\nThere is no available task to be marked as done. Please try again.") #prompt
        return

def DeleteTask(): #function that deletes a task
    print("\n----- Deleting a task -----") #print
    tasknumber = PrintTasks() #call the function that print all the tasks
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    sql_command = "DELETE FROM task WHERE task_no = %s" #sql command
    query_vals = (tasknumber,) #values
    mycursor.execute(sql_command, query_vals) #execute sql command
    mydb.commit() #confirm the changes
    print("\nThe selected task has been successfully deleted.") #prompt

def DeleteCategory(): #function that deletes a category
    print("\n----- Deleting a category -----") #print
    categorynumber = PrintCategories() #call the function that print all the categories
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    sql_command = "SELECT * FROM task WHERE category_no = %s" #sql command
    query_vals = (categorynumber,) #values
    mycursor.execute(sql_command, query_vals) #execute sql command
    myresult = mycursor.fetchone() #returns all the rows from task table given the condition
    if myresult == None: #if there are no tasks
        mycursor = mydb.cursor() #make the connection to excute SQL queries
        sql_command = "DELETE FROM category WHERE category_no = %s" #sql command
        query_vals = (categorynumber,) #values
        mycursor.execute(sql_command, query_vals) #execute sql command
        mydb.commit() #confirm the changes
        print("\nThe selected category has been successfully deleted.") #prompt
    else:
        print("\nThe selected category currently contains tasks. Please delete all tasks under the category first before deleting.") #prompt
        return

def ViewAllCategories(): #function that view all the categories
    print("\n----- Viewing all categories -----") #print
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    mycursor.execute("SELECT * FROM category") #execute sql command
    result=mycursor.fetchall() #returns all the rows from table category
    mycursor.execute("SELECT COUNT(category_no) FROM category") #execute sql command
    count=mycursor.fetchone() #return the count of all categories
    counter = str(count[0]) #counter
    
    if counter != "0": #if the counter is not 0
        for row in result: #for loop
            print("\n-------------------------------") #print
            print("Category number: ",(row[0]))  #print
            print("Category name: ",(row[1]))  #print
            print("Category date created: ", (row[2])) #print
            print("-------------------------------") #print
    else: #if there are no categories
        print("\n--------------------------------------------------------------------------") 
        print("\nThere are no available categories at the moment. Please add one first.") #prompt
        print("\n--------------------------------------------------------------------------")

def ViewAllTasks(): #function that view all the tasks
    print("\n----- Viewing all tasks -----") #print
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    mycursor.execute("SELECT * FROM task") #sql execute
    myresult = mycursor.fetchall() #returns all the rows from table task
    mycursor.execute("SELECT COUNT(task_no) FROM task") #sql execute
    count=mycursor.fetchone() #return the count of all tasks
    counter = str(count[0]) #counter
    
    if counter !="0": #if the counter is not 0
        for row in myresult: #for loop
            print("\n-------------------------------") #print 
            print("Task number: ", row[0]) #print
            print("Category number: ", row[1]) #print
            print("Task name: ", row[2]) #print
            print("Task due date: ", row[3]) #print
            print("Task date created: ", row[4]) #print
            print("Task description: ", row[5]) #print
            print("Task status: ", row[6]) #print
            print("-------------------------------")
    else: #if there are no tasks
        print("\n--------------------------------------------------------------------------")
        print("\nThere are no available task at the moment. Please add one first.") #prompt
        print("\n--------------------------------------------------------------------------")

def ViewTaskToday(): #function to view all task
    print("\n----- Viewing Tasks Today -----") #print
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    datecreated = datetime.datetime.now() #declaring a new variable with day today
    mycursor.execute("SELECT * FROM task WHERE DAY(due_date) = DAY(NOW()) ") #sql command
    myresult = mycursor.fetchall() #return the rows from task table
    mycursor.execute("SELECT COUNT(task_no) FROM task WHERE DAY(due_date) = DAY(NOW())") #sql command
    count=mycursor.fetchone() #return the count of the number of tasks due today
    counter = str(count[0]) #counter
    
    if counter =="0": #there is no due
        print("\n--------------------------------------------------------------------------")
        print("\nThere are no available tasks that are due today. You may rest.")
        print("\n--------------------------------------------------------------------------")
    else: #if there is due
        for row in myresult: #loop
            print("\n-------------------------------")
            print("Task number: ", row[0]) #print
            print("Category number: ", row[1]) #print            
            print("Task name: ", row[2]) #print
            print("Task due date: ", row[3]) #print
            print("Task date created: ", row[4]) #print
            print("Task description: ", row[5]) #print
            print("Task status: ", row[6]) #print
            print("-------------------------------")

def ViewMonthlyTask():#function
    print("\n----- Viewing Tasks For This Month -----")
    mycursor = mydb.cursor() #make the connection to excute SQL queries
    datecreated = datetime.datetime.now() #declaring a new variable with day today
    mycursor.execute("SELECT * FROM task WHERE MONTH(due_date) = MONTH(NOW()) ORDER BY due_date ASC") #sql command
    myresult = mycursor.fetchall() #return the rows from task table
    mycursor.execute("SELECT COUNT(task_no) FROM task WHERE MONTH(due_date) = MONTH(NOW())") #sql command
    count=mycursor.fetchone() #return the count of the number of tasks due this month
    counter = str(count[0]) #counter
    
    if counter =="0": #there is no due
        print("\n--------------------------------------------------------------------------")
        print("\nThere are no available tasks that are due this month. You may rest.") #prompt
        print("\n--------------------------------------------------------------------------")
    else: #there is due
        for row in myresult: #there is due
            print("\n-------------------------------")
            print("Task number: ", row[0]) #print
            print("Category number: ", row[1]) #print            
            print("Task name: ", row[2]) #print
            print("Task due date: ", row[3]) #print
            print("Task date created: ", row[4]) #print
            print("Task description: ", row[5]) #print
            print("Task status: ", row[6]) #print
            print("-------------------------------")

database() #call the function database

print("\nWelcome to the Task Recording App!") #print

while(True): #loop
    PrintMenu() #call the function to print the menu
    user_choice = str(input("Enter a number: ")) #input from the user
    if user_choice == "1": #if the input is 1
        AddCategory() #call the function to add category
    elif user_choice == "2": #if the input is 2
        EditCategory()  #call the function to edit category
    elif user_choice == "3": #if the input is 3
        DeleteCategory()  #call the function to delete category
    elif user_choice == "4": #if the input is 4
        ViewAllCategories() #call the function to view all the categories
    elif user_choice == "5": #if the input is 5
        AddTask()  #call the function to add task
    elif user_choice == "6": #if the input is 6
        EditTask()  #call the function to add task
    elif user_choice == "7": #if the input is 7
        DeleteTask() #call the function to delete task
    elif user_choice == "8": #if the input is 8
        ViewAllTasks() #call the function to view task
    elif user_choice == "9": #if the input is 9
        MarkTaskAsDone() #call the function to mark a selected task's status to done
    elif user_choice == "10":  #if the input is 10
        ViewTaskToday() #call the function to view the tasks due today
    elif user_choice == "11": #if the input is 11
        ViewMonthlyTask() #call the function to view the tasks due this month
    elif user_choice == 0: #if the input is 0
        break #exit
    else:
        print("\n")
        print("------------------------------")
        print("\tInvalid input.") #prompt
        print("------------------------------")
print("\nThank you for using the program!") #prompt
print(" ")