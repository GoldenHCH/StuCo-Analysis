import gspread
from oauth2client import service_account as sv_acc
import pandas as pd

def api():
    scopes = {
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
              }

    # sheet_id = "1l6DpBYExqIDhcaa7hk7Aza1LTUzwdF8UVMfM4exNXkA"
    # sheet_name = "Form Responses 1"
    # sheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(sheet_id, sheet_name)
    # df = pd.read

    creds = sv_acc.ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scopes=scopes)

    # read data from sheet into a pandas dataframe
    file = gspread.authorize(creds)
    worksheet = file.open('Analysis of things that make an event successful  (Responses)').sheet1
    data = worksheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df.drop(columns=['Time'])

    new_df = pd.DataFrame(df, columns=['Event', 'Response', "Rating"])

    return new_df