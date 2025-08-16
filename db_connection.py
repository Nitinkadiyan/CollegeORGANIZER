import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost\\SQLEXPRESS;;"  # <--- change this to your server name
            "Database=CollegeMaker;"
            "Trusted_Connection=yes;"
        )
        return connection
    except Exception as e:
        print("Error connecting to database:", e)
        return None