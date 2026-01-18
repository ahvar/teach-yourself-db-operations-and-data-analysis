import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE Person(
        id INTEGER PRIMARY KEY,
        email VARCHAR
    )
"""
)

cursor.executemany(
    """INSERT INTO Person(id, email) VALUES (?,?)""",
    [(1, "a@b.com"), (2, "c@d.com"), (3, "a@b.com")],
)


cursor.execute(
    """
    SELECT email
    FROM Person
    GROUP BY email
    HAVING COUNT(email) > 1
"""
)
