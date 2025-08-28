"""
Add and list components
You'll now practice adding components to your Data Context, and listing out the components in your Data Context. Pay special attention to how Data Sources differ from the rest of the components in this exercise.

The Context has already been created for you and assigned to the variable context. Great Expectations and pandas are available as gx and pd, respectively.
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

# List out Expectation Suites
print(context.suites.all())

# Add Expectation Suite to Data Context
suite = context.suites.add(
	gx.ExpectationSuite(name="my_suite")
)

# List out Expectation Suites again
print(context.suites.all())

# Add Checkpoint to Data Context
checkpoint = context.checkpoints.add(
	gx.Checkpoint(
      name="my_checkpoint", 
      validation_definitions=[]
    )
)

# List out Checkpoints again
print(context.checkpoints.all())

# Add pandas Data Source to Data Context
data_source = context.data_sources.add_pandas(
	name="my_data_source"
)

# List out Data Sources again
print(context.data_sources.all())

# List Checkpoints
checkpoints = context.checkpoints.all()
print(checkpoints)

# Add Checkpoint to Data Context
checkpoint = context.checkpoints.add(
	gx.Checkpoint(
      name="checkpoint_2", 
      validation_definitions=[]
    )
)

# Retrieve Checkpoint
checkpoint = context.checkpoints.get(
  name="checkpoint_2"
)

# Print name of Checkpoint
print(checkpoint.name)


# Add Checkpoint to Data Context
checkpoint = context.checkpoints.add(
	gx.Checkpoint(
      name="checkpoint_1", 
      validation_definitions=[]
    )
)

# Delete Checkpoint
context.checkpoints.delete(
  name="checkpoint_1"
)

# List out Checkpoints
print(context.checkpoints.all())