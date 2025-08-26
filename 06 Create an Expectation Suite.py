import great_expectations as gx
import pandas as pd

# Data file location
data_csv_path = "data/2025-08-04--09-20-04__CARHARTT_FamilyFarmandHome_FamilyFarmandHome_20250802.txt"
column_names = [
    "HDR",
    "FamilyFarmandHome",
    "FAMILYFARMANDHOME",
    "08/02/2025",
    "P",
    "Unnamed: 5",
    "Unnamed: 6",
    "Unnamed: 77",
]

# Read data into pandas
dataframe = pd.read_csv(
    data_csv_path, sep="|", engine="python", header=0, skipfooter=1, names=column_names
)

# Create Data Context
context = gx.get_context()

# Add Data Source
data_source = context.data_sources.add_pandas(name="my_pandas_datasource")

# Add Data Asset
data_asset = data_source.add_dataframe_asset(name="my_dataframe_asset")

# Add batch definition
# Batch definition: A configuration of how a Data Asset should be divided for testing
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    name="my_batch_definition"
)

# Add batch using batch_definition
# Batch: A group of records that validations can be run on
batch = batch_definition.get_batch(batch_parameters={"dataframe": dataframe})

# Create Expectation Suite
suite = gx.ExpectationSuite(name="my_suite")

# Create Expectation
col_name_expectation = gx.expectations.ExpectColumnToExist(column="my_column_name")

# Add Expectation to Suite
suite.add_expectation(expectation=col_name_expectation)

# View Suite's Expectations
print(suite.expectations)

# Validate Suite
validation_results = batch.validate(expect=suite)

# Describe Validation Results
print(validation_results.describe())

# Validate Expectation
validation_results = batch.validate(expect=col_name_expectation)

# Describe Validation Results
print(validation_results.describe())

