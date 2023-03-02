import json
import os
from dagster import file_relative_path
from .db_io_managers import bigquery_pandas_io_manager
from dagster_dbt import dbt_cli_resource

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt_project")
DBT_PROFILES_DIR = DBT_PROJECT_DIR  + "/config"

#=====================================================================================
# Set google application credentials with json service account
# json must be saved in environment variable GCP_CREDS_JSON
#=====================================================================================
AUTH_FILE = "./gcp_creds.json"
with open(AUTH_FILE, "w") as file:
    json.dump(json.loads(os.getenv("GCP_CREDS_JSON")), file)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = AUTH_FILE
#=====================================================================================


RESOURCES_DEV = {
    "db_io_manager": bigquery_pandas_io_manager.configured (
        {
            "project_id": "develop-291715",
            "dataset_id": "analytics"
        }
    ),
    "dbt": dbt_cli_resource.configured (
        {
            "project_dir": DBT_PROJECT_DIR, 
            "profiles_dir": DBT_PROFILES_DIR
        }
    )
}

RESOURCES_STAGING = {
    "db_io_manager": bigquery_pandas_io_manager.configured (
        {
            "project_id": "staging-291715",
            "dataset_id": "analytics"
        }
    ),
    "dbt": dbt_cli_resource.configured (
        {
            "project_dir": DBT_PROJECT_DIR, 
            "profiles_dir": DBT_PROFILES_DIR
        }
    )
}

RESOURCES_PROD = {
    "db_io_manager": bigquery_pandas_io_manager.configured (
        {
            "project_id": "prod-291715",
            "dataset_id": "analytics"
        }
    ),
    "dbt": dbt_cli_resource.configured (
        {
            "project_dir": DBT_PROJECT_DIR, 
            "profiles_dir": DBT_PROFILES_DIR
        }
    )
}


def get_env():
    if os.getenv("DAGSTER_CLOUD_IS_BRANCH_DEPLOYMENT", "") == "0":
        return "PROD"
    else: 
        if os.getenv("DAGSTER_CLOUD_DEPLOYMENT_NAME", "") == "staging":
            return "STAGING"
        return "DEV"


resources_by_deployment_name = {
    "DEV" : RESOURCES_DEV,
    "PROD": RESOURCES_PROD,
    "STAGING": RESOURCES_STAGING
}



RESOURCES = resources_by_deployment_name[get_env()]