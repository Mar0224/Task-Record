# Task-Record

The task record app is a simplified version of a task listing app, where a user can list tasks, provide grouping and deadline through a command line interface in Python that is connected to a MariaDB database. It has the following features: Add a category, Edit category, Delete category, View category, Add a task to a category, Edit task, Delete task, View all tasks, View all tasks due today, View all tasks due this month, and Mark task as done. 

In order to use the task record system, first, unzip the group2_t2l.zip file containing the taskrecord.py source codes, a taskrecord.sql dump file with dummy data, and this READme file with instructions on how to run the program.

Before running the files, make sure that you have both Python and MariaDB installed. If not, you can download the latest version of Python here https://www.python.org/downloads/ and the latest version of MariaDB here https://mariadb.org/download/?p=mariadb&r=10.6.8&os=Linux&cpu=x86_64&pkg=tar_gz&i=systemd&m=gigenet&t=mariadb.Just look for the compatible versions for your computer.

You can check if you have Python installed by going to a terminal, such as the command prompt and if you type ‘python’ and press enter, it should show the current version of Python installed. 

You can check if you have MariaDB installed by going to a terminal, such as the command prompt and if you type ‘mysql -u root -p’ and press enter, it should ask you for a password and when you input your password, you can use MariaDB.

After making sure that you have both Python and MariaDB installed, open the taskrecord.py on a code editor and go to line 8 to change the password ‘password’ to your password on MariaDB and save the file. Also, note that the current source code runs dummy data. So, if you wish to create a new database, delete line 9: database = "database name". 

Go to a terminal, such as command prompt, and then go to the directory of the Python file and SQL file. It must be noted that they should be in the same directory. Type "python taskrecord.py" and press enter to run. You can now try its different features. 

If you will be using the taskrecordDUMP.sql file and you encounter an error upon running "python taskrecord.py", try opening the SQL file in any terminal with MariaDB then source the SQL file. 
