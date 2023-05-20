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
def main_2_parse(a, b):

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME,
                                majorDimension='COLUMNS').execute()
    values = result.get('values', [])
    # except HttpError as err:
    #     print(err)
    e = open('text2.txt', 'w')
    u = open('text2_2.txt', 'w')
    button_rows_1 = values[a]
    button_rows_2 = values[b]
    button_rows_1.pop(0)
    button_rows_1.pop(0)
    button_rows_2.pop(0)
    button_rows_2.pop(0)

    num = 0
    if len(button_rows_2) <= len(button_rows_1):
        chislo = len(button_rows_1) - len(button_rows_2)
        if chislo >= 0:
            for i in range(chislo):
                button_rows_1.pop()

    while True:
        if num <= (len(button_rows_1) - 1):
            if len(button_rows_2[num]) == 0:
                button_rows_1.pop(num)
                button_rows_2.pop(num)
                num =0
            else:
                num += 1
        else:
            break

    text = str(button_rows_1)
    e.write(text + '\n')
    e.close()
    text = str(button_rows_2)
    u.write(text)
    u.close()

#
# if __name__ == '__main__':
#     main_2_parse()