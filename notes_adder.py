from db_connection import get_connection
notes={}
def add_note():
    subject= input("Enter subject: ").strip()
    topic = input("Enter topic: ").strip()
    subtopic = input("Enter subtopic(optional): ").strip()
    content=input("Enter your notes: ").strip()

    # if subject not in notes:
    #     notes[subject]={}
    # if topic not in notes[subject]:
    #     notes[subject][topic]={}
    # if subtopic:
    #     notes[subject][topic][subtopic]=content
    # else: 
    #     notes[subject][topic]["General"]=content

    # print("Note added successfully")

    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(
        "Insert INTO NotesMaker(Subject,Topic,Subtopic,Content)VALUES(?,?,?,?)",
        (subject,topic,subtopic if subtopic else "General",content)
    )
    conn.commit()
    conn.close()
    print("Notes added successfully")

def view_notes():
    # if not notes:
    #     print("No notes found\n")
    #     return 
    # for subject,topics in notes.items():
    #     print(f"subject: {subject}")
    #     for topic,subtopics in topics.items():
    #         print(f"topic: {topic}")
    #         for subtopic,content in subtopics.items():
    #             print(f" subtopic : {subtopic}")
    #             print(f"Content : {content}\n")
     conn= get_connection()
     cursor=conn.cursor()
     cursor.execute( "SELECT subject,topic,subtopic,content FROM NotesMaker" )
     rows=cursor.fetchall()
     for row in rows:
         print(row)
     conn.commit()
     conn.close()

def menu():
        print("Add Notes")
        print("1. Add notes")
        print("2. View notes")
        print("3. Exit")
def notes():         
 while True:
    menu()
    choice = input("Enter choice")

    if choice == "1":
        add_note()
    elif choice =="2":
        view_notes()
    elif choice == "3":
        print("exiting notes")
        break
    else:
        print("Invalid option , try again")

if __name__=="__main__":
    notes()