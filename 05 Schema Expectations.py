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
print(dataframe.head())
print(dataframe.columns)

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

# Create Expectations
# Create an Expectation that the dataset contains a column named "HDR"
col_name_expectation = gx.expectations.ExpectColumnToExist(
    column="HDR"
)

# Validate the Expectation
validation_results = batch.validate(expect=col_name_expectation)

# Print out success status of Validation Results
print(validation_results.success)

# Establish a Column Range Expectation
# In this exercise, you'll be writing an Expectation regarding the column count of the dataset. Suppose the number of columns can change, but it should always stay in an interval around 16.

# The dataset has already been loaded into a Batch, assigned to the variable batch. Great Expectations and pandas are available as gx and pd, respectively.
# Create the Expectation
col_count_expectation = gx.expectations.ExpectTableColumnCountToBeBetween(
  min_value=14, max_value=18
)

# Validate the Expectation
validation_results = batch.validate(
  expect=col_count_expectation
)

# Print out the success status
print(validation_results.success)

# Print out the actual column count
print(validation_results.result["observed_value"])
