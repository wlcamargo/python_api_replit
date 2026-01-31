import requests
import pandas as pd

url = "https://e5e2f3a3-454c-43de-b139-659366de071e-00-t572qw8e44wh.janeway.replit.dev/dadospessoais"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    df = pd.DataFrame([data])
    
    df.to_csv('personal_data.csv', index=False)
    
    print("Data successfully exported to personal_data.csv")
    print("\nData preview:")
    print(df)
else:
    print(f"Error: {response.status_code}")
