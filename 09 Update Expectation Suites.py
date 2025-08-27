"""
Copy an Expectation
In this exercise, you'll practice copying an Expectation from one Expectation Suite to another, without producing an error. Two Expectation Suites have already been created for you: one called suite and one called new_suite. The Expectation you will copy has been assigned to the variable expectation. Great Expectations and pandas are available as gx and pd, respectively.
"""
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
new_suite = gx.ExpectationSuite(name="my_new_suite")

# Create Expectation
expectation = gx.expectations.ExpectTableColumnCountToEqual(value=17)

# Copy Expectation (using deprecated copy() method since model_copy() is not available)
expectation_copy = expectation.copy()
# Set New Expectation ID to None
expectation_copy.id = None

# Add new Expectation to Suite
new_suite.add_expectation(
  expectation=expectation_copy
)
suite.add_expectation(
  expectation=expectation
)

# Check that Expectation was added
print(expectation_copy in new_suite.expectations)

# Delete the Expectation
suite.delete_expectation(
  expectation=expectation
)

# ExpectationSuite 'my_suite' must be added to the DataContext before it can be updated. Please call `context.suites.add(<SUITE_OBJECT>)`, then try your action again.
context.suites.add(suite)

# Save changes
suite.save()

# Create Validation Definition
validation_definition = gx.ValidationDefinition(
  data=batch_definition, 
  suite=suite, 
  name="my_validation_definition"
)

# Run the Validation Definition
validation_definition.run(
  batch_parameters={"dataframe": dataframe}
)

# Add expectation to suite
suite.add_expectation(
  expectation=expectation
)

# Update Expectation
expectation.value = 18

# Save Expectation
expectation.save()

# Validate Expectation
validation_results = batch.validate(
	expect=expectation
)

# Get success status of Validation Results
print(validation_results.success)