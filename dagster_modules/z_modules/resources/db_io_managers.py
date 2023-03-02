import json

import pandas as pd
import datetime
import pandas_gbq
from google.oauth2 import service_account

from dagster import (
    Field,
    IOManager,
    InitResourceContext,
    InputContext,
    OutputContext,
    StringSource,
    io_manager,
)

class BigQueryDataframeIOManager(IOManager):
    def __init__(self, project_id: str, dataset_id: str) -> None:
        self._project_id = project_id
        self._dataset_id = dataset_id

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        # Skip handling if the output is None
        if obj is None:
            return

        table_name = context.asset_key.path[-1]

        pandas_gbq.to_gbq(
            obj,
            f"{self._dataset_id}.{table_name}",
            project_id=self._project_id,
            #if_exists="replace",
            if_exists="append", 
        )
        # Recording metadata from an I/O manager:
        # https://docs.dagster.io/concepts/io-management/io-managers#recording-metadata-from-an-io-manager
        context.add_output_metadata({"dataset_id": self._dataset_id, "table_name": table_name})

    def load_input(self, context: InputContext):
        table_name = context.asset_key.path[-1]

        df = pandas_gbq.read_gbq(
            f"SELECT * FROM `{self._dataset_id}.{table_name}`"
        )
        return df


@io_manager(
    config_schema={
        "project_id": StringSource,
        "dataset_id": Field(
            str, default_value="my_dataset", description="Dataset ID. Defaults to 'my_dataset'"
        ),
    }
)
def bigquery_pandas_io_manager(init_context: InitResourceContext) -> BigQueryDataframeIOManager:
    return BigQueryDataframeIOManager(
        project_id=init_context.resource_config["project_id"],
        dataset_id=init_context.resource_config["dataset_id"],
    )