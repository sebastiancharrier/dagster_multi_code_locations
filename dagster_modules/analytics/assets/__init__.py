from dagster import load_assets_from_package_module, file_relative_path
from dagster_dbt import load_assets_from_dbt_project
from . import sales

sales_assets = load_assets_from_package_module(
    package_module = sales,
    group_name = 'analytics',
    key_prefix = ["raw"]
)

DBT_PROJECT_DIR = file_relative_path(__file__, "../../../dbt_project")
DBT_PROFILES_DIR = DBT_PROJECT_DIR  + "/config"

dbt_assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR,
    DBT_PROFILES_DIR,
    key_prefix=["analytics"],
    select= "tag:analytics" # To use --select tag in dbt
)