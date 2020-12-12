import schedule
import time
import requests
import csv
import pandas as pd
import sqlite3 as sql


def download(url=None):
    if not url:
        url = "https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD"
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        file_name = f'crashes-{timestr}.csv'
        with open( f'../data/{file_name}','w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerows(my_list)
    return file_name


def export_csv_to_sqlite(file_name):
    conn = sql.connect(f'../metabase-data/{file_name}.db')
    df = pd.read_csv(f'../data/{file_name}')
    df.to_sql(file_name, conn, if_exists='append', index=False)

    


def job():
    print("I'm working...")
    file_name = download()
    export_csv_to_sqlite(file_name)


# schedule.every(10).seconds.do(job)
schedule.every().day.at("23:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)