from dagster import load_assets_from_package_module
from . import raw

raw_assets = load_assets_from_package_module(
    package_module = raw,
    group_name = 'streaming',
    key_prefix = ["raw"]
)