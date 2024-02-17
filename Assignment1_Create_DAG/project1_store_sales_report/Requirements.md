## Project Goal: 
- Build an Airflow application to automate daily profit reporting for a retail store chain.

## Inputs:
- Daily CSV file containing transaction data from all stores.

## Data Format:
- Each row represents a single transaction.
### Columns include:
- STORE_ID (unique)
- STORE_LOCATION (may contain special characters)
- PRODUCT_CATEGORY
- PRODUCT_ID
- MRP (with $)
- CP (cost price)
- DISCOUNT
- SP (selling price)
DATE (the previous day)


## Requirements:
- Identify the location with the highest daily profit.
- Calculate the daily profit for each individual store.


## Implementation Steps:

1) Read and Clean Data:
- Read the daily CSV file.
- Remove unwanted characters from STORE_LOCATION.
- Remove dollar signs from MRP and convert to numeric values.
2) Store Data:
- Store the cleansed data in a database.
3) Calculate Profit:
- Write SQL queries to calculate:
- Daily profit for each store.
- Total profit for each location (grouped by STORE_LOCATION).
## Output Reports:
- Generate CSV files containing the calculated profit results.
- Send Reports:
Email the generated reports to the company's email address.


