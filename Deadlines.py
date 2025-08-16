import pyodbc
from db_connection import get_connection
Dates=[]

def add_deadline():
    title= input("enter title:")
    Description=input("enter description")
    date=input("Enter date (DD-MM-YYYY): ")
    # Dates.append({"title":title,"description":Description,"Date":date})
    # print("Deadline added successfully")
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(
        "Insert INTO deadlines(title,description,date)VALUES(?,?,?)",(title,Description,date))
    conn.commit()
    conn.close()

def view_dates():
    # if not Dates:
    #     print("no such deadline found")
    #     return 
    # for d in Dates:
    #     print("----------------")
    #     print(f"title: {d['title']}")
    #     print(f"Description: {d['description']}")
    #     print(f"date: {d['Date']}")
    #     print("----------------")
     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "SELECT title,description,date FROM deadlines" )
     rows=cursor.fetchall()
     for row in rows:
         print(row)
     conn.commit()
     conn.close()

def search_dates():
     title = input("enter the title of deadline: ")
    #  found = False
    #  for i in Dates:
    #      if i["title"].lower()==title:
    #          print("--------------")
    #          print(f"title: {i['title']}")
    #          print(f"Description: {i['description']}")
    #          print(f"date: {i['Date']}")
    #          print("--------------")
    #          found=True
    #          break
    #      print("No such data find")
     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "SELECT title,description,date FROM deadlines WHERE title=? ",(title,))
     row=cursor.fetchone()
     if row:
         print(f"Title : {row[0]}\nDescription : {row[1]}\n Date : {row[2]}")
     else:
         print("No such data found")
     conn.commit()
     conn.close()

def delete_date():
    # if not Dates:
    #     print("No deadline here...")
    #     return 
    title= input("Enter the title you want to delete")
    conn= get_connection()
    cursor=conn.cursor()
    cursor.execute( "DELETE FROM deadlines WHERE title=?",(title,)) 
    conn.commit()
    conn.close() 
    # for i in Dates:
    #     if i["title"].lower() == title.lower():
    #         Dates.remove(i)
    #         print("Data removed Successfully")
    #         return
    #     print("No matching data found")
    








def dates_menu():
    print("----Deadlines----")
    print("1. Add deadlines/Important dates")
    print("2. View all Deadlines/ Important dates")
    print("3. Search ")
    print("4. Delete a deadline/important date")
    print("5. exit")
def run_deadline():
  while True:
    dates_menu()
    choice= input("Enter your choice ")
    if choice =="1":
        add_deadline()
    elif choice =="2":
        view_dates()
    elif choice =="3":
          search_dates()
    elif choice=="4":
         delete_date()
    elif choice =="5":
        print("Exiting this feature")
        break
    else: 
        print("Invalid Choice ,Try Again")



if __name__=="__main__":
  run_deadline()