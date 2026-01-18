import pandas as pd

employees = pd.DataFrame(
    [
        {"id": 1, "name": "Joe", "salary": 70000, "managerId": 3},
        {"id": 2, "name": "Henry", "salary": 80000, "managerId": 4},
        {"id": 3, "name": "Sam", "salary": 60000, "managerId": None},
        {"id": 4, "name": "Max", "salary": 90000, "managerId": None},
    ]
)

merged = employees.merge(
    employees, left_on="managerId", right_on="id", suffixes=("", "_manager")
)

result = merged[merged["salary"] > merged["salary_manager"]][["name"]]
