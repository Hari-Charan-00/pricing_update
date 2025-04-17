import pandas as pd
 
def calculate_new_price(row, pricing_rules):
 
    new_price = row['current_price']

    for rule in pricing_rules:

        if rule['condition'](row):

            new_price = rule['adjustment'](row, new_price)
 
    # Ensure minimum profit

    min_price = row['cost_price'] * 1.20

    return round(max(new_price, min_price), 2)
 
 
def apply_pricing_rules(products_df, sales_df, pricing_rules):
 
    # Merge product and sales data

    merged_df = pd.merge(products_df, sales_df, on='sku', how='left').fillna({'quantity_sold': 0})
 
    # Apply pricing rules row-wise

    merged_df['new_price'] = merged_df.apply(lambda row: calculate_new_price(row, pricing_rules), axis=1)
 
    # Format the prices to two decimal places and add a currency unit.

    merged_df['new_price'] = merged_df['new_price'].apply(lambda price: f'${price:.2f}')

    merged_df['current_price'] = merged_df['current_price'].apply(lambda price: f'${price:.2f}') # added formatting
 
    return merged_df
 
def main():

    # Load data from CSV files

    products_df = pd.read_csv('products.csv')

    sales_df = pd.read_csv('sales.csv')
 
    # Clean column names

    products_df.columns = products_df.columns.str.strip().str.lower().str.replace(' ', '_')

    sales_df.columns = sales_df.columns.str.strip().str.lower().str.replace(' ', '_')
 
    # Define the pricing rules

    pricing_rules = [

        {

            'condition': lambda row: row['stock'] <= 20 and row['quantity_sold'] > 30,

            'adjustment': lambda row, price: price * 1.15,

        },

        {

            'condition': lambda row: row['stock'] > 200 and row['quantity_sold'] == 0,

            'adjustment': lambda row, price: price * 0.70,

        },

        {

            'condition': lambda row: row['stock'] > 100 and row['quantity_sold'] < 20,

            'adjustment': lambda row, price: price * 0.90,

        },

    ]
 
    # Apply the pricing rules

    final_df = apply_pricing_rules(products_df, sales_df, pricing_rules)
 
    # Save the results to a CSV file

    final_df[['sku', 'current_price', 'new_price']].to_csv('updated_prices.csv', index=False)

    print("Successfully saved updated prices to updated_prices.csv")

if __name__ == "__main__":
    main()
