import pandas as pd
import numpy as np

np.random.seed(42)

rows = 20000

regions = ["North","South","East","West"]
categories = ["Electronics","Furniture","Office Supplies"]

data = {
    "order_id": range(1, rows+1),
    "order_date": pd.date_range(start="2023-01-01", periods=rows, freq="h"),
    "region": np.random.choice(regions, rows),
    "product_category": np.random.choice(categories, rows),
    "quantity": np.random.randint(1,5, rows),
    "sales": np.random.randint(20,500, rows),
    "profit": np.random.randint(5,150, rows)
}

df = pd.DataFrame(data)

df.to_csv("data/sales_data.csv", index=False)

print("Dataset created successfully!")
