import pandas as pd


employee = pd.DataFrame(
    [
        {"id": 1, "name": "Joe", "salary": 70000, "managerId": 3},
        {"id": 2, "name": "Henry", "salary": 80000, "mangerId": 4},
        {"id": 3, "name": "Sam", "salary": 60000, "managerId": None},
        {"id": 4, "name": "Max", "salary": 90000, "managerId": None},
    ]
)

merged = employee.merge(
    employee, right_on="id", left_on="managerId", suffixes=("_manager", "")
)
result = merged[merged["salary"] > merged["salary_manager"]][["name"]]
