import pandas as pd
"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name,
salary, and the ID of their manager.

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
"""

employees = [
    {
        'id': 1,
        'name': "Joe",
        'salary': 70000,
        'managerId': 3,
    },
    {
        'id': 2,
        'name': 'Henry',
        'salary': 80000,
        'managerId': 4,
    },
    {
        'id': 3,
        'name': 'Sam',
        'salary': 60000,
        'managerId': None,
    },
    {
        'id': 4,
        'name': 'Max',
        'salary': 90000,
        'managerId': None,
    }

]

employees = pd.DataFrame(employees)
result = employees.merge(
    employees,left_on='managerId',
    right_on='id',
    suffixes=('_emp', '_mgr')
)
result = result[result['salary_emp'] > result['salary_mgr']]
final_result = result[['name_emp']].rename(columns={'name_emp': 'Employee'})