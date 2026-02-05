import pandas as pd

person = pd.DataFrame(
    [
        {"personId": 1, "lastName": "Wang", "firstName": "Allen"},
        {"personId": 2, "lastName": "Alice", "firstName": "Bob"},
    ]
)

address = pd.DataFrame(
    [
        {"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"},
        {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"},
    ]
)

merged = person.merge(address, left_on="personId")
