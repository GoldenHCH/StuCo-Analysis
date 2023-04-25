import gspread
from oauth2client import service_account as sv_acc
import pandas as pd

scopes = {
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
          }

creds = sv_acc.ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scopes=scopes)

# read data from sheet into a pandas dataframe
file = gspread.authorize(creds)
worksheet = file.open('Analysis of things that make an event successful  (Responses)').sheet1
data = worksheet.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

print(df)