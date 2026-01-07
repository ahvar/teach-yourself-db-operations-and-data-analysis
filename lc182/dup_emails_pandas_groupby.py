import pandas as pd

person_df = pd.DataFrame(
    [
        {"id": 1, "email": "a@b.com"},
        {"id": 2, "email": "c@d.com"},
        {"id": 3, "email": "a@b.com"},
    ]
)
result = (
    person_df.groupby('email')
    .filter(lambda x: len(x) > 1)[['email']]
    .drop_duplicates()
    .rename(columns={'email': 'Email'})
)
print(result)


