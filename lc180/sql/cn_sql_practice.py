import sqlite3

conn = sqlite3.connect("logs.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE Logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        num INTEGER
    )
"""
)

cursor.executemany(
    """INSERT INTO Logs(id, num) VALUES (?,?)""",
    [(1, 1), (2, 1), (3, 1), (4, 2), (5, 1), (6, 2), (7, 2)],
)

cursor.execute(
    """
              
    SELECT DISTINCT l1.num as ConsecutiveNums
    FROM Logs l1
    JOIN Logs l2 ON l1.id = l2.id - 1
    JOIN Logs l3 on l2.id = l3.id - 1
    WHERE l1.num = l2.num AND l2.num = l3.num;
              
"""
)

conn.commit()
conn.close()
