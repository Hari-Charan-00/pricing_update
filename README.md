Price Calculation Project README
1. Introduction
This project calculates new prices for products based on a set of rules, incorporating product and sales data from CSV files. The core logic is implemented in Python using the Pandas library for efficient data manipulation.

2. Files
2.1 Input Files
products.csv: Contains product information, including SKU, current price, cost price, and stock quantity.

sales.csv: Contains sales data, including SKU and quantity sold.

2.2 Output File
updated_prices.csv: A CSV file containing the original product data along with the calculated new prices.

3. Data Processing
Data Loading:

The script reads the product and sales data from the input CSV files into Pandas DataFrames.

Data Cleaning:

Column names in both DataFrames are standardized by:

Removing leading/trailing whitespace.

Converting to lowercase.

Replacing spaces with underscores.

Data Merging:

The product and sales DataFrames are merged using the SKU as the key. A left merge is performed to ensure all products are included, even if they have no corresponding sales data.

Missing quantity sold values (for products with no sales) are filled with 0.

Price Calculation:

The script applies a set of pricing rules to each product to determine the new price.  The rules are implemented in the calculate_new_price function.

The rules are as follows:

Rule 1: If stock is less than or equal to 20 and quantity sold is greater than 30, the price is increased by 15%.

Rule 2: If stock is greater than 200 and quantity sold is 0, the price is reduced by 30%.

Rule 3: If stock is greater than 100 and quantity sold is less than 20, the price is reduced by 10%.

Rule 4: The new price is never less than 120% of the cost price (minimum profit margin).

The rules are applied in the order specified, with Rule 1 having the highest priority.

Price Formatting:

The calculated new prices, as well as the original prices, are formatted to two decimal places and include a dollar sign ($) as the currency unit.

Output:

The final DataFrame, containing the SKU, original price, and new price, is saved to a CSV file named "updated_prices.csv".

4. Code Structure
The code is organized into the following functions:

calculate_new_price(row, pricing_rules): Calculates the new price for a single product based on the given pricing rules.

apply_pricing_rules(products_df, sales_df, pricing_rules): Applies the pricing rules to the product DataFrame, incorporating sales data.

main():  The main function that orchestrates the data loading, processing, rule application, and output generation.

5. Dependencies
Python 3.x

Pandas

6. Execution
Place the input CSV files ("products.csv" and "sales.csv") in the same directory as the Python script.

Run the Python script.

The output file ("updated_prices.csv") will be created in the same directory.

7. Assumptions
The input CSV files are assumed to be in the correct format and encoding.

The script assumes that the column 'sku' is present in both input CSV files and is the key used to join the data.

8. Improvements
The pricing rules could be made more flexible by storing them in a separate configuration file or database.

Error handling could be further enhanced, such as adding more specific exceptions or logging.

The code could be optimized for even larger datasets by exploring alternative data structures or parallel processing techniques.
