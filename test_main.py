from import_for_main import *

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_SPREADSHEET_ID = '1PFVs-972x5rNeNHGKBpHelPK6D3bRa5wnnQ-VPPxvVo'##'1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'List1!A1:Z999'

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return
        f = open('text1.txt', 'w')
        ########################
        button_rows_1 = values[00]
        n = 0
        for i in button_rows_1:
            if i == '':
                button_rows_1.pop(n)
            n+=1
        ###########################
        #print(button_rows_1) # outputs the first line
        text = str(button_rows_1)
        # text = text.encode('UTF-8')
        f.write(text)
        f.close()
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()