import pandas as pd

logs = pd.DataFrame(
    [
        {"id": 1, "num": 1},
        {"id": 2, "num": 1},
        {"id": 3, "num": 1},
        {"id": 4, "num": 2},
        {"id": 5, "num": 1},
        {"id": 6, "num": 2},
        {"id": 7, "num": 2},
    ]
)

# identify the consecutive groups
logs["group"] = (logs["num"] != logs["num"].shift()).cumsum()

group_sizes = logs.groupby(["group", "num"]).size().reset_index(name="count")

at_least_three = group_sizes[group_sizes["count"] >= 3]

result = at_least_three["num"].unique()
