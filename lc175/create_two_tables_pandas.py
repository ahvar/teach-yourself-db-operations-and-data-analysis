import pandas as pd

person = [
    {
        "firstName": "john",
        "lastName": "smith",
        "personId": 1
    },
    {
        "firstName": "ahmed",
        "lastName": "troup",
        "personId": 2
    }
]

address = [
    {
        "personId": 2,
        "city": "Banklevel",
        "state": "OS"
    },
    {
         "personId": 5,
         "city": "dump",
         "state": "NR"
    }
]

person_df = pd.DataFrame(person)
print(person_df)
address_df = pd.DataFrame(address)
print(address_df)
print(person_df.merge(address_df, on='personId', how='left'))


