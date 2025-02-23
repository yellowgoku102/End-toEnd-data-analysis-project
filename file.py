import pandas as pd
from sqlalchemy import create_engine

# URL-encoded password
password = ".........."

# Create a database connection
engine = create_engine(f'mysql+pymysql://root:{password}@localhost/sales_db')

# Fetch data from the sales table
query = "SELECT * FROM sales"
df = pd.read_sql(query, engine)

print(df)

# Calculate total sales
df['total_sales'] = df['quantity'] * df['price']

# Group by product and calculate total sales per product
sales_per_product = df.groupby('product')['total_sales'].sum().reset_index()

print(sales_per_product)


# ...existing code...

# Export to Excel
sales_per_product.to_excel('sales_analysis.xlsx', index=False)




import pandas as pd
from sqlalchemy import create_engine

def fetch_data():
    # URL-encoded password
    password = "........."
    
    # Create a database connection
    engine = create_engine(f'mysql+pymysql://root:{password}@localhost/sales_db')
    
    # Fetch data from the sales table
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, engine)
    
    return df

def analyze_data(df):
    # Calculate total sales
    df['total_sales'] = df['quantity'] * df['price']
    
    # Group by product and calculate total sales per product
    sales_per_product = df.groupby('product')['total_sales'].sum().reset_index()
    
    return sales_per_product

def export_to_excel(df, filename):
    # Export to Excel
    df.to_excel(filename, index=False)

def main():
    # Fetch data
    data = fetch_data()
    print(data)
    
    # Analyze data
    analysis = analyze_data(data)
    print(analysis)
    
    # Export analysis to Excel
    export_to_excel(analysis, 'sales_analysis.xlsx')

if __name__ == "__main__":
    main()
