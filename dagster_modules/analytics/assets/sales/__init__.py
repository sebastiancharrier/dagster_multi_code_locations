from dagster import asset
import numpy as np
import pandas as pd

@asset()
def asset_in_MODULE_ANALYTICS() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "user_id": range(1000),
            "company": np.random.choice(
                ["FoodCo", "ShopMart", "SportTime", "FamilyLtd"], size=1000
            ),
            "is_test_user": np.random.choice([True, False], p=[0.002, 0.998], size=1000),
        }
    )