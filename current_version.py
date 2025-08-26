import great_expectations as gx

print(gx.__version__)

# Retrieve your Data Context
context = gx.get_context()
assert type(context).__name__ == "EphemeralDataContext"

# Define the Data Source name
data_source_name = "my_data_source"

# Add the Data Source to the Data Context
data_source = context.data_sources.add_pandas(name=data_source_name)
assert data_source.name == data_source_name
