import sqlite3 as sql
import pandas as pd
import os
import json
import re
from datetime import datetime
import logging

from src.code.constants import (
    HOSPITALS_QUERY_TEMPLATE, CRASHES_QUERY_TEMPLATE,
    CRASHES, HOSPITALS, UTILS_PATH, AFTER_ETL,
    CURRENT_FILENAMES_FILE, METABASE_DATA_PATH,
    HOSPITALS_ETL_COLS, CRASH_DATE, CRASH_TIME,
    LOCATION_1, COORDINATES, LOCATION, CRASHES_ETL_COLS
)

def run_etl_crashes() -> None:
    """
    Run ETL process for vehicle crashes data.

    :return:
    """

    with open(os.path.join(UTILS_PATH, CURRENT_FILENAMES_FILE), "r") as f:
        FILENAMES = json.load(f)

    filename = FILENAMES[CRASHES]
    conn = sql.connect(f"{METABASE_DATA_PATH}{filename}.db")
    query = f"{CRASHES_QUERY_TEMPLATE} '{filename}'"

    logging.info(f"ETL for {filename} has started.")

    df = pd.read_sql_query(query, conn)
    df = df.dropna(subset=[LOCATION])
    df = df.reset_index(drop=True)

    df[CRASH_DATE] = df[CRASH_DATE] + " " + df[CRASH_TIME]
    df[CRASH_DATE] = df[CRASH_DATE].apply(lambda x: datetime.strptime(x, "%m/%d/%Y %H:%M").isoformat())
    df = df.drop(CRASH_TIME, axis=1)

    df.columns = CRASHES_ETL_COLS

    filename_after_etl = f"{filename.split('.')[0]}{AFTER_ETL}.csv"
    FILENAMES[f"{CRASHES}{AFTER_ETL}"] = filename_after_etl
    conn = sql.connect(f"{METABASE_DATA_PATH}{filename_after_etl}.db")

    df.to_sql(filename_after_etl, conn, if_exists='replace', index=False)

    with open(os.path.join(UTILS_PATH, CURRENT_FILENAMES_FILE), 'w') as json_file:
        json.dump(FILENAMES, json_file, ensure_ascii=False, indent=4)

    logging.info(f"SQLite database for {filename_after_etl} sucessfully created.")

def run_etl_hospitals() -> None:
    """
    Run ETL process for hospitals data.

    :return:
    """

    with open(os.path.join(UTILS_PATH, CURRENT_FILENAMES_FILE), "r") as f:
        FILENAMES = json.load(f)

    filename = FILENAMES[HOSPITALS]
    conn = sql.connect(f"{METABASE_DATA_PATH}{filename}.db")
    query = f"{HOSPITALS_QUERY_TEMPLATE} '{filename}'"

    logging.info(f"ETL for {filename} has started.")

    df = pd.read_sql_query(query, conn)
    df = df.dropna(subset=[LOCATION_1])

    loc_extract_reg = re.compile("\(\d{2}\.\d+\,\s\-\d{2}\.\d+\)")

    df[COORDINATES] = df[LOCATION_1].apply(lambda x: loc_extract_reg.search(x).group(0))
    df[LOCATION_1] = df[LOCATION_1].apply(lambda x: loc_extract_reg.sub("", x).strip())

    df.columns = HOSPITALS_ETL_COLS

    filename_after_etl = f"{filename.split('.')[0]}{AFTER_ETL}.csv"
    FILENAMES[f"{HOSPITALS}{AFTER_ETL}"] = filename_after_etl
    conn = sql.connect(f"{METABASE_DATA_PATH}{filename_after_etl}.db")

    with open(os.path.join(UTILS_PATH, CURRENT_FILENAMES_FILE), 'w') as json_file:
        json.dump(FILENAMES, json_file, ensure_ascii=False, indent=4)

    df.to_sql(filename_after_etl, conn, if_exists='replace', index=False)

    logging.info(f"SQLite database for {filename_after_etl} sucessfully created.")