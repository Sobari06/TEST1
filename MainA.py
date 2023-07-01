import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import streamlit as st


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('united-option-379311-32c22a337d18.json', scope)
client = gspread.authorize(credentials)

sheet_id1 = '1ble8oYGa8kQBrOUAcLox2QhbBWx1pRXIp7fXR6UjeYk'
spreadsheet = client.open_by_key(sheet_id1)

sheet_name = 'Table'  # Ganti dengan nama sheet yang diinginkan
worksheet = spreadsheet.worksheet(sheet_name)

data = worksheet.get_all_values()
df = pd.DataFrame(data)

print(df)
st.write(df)




#https://docs.google.com/spreadsheets/d/1ble8oYGa8kQBrOUAcLox2QhbBWx1pRXIp7fXR6UjeYk/edit#gid=1372289488
sheet_id1 = '1ble8oYGa8kQBrOUAcLox2QhbBWx1pRXIp7fXR6UjeYk'
dfA = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id1}/export?format=csv')
print(dfA)