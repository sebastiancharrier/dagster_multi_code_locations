from dagster import file_relative_path
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_DIR = file_relative_path(__file__, "../../../dbt_project")
DBT_PROFILES_DIR = DBT_PROJECT_DIR  + "/config"

dbt_common_assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR,
    DBT_PROFILES_DIR,
    key_prefix=["common"],
    select= "tag:common" # To use --select tag in dbt
)