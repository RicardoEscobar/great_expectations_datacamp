import great_expectations as gx
import pandas as pd

# Create Data Context
context = gx.get_context()

# Add Data Source
data_source = context.data_sources.add_pandas(
  name="my_pandas_datasource"
)

# Add Data Asset
data_asset = data_source.add_dataframe_asset(
  name="my_dataframe_asset"
)

print(data_asset)

