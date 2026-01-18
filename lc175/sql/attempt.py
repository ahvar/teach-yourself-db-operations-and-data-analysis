import sqlite3

conn = sqlite3.connect("two_tables.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE Person(
        personId INTEGER PRIMARY KEY,
        lastName VARCHAR,
        firstName VARCHAR
)"""
)


cursor.execute(
    """
    CREATE TABLE Address(
        addressId INTEGER PRIMARY KEY,
        personId INTEGER,
        city VARCHAR,
        state VARCHAR
    )
    """
)
cursor.executemany(
    """INSERT INTO Person (personId, lastName, firstName) VALUES (?,?,?)""",
    [(1, "Wang", "Allen"), (2, "Alice", "Bob")],
)

cursor.executemany(
    """INSERT INTO Address (addressId, personId, city, state) VALUES (?,?,?,?)""",
    [(1, 2, "New York City", "New York"), (2, 3, "Leetcode", "California")],
)

cursor.execute(
    """
    SELECT Person.firstName, Person.lastName, Address.city, Address.state
    FROM Person LEFT JOIN Address on Person.personId = Address.personId;
"""
)
