import pandas as pd
import requests

# Step 1: Read data from Excel
excel_file = "servers.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Extract server names
server_names = df['ServerName'].tolist()

# Step 3: Make API requests for each server
api_base_url = "https://fetch-server.com/api/v1/patch/node/"

for server_name in server_names:
    api_url = api_base_url + server_name
    response = requests.get(api_url)
    
    # Step 4: Handle response
    if response.status_code == 200:
        result = response.json()
        # Process result
        print(f"Info for server {server_name}: {result}")
    else:
        print(f"Error fetching info for server {server_name}: {response.status_code}")
