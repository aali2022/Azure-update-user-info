import pandas as pd
from msgraph.core import GraphClient
from azure.identity import ClientSecretCredential

# Azure AD credentials
tenant_id = 'YOUR_TENANT_ID'
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# CSV file path
csv_file = 'aduserdata.csv'

def update_user_information():
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file, dtype=str)

    # Set up the Azure AD credentials and create a GraphClient object
    credentials = ClientSecretCredential(tenant_id=tenant_id, client_secret=client_secret, client_id=client_id)
    graph_client = GraphClient(credential=credentials)

    # Iterate over the rows in the CSV file
    for index, row in df.iterrows():
        user_id = row['UserPrincipalName']
        company_name = row['CompanyName']
        department = row['Department']
        office_location = row['OfficeLocation']
        mobile_phone = row['MobilePhone']
        job_title = row['JobTitle']
        print(mobile_phone)

        # Define the user properties to update
        user_properties = {
            'companyName': company_name,
            'department': department,
            'officeLocation': office_location,
            'mobilePhone': mobile_phone,
            'jobTitle': job_title
        }

        # Update user information
        url = f'/users/{user_id}'
        response = graph_client.patch(url, json=user_properties)
        #response = graph_client.user[user_id].update(user_properties)

        if response.status_code == 204:
            print(f"Updated information for user {user_id}: Success")
        else:
            print(f"Failed to update information for user {user_id}: {response.text}")

if __name__ == '__main__':
    update_user_information()
