import psycopg2

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="yourpassword"
    )
    cursor = conn.cursor()

    # Example: Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    ''')
    conn.commit()
    print("Table created successfully!")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
