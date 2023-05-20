import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from random import randint

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')

Credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1PFVs-972x5rNeNHGKBpHelPK6D3bRa5wnnQ-VPPxvVo'
SAMPLE_RANGE_NAME = 'List1!A1:Z999'


service = build('sheets', 'v4', credentials=Credentials)
def main_parse():
# Call the Sheets API

    service = build('sheets', 'v4', credentials=Credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
        return
    f = open('text1.txt', 'w')
    button_rows_1 = values[00]
    n = 0
    for i in button_rows_1:
        if i == '':
            button_rows_1.pop(n)
        n+=1
    text = str(button_rows_1)
    f.write(text)
    f.close()




