import pandas as pd
from datetime import datetime, timedelta
import os
import json
import _sqlite3 as sql
from docx import Document
from docx.shared import Inches
from matplotlib import pyplot as plt
import numpy as np
from io import BytesIO

from src.code.constants import (
    HOSPITALS_QUERY_TEMPLATE, CRASHES_QUERY_TEMPLATE,
    DATA_PATH, CRASHES, HOSPITALS,
    CURRENT_FILENAMES_FILE, METABASE_DATA_PATH,
    HOSPITALS_ETL_COLS, CRASH_DATE, CRASH_TIME,
    LOCATION_1, COORDINATES, LOCATION,
    CRASHES_ETL_COLS, CRASHES_AFTER_ETL, SELECT_ALL, DATETIME, DAY_FORMAT
)

with open(os.path.join(DATA_PATH, CURRENT_FILENAMES_FILE), "r") as f:
    FILENAMES = json.load(f)


def make_report() -> None:

    filename = FILENAMES[CRASHES_AFTER_ETL]
    conn = sql.connect(f"{METABASE_DATA_PATH}{filename}.db")

    query = f"{SELECT_ALL} '{filename}'"

    df = pd.read_sql_query(query, conn)
    df[DATETIME] = df[DATETIME].apply(lambda x: x.split('T')[0])

    yesterday = datetime.today() - timedelta(days=5) # shift for 5 days
    last_week = set([(yesterday - timedelta(days=x)).strftime(DAY_FORMAT) for x in range(7)])
    last_month = set([(yesterday - timedelta(days=x)).strftime(DAY_FORMAT) for x in range(30)])
    yesterday = yesterday.strftime(DAY_FORMAT)

    yesterday_data = df[df[DATETIME] == yesterday]
    last_week_data = df[df[DATETIME].isin(last_week)]
    last_month_data = df[df[DATETIME].isin(last_month)]

    names = [f"Yesterday ({(datetime.today() - timedelta(days=1)).strftime('%d %B %Y')})", "Last Week", "Last Month"]
    datasets = [yesterday_data, last_week_data, last_month_data]

    document = Document()

    document.add_heading("Crash Report", 0)
    document.add_heading(f"Report is generated on {datetime.today().strftime('%d %B %Y')}", 1)

    for name, data in zip(names, datasets):
        document.add_paragraph()

        injured = int(data["persons_injured"].sum())
        killed = int(data['persons_killed'].sum())
        street_info = data['street_name'].value_counts()[:10].to_dict()

        document.add_paragraph(f"{name}:")
        document.add_paragraph(f"Number of accidents: {len(data)}")
        document.add_paragraph(f"Number of people injured: {injured}")
        document.add_paragraph(f"Number of people killed: {killed}")

        memfile = BytesIO()
        plt.figure(figsize=(6, 4))
        plt.barh(np.arange(9, -1, -1), street_info.values())
        plt.yticks(np.arange(9, -1, -1), street_info.keys())
        plt.ylabel('Street Name')
        plt.xlabel('Number of Accidents')
        plt.grid()
        plt.tight_layout()
        plt.savefig(memfile)

        document.add_picture(memfile, width=Inches(6))

    document.save('report.docx')

make_report()