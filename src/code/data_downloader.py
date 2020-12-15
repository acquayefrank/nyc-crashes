import requests
import csv
import time
import os
import sqlite3 as sql
import pandas as pd
import json

from src.code.constants import (
    CRASHES, HOSPITALS,
    VEHICLE_CRASHES_LINK,
    HOSPITALS_LINK,
    CURRENT_FILENAMES_FILE,
    DATA_PATH, METABASE_DATA_PATH
)

FILE_NAME_TO_LINK = {
    CRASHES: VEHICLE_CRASHES_LINK,
    HOSPITALS: HOSPITALS_LINK
}

def download_data() -> None:
    """
    Downloads vehicle crash and hospitals data from NYC Open Data.

    :return:
    """
    with requests.Session() as s:

        filenames = dict()

        for name, link in FILE_NAME_TO_LINK.items():

            file = s.get(link)
            file_decoded = file.content.decode("utf-8")
            file_csv = csv.reader(file_decoded.splitlines(), delimiter=",")
            file_csv = list(file_csv)

            timestr = time.strftime("%Y%m%d-%H%M%S")
            file_name = f"{name}-{timestr}.csv"
            filenames[name] = file_name

            with open(os.path.join(DATA_PATH, file_name), "w") as result_file:
                wr = csv.writer(result_file, dialect="excel")
                wr.writerows(file_csv)

            print(f"{name.title()} successfully downloaded.")

        with open(os.path.join(DATA_PATH, CURRENT_FILENAMES_FILE), 'w') as json_file:
            json.dump(filenames, json_file, ensure_ascii=False, indent=4)


def export_csv_to_sqlite() -> None:
    """
    Exports downloaded crash and hospitals data to SQLite database.

    :return:
    """

    with open(os.path.join(DATA_PATH, CURRENT_FILENAMES_FILE), 'r') as f:
        filenames = json.load(f)

    crashes_file = filenames[CRASHES]
    hospitals_file = filenames[HOSPITALS]

    for file in [crashes_file, hospitals_file]:

        conn = sql.connect(f'{METABASE_DATA_PATH}{file}.db')
        df = pd.read_csv(os.path.join(DATA_PATH, file))
        df.to_sql(file, conn, if_exists='replace', index=False)

        print(f"SQLite database for {file} sucessfully created.")

download_data()
export_csv_to_sqlite()