"""
Establish numeric Expectations
In this exercise, you'll practice establishing and validating some numeric-type Expectations, both at the aggregate- and row-levels. As you go through each of these Expectations, think about whether or not this is an Expectation you would write for this particular dataset. Is this a reasonable thing to expect of the data? Do you expect the Validation Result to be successful?

A Batch connected to the Shein Footwear dataset has already been created and assigned to the variable batch. Great Expectations and pandas are available as gx and pd, respectively.
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
datasource = context.add_datasource(
    "my_datasource",
    class_name="PandasDatasource",
    dataframes={"my_dataframe": dataframe}
)

# Create a Batch
batch = context.create_batch(dataframe)


# View head of DataFrame
print(batch.data.head())

# Create an Expectation for the median value of the "star_rating" column be between 2 and 4.
# Column median Expectation
expectation = gx.expectations.ExpectColumnMedianToBeBetween(
  column="star_rating", 
  min_value=2, 
  max_value=4,
)

# Validate Expectation and print success status
validation_results = batch.validate(
  expect=expectation
)

print(validation_results.success)


# 3
# Create an Expectation that each value of the "star_rating" column be between 1 and 5.
# Column values range Expectation
expectation = gx.expectations.ExpectColumnValuesToBeBetween(
  column="star_rating", 
  min_value=1, 
  max_value=5,
)

# Validate Expectation and print success status
validation_results = batch.validate(
  expect=expectation
)
print(validation_results.success)


# 4
# Create an Expectation that the values of the "star_rating" column be increasing.
# Column values increasing Expectation
expectation = gx.expectations.ExpectColumnValuesToBeIncreasing(
  column="star_rating"
)

# Validate Expectation and print success status
validation_results = batch.validate(
  expect=expectation
)   

print(validation_results.success)

"""
Establish string Expectations
In this exercise, you'll practice establishing and validating some string-type Expectations, including parseability Expectations. As with the previous exercise, think critically about the Expectations you create in this exercise and whether or not you think they are befitting of the data.

A Batch connected to the Shein Footwear dataset has already been created and assigned to the variable batch. Great Expectations and pandas are available as gx and pd, respectively.


"""
# View head of DataFrame
print(batch.data.head())

# Column value lengths Expectation
expectation = gx.expectations.ExpectColumnValueLengthsToBeBetween(
  column="name", 
  value=100
)

# Validate Expectation and print success status
validation_results = batch.validate(
  expect=expectation
)
print(validation_results.success)


# Regex pattern: non-zero number of words, each starting 
# with an uppercase letter or number and separated by spaces
regex = r"([A-Z\d]\S*)(\s([A-Z\d]\S*))*"

# Regex Expectation
expectation = gx.expectations.ExpectColumnValuesToMatchRegex(
  column="name", 
  regex=regex
)

# Validate Expectation and print success status
validation_results = batch.validate(
    expect=expectation
)
print(validation_results.success)


# Dateutil Expectation
expectation = gx.expectations.ExpectColumnValuesToBeDateutilParseable(
  column="name"
)

# Validate Expectation and print success status
validation_results = batch.validate(
  expect=expectation
)
print(validation_results.success)
