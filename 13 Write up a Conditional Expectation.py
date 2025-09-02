"""
Write up a Conditional Expectation
Taking a look at the Shein dataset, you can probably come up with a few Conditional Expectations. One such Expectation could be that the star_rating of a product should be 0.0 if the product has no reviews. Let's practice establishing this Conditional Expectation.

A Batch connected to the Shein Footwear dataset has already been created and assigned to the variable batch. Great Expectations and pandas are available as gx and pd, respectively.

Establish an Expectation that all values in the star_rating column should equal 0.0 for rows with a review_count of 0.
"""

# Establish Conditional Expectation
expectation = gx.expectations.ExpectColumnValuesToBeInSet(
    column='star_rating',
    value_set={0.0},
    condition_parser='pandas',
    row_condition='review_count==0',
)

"""
Run your Expectation.
Print out the success status of the Expectation.
"""

# Establish Conditional Expectation
expectation = gx.expectations.ExpectColumnValuesToBeInSet(
    column='star_rating',
    value_set={0.0},
    condition_parser='pandas',
    row_condition='review_count==0',
)

# Run Expectation
results = batch.validate(expectation)

# Print success status
print(results.success)

"""
Invert a Conditional Expectation
It's important to keep in mind that, as with conditional probability, Conditional Expectations are not necessarily equal to their inverse. An Expectation of Column A conditional on Column B might succeed, but its inverse may not. Let's explore that in this exercise.

A Batch connected to the Shein Footwear dataset has already been created and assigned to the variable batch. Great Expectations and pandas are available as gx and pd, respectively.
"""

# Establish Conditional Expectation
# Establish Conditional Expectation
expectation = gx.expectations.ExpectColumnValuesToBeInSet(
    column='star_rating',
    value_set={0.0},
    condition_parser='pandas',
    row_condition='seller_name.isnull()',
)

# Run Expectation
results = batch.validate(expectation)

# Print success status
print(results.success)

"""

Create and run an Expectation that all values in the seller_name column be null for rows with star_rating equal to 0.0.
"""

# Establish Conditional Expectation
expectation = gx.expectations.ExpectColumnValuesToBeNull(
    column='seller_name',
    condition_parser='pandas',
    row_condition='star_rating==0.0',
)

# Run Expectation
results = batch.validate(expectation)

# Print success status
print(results.success)

