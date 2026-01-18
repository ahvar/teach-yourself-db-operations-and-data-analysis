import pandas as pd

person_df = pd.DataFrame(
    [
        {"personId": 1, "lastName": "Wang", "firstName": "Allen"},
        {"personId": 2, "lastName": "Alice", "firstName": "Bob"},
    ]
)

address_df = pd.DataFrame(
    [
        {"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"},
        {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"},
    ]
)


output = person_df.merge(address_df, on="personId", how="left")
