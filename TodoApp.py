import pyodbc
from db_connection import get_connection
tasks={}

def add_task():
     taskName= input("enter the name of task: ")
     tasks[taskName]={"status" :"Not done"}
     print(f"Task '{taskName}' added successfully")

     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "Insert INTO Tasks(title,status)VALUES(?,?)",(taskName,"Not done") )
     conn.commit()
     conn.close()
     print("Task added succesfully")
     

def view_task():
     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "SELECT title,status FROM Tasks" )
     rows=cursor.fetchall()
     for row in rows:
         print(row)
     conn.commit()
     conn.close()
    #  if not tasks:
    #     print("No Task found")
    #  else:
    #     print("\n Your Tasks : ")
    #     for i,t in enumerate(tasks,start=1):
    #         print(f"{i} . {t}-{tasks[t]['status']} ")

def delete_task():
    # if not tasks:
    #         print("\n No tasks to delete")
    #         return
    taskName=input("\n Enter the  task You want to delete")
    # if taskName in tasks:
    #       del tasks[taskName]
    #       print("Task deleted successfully")
    # else:
    #       print("Task not found")
    conn= get_connection()
    cursor=conn.cursor()
    cursor.execute( "DELETE FROM Tasks WHERE title=?",(taskName,)) 
    conn.commit()
    conn.close() 
    print("Task deleted successfully")


def update_status(taskName,new_status):
    # if taskName in tasks:
    #     tasks[taskName]['status']=new_status
    #     print("Changes made successfully")
    conn= get_connection()
    cursor=conn.cursor()
    cursor.execute( "UPDATE Tasks SET status=? WHERE title=?",(new_status,taskName) )
    conn.commit()
    conn.close()
    print("Updates made successfully")


def show_menu():
    print("\n --- To Do App ---")
    print("1. Add task")
    print("2. View tasks")
    print("3.  Mark Task as completed")
    print("4. Delete task")
    print("5. exit")
def run_todo():
    while True:
        show_menu()
        choice = input("enter your choice")

        if choice =="1":
            add_task()
        elif choice =="2":
            view_task()
        elif choice =="3": 
             taskName=input("\n Enter the  task You want to mark as completed")
             new_status=input("Enter updates about the task")
             update_status(taskName,new_status)
        elif choice =="4":
           delete_task()
        elif choice =="5":
            print("Exiting app")
            break
        else:
            print("Invalid choice, try again")


if __name__=="__main__":
 run_todo()

