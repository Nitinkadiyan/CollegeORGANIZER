from TodoApp import tasks,show_menu,run_todo
from Deadlines import dates_menu,run_deadline
from notes_adder import notes
from Student_dashboard import dashboard_menu,run_dash

def display_menu():
    print("==================")
    
    print("\n StudySphere (Study Organizer Project")

    print("\n==================")

    print("1. Task manager")
    print("2. Deadlines")
    print("3. Students DashBoard")
    print("4. Notes Adder")
    print("5. Exit ")
    print("\n==================")
    
while True:   
    display_menu() 
    choice = input("Enter your choice: ")

    if choice =="1":
        run_todo()
    elif choice=="2":
        run_deadline()
    elif choice=="3":
        run_dash()
    elif choice=="4":
        notes()
    elif choice =="5":
        print("Exiting app")
        break
    else:
        print("Invalid choice, Try again")


   