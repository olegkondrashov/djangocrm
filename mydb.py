import psycopg

try:
    # Connect to the 'postgres' database
    conn = psycopg.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port=5432
    )
    conn.autocommit = True
    cur = conn.cursor()

    # Drop the database if it exists
    cur.execute("DROP DATABASE IF EXISTS my_db")

    # Create a new database
    cur.execute("CREATE DATABASE my_db")

    print("done")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection if they were established
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
