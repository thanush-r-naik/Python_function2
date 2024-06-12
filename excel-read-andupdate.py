import pandas as pd
import requests

# Step 1: Read data from Excel
excel_file = "servers.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Extract server names
server_names = df['ServerName'].tolist()

# Step 3: Prepare authentication credentials
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # Replace YOUR_ACCESS_TOKEN with your actual access token
    'Content-Type': 'application/json'
}

# Step 4: Initialize an empty list to store data for each server
server_data = []

# Step 5: Make API requests for each server
api_base_url = "https://fetch-server.com/api/v1/patch/node/"

for server_name in server_names:
    api_url = api_base_url + server_name
    response = requests.get(api_url, headers=headers)
    
    # Step 6: Handle response
    if response.status_code == 200:
        result = response.json()
        
        # Extracting specific fields from the response
        patch_group = result.get('patch_group', 'N/A')
        hostname = result.get('hostname', 'N/A')
        patch_status = result.get('patch_status', 'N/A')
        
        # Append the data for this server to the list
        server_data.append([server_name, patch_group, hostname, patch_status])
    else:
        print(f"Error fetching info for server {server_name}: {response.status_code}")

# Step 7: Convert the list of data into a DataFrame
columns = ['ServerName', 'PatchGroup', 'Hostname', 'PatchStatus']
output_df = pd.DataFrame(server_data, columns=columns)

# Step 8: Write the DataFrame to an Excel file
output_excel_file = "output_servers_info.xlsx"
output_df.to_excel(output_excel_file, index=False)

print(f"Data written to {output_excel_file}")
