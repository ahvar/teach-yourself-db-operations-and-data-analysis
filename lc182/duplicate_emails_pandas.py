import pandas as pd

person = [
    {
        "id": 1,
        "email": "a@b.com"
    },
    {
        "id":2,
        "email": "b@c.com"
    },
    {
        "id": 3,
        "email": "a@b.com"
    },
    {
        "id": 4,
        "email": "r@t.com"
    }
]

person_df = pd.DataFrame(person)
duplicates = person_df.groupby('email').filter(lambda x: len(x) > 1)
result = duplicates[['email']].drop_duplicates().rename(columns={'email': 'Email'})
