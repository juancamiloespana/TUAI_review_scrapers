import requests
import pandas as pd
import openpyxl


def get_osf_metadata_comprehensive(filters):
    """
    Fetches OSF registrations using multiple filters and returns all attributes,
    including the unique Registry ID (GUID).
    """
    # Construct the base URL
    base_url = "https://api.osf.io/v2/registrations/"
    
    # Build filter string
    filter_params = "&".join([f"filter[{k}]={v}" for k, v in filters.items()])
    url = f"{base_url}?{filter_params}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        registrations = data['data']
        
        records = []
        for reg in registrations:
            # 1. Start with the unique GUID found at the top level
            record = {'id': reg['id']}
            
            # 2. Add the URL directly for easy access in your audit
            record['url'] = f"https://osf.io/{reg['id']}/"
            
            # 3. Update the dictionary with all items in the 'attributes' block
            record.update(reg['attributes'])
            
            records.append(record)
        
        return pd.DataFrame(records)
    else:
        print(f"Error {response.status_code}: {response.text}")
        return pd.DataFrame()

# Execution with your criteria
search_criteria = {
    "description": "Large Language Model",
}

df = get_osf_metadata_comprehensive(search_criteria)

df.shape

# Ensure the 'id' column is at the beginning for better visibility
if not df.empty:
    cols = ['id'] + [c for c in df.columns if c != 'id']
    df = df[cols]



df.to_excel("H:/Mi unidad/cod1/TUAI_review_scrapers/outputs/osf_registrations.xlsx", index=False)

df['subjects']