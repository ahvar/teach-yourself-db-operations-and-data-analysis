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
address_df = pd.DataFrame(address)
person_and_address = person_df.merge(address_df, how='left', on='personId')
print(person_and_address)
