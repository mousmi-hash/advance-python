import mysql.connector

# Establish connection
try:
    conn = mysql.connector.connect(
        user="root",
        password="Mousmi@0",
        host="localhost",
        port=3306
    )
    print("Connected successfully")

except mysql.connector.Error as err:
    print("Connection Error:", err)
    exit()

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS giet2")
cursor.execute("USE giet2")

# Drop table if exists (renamed to avoid confusion)
cursor.execute("DROP TABLE IF EXISTS employees")

# Create table
cursor.execute("""
CREATE TABLE employees (
    roll INT,
    name VARCHAR(50),
    address VARCHAR(50),
    desig VARCHAR(50),
    salary INT,
    gender CHAR(1)
)
""")

# Insert data
data = [
    (101, 'aman', 'delhi', 'doctor', 25000, 'M'),
    (102, 'priya', 'raipur', 'teacher', 18000, 'F'),
    (103, 'rohan', 'mumbai', 'engineer', 30000, 'M'),
    (104, 'sanya', 'raipur', 'doctor', 22000, 'F'),
    (105, 'vikram', 'delhi', 'engineer', 27000, 'M'),
    (106, 'neha', 'pune', 'teacher', 15000, 'F'),
    (107, 'anuj', 'raipur', 'doctor', 32000, 'M')
]

cursor.executemany(
    "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", data
)
conn.commit()

# Function to run queries
def run_query(query, description):
    print("\n" + description)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print("Query Error:", err)


# Queries

run_query("SELECT * FROM employees;", "1. All data")
run_query("SELECT name FROM employees;", "2. Only name column")
run_query("SELECT name, address FROM employees;", "3. Name and address")
run_query("SELECT roll, salary FROM employees;", "4. Roll and salary")
run_query("SELECT * FROM employees WHERE name='aman';", "5. Name = aman")
run_query("SELECT * FROM employees WHERE address='delhi';", "6. Address = delhi")
run_query("SELECT * FROM employees WHERE gender='M';", "7. Gender = M")
run_query("SELECT * FROM employees WHERE desig='doctor';", "8. Designation = doctor")
run_query("SELECT * FROM employees WHERE salary=15000;", "9. Salary = 15000")
run_query("SELECT * FROM employees WHERE salary > 20000;", "10. Salary > 20000")
run_query("SELECT * FROM employees WHERE salary < 30000;", "11. Salary < 30000")
run_query("SELECT * FROM employees WHERE gender='M' AND salary > 20000;", "12. Male AND salary > 20000")
run_query("SELECT * FROM employees WHERE gender='F' OR address='raipur';", "13. Female OR address = raipur")
run_query("SELECT * FROM employees WHERE name LIKE 'a%';", "14. Name starts with 'a'")
run_query("SELECT * FROM employees WHERE name LIKE '%h';", "15. Name ends with 'h'")
run_query("SELECT * FROM employees WHERE address LIKE '%pur%';", "16. Address contains 'pur'")
run_query("SELECT * FROM employees ORDER BY name ASC;", "17. Sorted by name ASC")
run_query("SELECT * FROM employees ORDER BY salary DESC;", "18. Sorted by salary DESC")
run_query("SELECT COUNT(*) FROM employees;", "19. Total employees")
run_query("SELECT COUNT(*) FROM employees WHERE gender='M';", "20. Count male employees")

# Close connection
cursor.close()
conn.close()