from dagster import Definitions, load_assets_from_modules

from .assets import sales_assets, dbt_assets
from ..z_modules.resources import RESOURCES
from ..z_modules.assets import dbt_common_assets

ASSETS = [*dbt_common_assets, *sales_assets, *dbt_assets]

defs = Definitions(
    assets = ASSETS,
    resources = RESOURCES
)