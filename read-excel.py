import pandas as pd
import requests

# Step 1: Read data from Excel
excel_file = "servers.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Extract server names
server_names = df['ServerName'].tolist()

# Step 3: Format data
data = {
    'servers': server_names
}

# Step 4: Make API request
api_url = "http://example.com/api"
response = requests.post(api_url, json=data)

# Step 5: Handle response
if response.status_code == 200:
    result = response.json()
    # Process result
    print(result)
else:
    print("Error:", response.status_code)
    print(response.text)
