
import sqlite3
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute("""

    CREATE TABLE Employee(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        salary INTEGER,
        managerId INTEGER
    )
""")

cursor.executemany("""INSERT INTO Employee VALUES (?,?,?,?)""",
    [
        (1,'joe',70000, 3),
        (2, 'Henry', 80000, 4),
        (3, 'Sam', 60000, None),
        (4, 'Max', 90000, None)
    ]
)

cursor.execute("""
    SELECT e.name
    FROM Employee e
    JOIN Employee m ON e.managerId = m.id
    WHERE e.salary > m.salary;
""")





)
