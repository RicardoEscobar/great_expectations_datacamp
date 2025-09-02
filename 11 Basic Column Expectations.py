"""
Establish row-level Expectations
In this exercise, you'll practice writing some column-specific Expectations at the row level. You'll be using the same Shein footwear dataset from the video. You can learn more about the dataset here.

The Batch has already been assigned to a variable called batch and loaded with the Shein Footwear dataset. Great Expectations and pandas are available as gx and pd, respectively.
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

# Establish missingness Expectation
expectation = gx.expectations.expectation = gx.expectations.ExpectColumnValuesToNotBeNull(
  column="name"
)

# Run the Expectation
validation_results = batch.validate(expect=expectation)

# Print the success status
print(validation_results.success)

"""
Establish row-level Expectations
In this exercise, you'll practice writing some column-specific Expectations at the row level. You'll be using the same Shein footwear dataset from the video. You can learn more about the dataset here.

The Batch has already been assigned to a variable called batch and loaded with the Shein Footwear dataset. Great Expectations and pandas are available as gx and pd, respectively.
"""

# Add an Expectation that the "sku_id" column be of string type.
# Establish type Expectation
expectation = gx.expectations.ExpectColumnValuesToBeOfType(
  column="sku_id", type_="str"
)

# Run the Expectation
validation_results = batch.validate(expect=expectation)

# Print the success status
print(validation_results.success)

"""
Establish aggregate-level Expectations
Time to practice writing some column-specific Expectations at the aggregate level. The Expectation Suite and Batch have already been assigned to the variables suite and batch, respectively, and loaded with the Shein Footwear dataset. Great Expectations and pandas are available as gx and pd, respectively.

Add the following column Expectations:
"colour": in the set "Khaki", "Purple", or "Grey"
"seller_name": 7 to 10 distinct values
"link": all unique values
"review_count": most common value in the set "0" or "100+"
"""
# "colour" should be in the set "Khaki", "Purple", or "Grey"
colour_expectation = gx.expectations.ExpectColumnDistinctValuesToBeInSet(
    column="colour", value_set={"Khaki", "Purple", "Grey"}
)

# "seller_name" should have 7 to 10 distinct values
seller_expectation = gx.expectations.ExpectColumnUniqueValueCountToBeBetween(
    column="seller_name", min_value=7, max_value=10
)

# "link" should have all unique values
link_expectation = gx.expectations.ExpectColumnValuesToBeUnique(
    column="link"
)

# "review_count" should have a most common value in the set "0" or "100+"
review_count_expectation = gx.expectations.ExpectColumnMostCommonValueToBeInSet(
    column="review_count", value_set={"0", "100+"}
)

"""
Establish aggregate-level Expectations
Time to practice writing some column-specific Expectations at the aggregate level. The Expectation Suite and Batch have already been assigned to the variables suite and batch, respectively, and loaded with the Shein Footwear dataset. Great Expectations and pandas are available as gx and pd, respectively.

Add your Expectations to the Expectation Suite suite.
Print out the number of Expectations in your Expectation Suite.
"""

# Create suite
suite = gx.expectations.ExpectationSuite("shein_footwear_suite")

# "colour" should be in the set "Khaki", "Purple", or "Grey"
colour_expectation = gx.expectations.ExpectColumnDistinctValuesToBeInSet(
    column="colour", value_set={"Khaki", "Purple", "Grey"}
)

# "seller_name" should have 7 to 10 distinct values
seller_expectation = gx.expectations.ExpectColumnUniqueValueCountToBeBetween(
    column="seller_name", min_value=7, max_value=10
)

# "link" should have all unique values
link_expectation = gx.expectations.ExpectColumnValuesToBeUnique(
    column="link"
)

# "review_count" should have a most common value in the set "0" or "100+"
review_count_expectation = gx.expectations.ExpectColumnMostCommonValueToBeInSet(
	column="review_count", value_set={"0", "100+"}
)

# Create list of Expectations
expectations = [
  	colour_expectation,
  	seller_expectation, 
  	link_expectation, 
  	review_count_expectation
]

# Add Expectations to Suite
for expectation in expectations:
    suite.add_expectation(expectation)

# Print out number of Expectations
print(len(suite.expectations))


"""
Establish aggregate-level Expectations
Time to practice writing some column-specific Expectations at the aggregate level. The Expectation Suite and Batch have already been assigned to the variables suite and batch, respectively, and loaded with the Shein Footwear dataset. Great Expectations and pandas are available as gx and pd, respectively.

Run your Validation.
Print the success status of the Validation Result.
"""

# "colour" should be in the set "Khaki", "Purple", or "Grey"
colour_expectation = gx.expectations.ExpectColumnDistinctValuesToBeInSet(
    column="colour", value_set={"Khaki", "Purple", "Grey"}
)

# "seller_name" should have 7 to 10 distinct values
seller_expectation = gx.expectations.ExpectColumnUniqueValueCountToBeBetween(
    column="seller_name", min_value=7, max_value=10
)

# "link" should have all unique values
link_expectation = gx.expectations.ExpectColumnValuesToBeUnique(
    column="link"
)

# "review_count" should have a most common value in the set "0" or "100+"
review_count_expectation = gx.expectations.ExpectColumnMostCommonValueToBeInSet(
	column="review_count", value_set={"0", "100+"}
)

# Create list of Expectations
expectations = [
  	colour_expectation,
  	seller_expectation, 
  	link_expectation, 
  	review_count_expectation
]

# Add Expectations to Suite
for expectation in expectations:
    suite.add_expectation(expectation)

# Run validation
validation_results = batch.validate(expect=suite)

# Print success status of Validation Results
print(validation_results.success)