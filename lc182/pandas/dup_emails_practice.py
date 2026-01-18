import pandas as pd


person = pd.DataFrame(
    [
        {
            "id": 1,
            "email": "a@b.com",
            "id": 2,
            "email": "c@d.com",
            "id": 3,
            "email": "a@b.com",
        }
    ]
)

grouped = person.groupby("email")
grouped["Email"] = grouped["email"] > 1


result = (
    person.groupby("email")
    .filter(lambda x: len(x) > 1)[["email"]]
    .drop_duplicates()
    .rename(columns={"email": "Email"})
)
