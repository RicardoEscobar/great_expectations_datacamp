"""
Create and Run a Validation Definition
Time to create and run your first Validation Definition.

The Renewable Power Generation dataset has already been loaded into a pandas DataFrame dataframe and read into a Batch Definition batch_definition. An Expectation Suite has been created and assigned to the variable suite. Great Expectations and pandas are available as gx and pd, respectively.
"""

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

# Create a Validation Definition named "my_validation_definition" from your Batch Definition and Expectation Suite.
# Create Validation Definition
validation_definition = gx.ValidationDefinition(
  data=batch_definition, 
  suite=suite, 
  name="my_validation_definition"
)

# Add your Expectation Suite to the Data Context.
suite = context.suites.add(suite=suite)

# Validate your Expectation Suite by running your Validation Definition.
# Print out the success status of your Validation Results.
# Validate Expectation Suite
validation_results = validation_definition.run(
    batch_parameters={"dataframe": dataframe}
)

# View success status of Validation Results
print(validation_results.success)

# Validation Definition vs. Batch Definition
# Now, let's practice validating your Expectation Suite using two different techniques.

# The Renewable Power Generation dataset has already been loaded into a pandas DataFrame dataframe and read into a Batch Definition batch_definition. An Expectation Suite has been created and assigned to the variable suite. Great Expectations and pandas are available as gx and pd, respectively.
# Create Validation Definition
validation_definition = gx.ValidationDefinition(
  data=batch_definition,
  suite=suite, 
  name="my_validation_definition2"
)

# Validate Expectation Suite
validation_results = validation_definition.run(
    batch_parameters={"dataframe": dataframe}
)

# Describe Validation Results
print(validation_results.describe())

# Create a Batch Definition.
# Run the Batch Definition on your Expectation Suite.
# Describe the Validation Results.

# Get Batch
batch = batch_definition.get_batch(
  batch_parameters={"dataframe": dataframe}
)

# Validate Expectation Suite
validation_results = batch.validate(
  expect=suite
)

# Describe Validation Results
print(validation_results.describe())
