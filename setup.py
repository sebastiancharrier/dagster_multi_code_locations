import glob

from setuptools import find_packages, setup

setup(
    name="dagster_multi_code_locations",
    packages=find_packages(),
    # package data paths are relative to the package key
    package_data={
        "assets_dbt_python": ["../" + path for path in glob.glob("dbt_project/**", recursive=True)]
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "pandas",
        "pandas_gbq",
        "numpy",
        "dagster-duckdb",
        "dagster-duckdb-pandas",
        "dbt-bigquery==1.4",
        "gcsfs",
        "psycopg2-binary",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)