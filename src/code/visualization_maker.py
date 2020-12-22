import os
import json
import sqlite3 as sql
import pandas as pd
from datetime import datetime, timedelta
import folium
import logging

from constants import (
    UTILS_PATH, CURRENT_FILENAMES_FILE, RESULT_FOLDER,
    CRASHES_AFTER_ETL, METABASE_DATA_PATH,
    SELECT_ALL_QUERY, HOSPITALS_AFTER_ETL, DEPARTMENTS,
    DATETIME, DAY_FORMAT, TIME, CRASH_MAP_FILE
)

def make_visualization() -> None:
    """
    Make visualization of hospitals, police departments and recent crashes.
    Visualization is saved to CRASH_MAP_FILE.

    :return:
    """

    with open(os.path.join(UTILS_PATH, CURRENT_FILENAMES_FILE), "r") as f:
        FILENAMES = json.load(f)

    logging.info("Visualization is being created.")

    yesterday = datetime.today() - timedelta(days=7)  # shift for 7 days
    yesterday = yesterday.strftime(DAY_FORMAT)
    dataframes = []

    for file in [CRASHES_AFTER_ETL, HOSPITALS_AFTER_ETL, DEPARTMENTS]:
        new_file = FILENAMES[file]

        conn = sql.connect(f"{METABASE_DATA_PATH}{new_file}.db")
        query = f"{SELECT_ALL_QUERY} '{new_file}'"
        new_df = pd.read_sql_query(query, conn)
        dataframes.append(new_df)

    crashes_df, hospitals_df, departments_df = dataframes

    crashes_df[TIME] = crashes_df[DATETIME].apply(lambda x: x.split("T")[1])
    crashes_df[DATETIME] = crashes_df[DATETIME].apply(lambda x: x.split("T")[0])
    yesterday_data = crashes_df[crashes_df[DATETIME] == yesterday]

    ny_map = folium.Map(location=[40.7306, -73.9352])

    for row in yesterday_data.itertuples():
        time = row.time
        location = row.location
        street_name = row.street_name
        location = [float(coord) for coord in location[1:-1].split(', ')]

        popup_msg = f"Crash Time: {time}, Street: {street_name}"
        popup = folium.Popup(popup_msg, max_width=300)

        folium.Marker(
            location=location,
            popup=popup,
            icon=folium.Icon(color='red', icon='info', prefix='fa')
        ).add_to(ny_map)

    for row in hospitals_df.itertuples():
        name = row.facility_name
        location = row.coordinates
        location = [float(coord) for coord in location[1:-1].split(', ')]

        popup_msg = f"Hospital: {name}"
        popup = folium.Popup(popup_msg, max_width=300)

        folium.Marker(
            location=location,
            popup=popup,
            icon=folium.Icon(color='green', icon='ambulance', prefix='fa')
        ).add_to(ny_map)

    for row in departments_df.itertuples():
        precinct = row.precinct
        phone = row.phone
        location = row.location
        location = [float(coord) for coord in location[1:-1].split(', ')]

        popup_msg = f"Precinct: {precinct}, Phone number: {phone}"
        popup = folium.Popup(popup_msg, max_width=300)

        folium.Marker(
            location=location,
            popup=popup,
            icon=folium.Icon(color='blue', icon='user', prefix='fa')
        ).add_to(ny_map)

    today = datetime.today().strftime(DAY_FORMAT)
    report_for_citizens = f"{CRASH_MAP_FILE}-{today}.html"

    ny_map.save(os.path.join(RESULT_FOLDER, report_for_citizens))
    logging.info("Visualization successfully created.")
    logging.info("All processes completed successfully.")