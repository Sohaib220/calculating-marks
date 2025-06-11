import sqlite3


def export_data_to_list(db_name, table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        # Execute a query to fetch all data from the table
        cur.execute(f"SELECT * FROM {table_name}")
        data = cur.fetchall()

        # Fetch the column names
        column_names = [description[0] for description in cur.description]

        # Combine column names and data
        data_list = [column_names] + data

        print("Data exported successfully.")
        return data_list
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        # Close the connection
        if conn:
            conn.close()


# Replace 'grades.db' with your database name and 'grades' with your table name
data_list = export_data_to_list('grades.db', 'grades')
for data in data_list:
    print(data)
