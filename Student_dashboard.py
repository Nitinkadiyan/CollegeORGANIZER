from TodoApp import tasks as Tasks
from Deadlines import Dates as Dates
import pyodbc
from db_connection import get_connection
def student_dashboard():
    # print("-------Tasks Overview--------")
    # if Tasks:
    #     Total_tasks=len(Tasks)
    #     completed_tasks= sum(1 for task in Tasks.values() if task["status"].lower() == "done")
    #     pending_tasks=Total_tasks - completed_tasks
    #     print(f"Total tasks: {Total_tasks}")
    #     print(f"Completed tasks: {completed_tasks}")
    #     print(f"Pending tasks: {pending_tasks}")
    #     if pending_tasks >0:
    #         print("Pending tasks : ")
    #         for title,task in Tasks.items():
    #             if task["status"].lower()!="done":
    #                 print(f" --{title}")
    # else :
    #     print("No tasks added yet")import pyodbc
     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "SELECT COUNT(*) FROM Tasks" )
     total_tasks=cursor.fetchone()[0]
     cursor.execute( "SELECT COUNT(*) FROM Tasks WHERE status='done';" )
     completed_tasks=cursor.fetchone()[0]
     pending_tasks=total_tasks-completed_tasks
     print("----Tasks viewer ------")
     print(f"Total tasks : ",{total_tasks})
     print(f"Completed Tasks : ",{completed_tasks})
     print(f"Pending tasks : ",{pending_tasks})
     conn.commit()
     conn.close()


def Deadlines_check():
    #     print("----------------")
     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "SELECT title,description,date FROM deadlines" )
     rows=cursor.fetchall()
     for row in rows:
         print(row)
     conn.commit()
     conn.close()
     

def dashboard_menu():
    print("==================")
    print("----Students dashboard----")
    print("==================")
    print("1. Tasks Overview")
    print("2. Important Deadlines")
    print("3. Exit")
def run_dash():
  while True:
    dashboard_menu()
    choice = input("Enter your choice ")
    if choice =="1":
        student_dashboard()
    elif choice =="2":
        Deadlines_check()
    elif choice =="3":
        print("Exiting this feature ")
        break
    else:
        print("Invalid choice try again")



if __name__=="__main__":
 run_dash()
