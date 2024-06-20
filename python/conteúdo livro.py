import pandas as pd
from tabulate import tabulate

# Creating a sample dataframe for demonstration
# Since actual market data for DESKTOP INTERNET expenses is not available, we will create a fictional dataset

data = {
    "Month": [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ],
    "Year": [2023] * 12,
    "Operating Expenses": [10000, 11000, 10500, 11500, 12000, 11800, 12500, 13000, 12800, 14000, 13500, 14500],
    "Marketing Expenses": [5000, 4800, 5100, 5000, 5300, 5500, 5600, 5700, 5900, 6100, 6200, 6300],
    "R&D Expenses": [3000, 3200, 3100, 3400, 3500, 3450, 3600, 3800, 3700, 4000, 3900, 4100],
    "Total Expenses": [18000, 19000, 18700, 19900, 20800, 20750, 21700, 22500, 22400, 24100, 23600, 24900]
}

df = pd.DataFrame(data)

df
print(tabulate(df, headers='keys', tablefmt='psql'))