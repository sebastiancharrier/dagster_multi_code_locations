from dagster import Definitions, load_assets_from_modules

from .assets import raw_assets
from ..z_modules.resources import RESOURCES

ASSETS = [*raw_assets]

defs = Definitions(
    assets = ASSETS,
    resources = RESOURCES
)