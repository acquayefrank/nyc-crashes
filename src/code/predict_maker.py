import os
import json
import sqlite3 as sql
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from catboost import CatBoostRegressor
from typing import List
import logging

from constants import (
    UTILS_PATH, STREETS_FOR_PREDICTIONS_FILE,
    CURRENT_FILENAMES_FILE, SELECT_DATETIME_STREETS_QUERY,
    METABASE_DATA_PATH, CRASHES_AFTER_ETL, STREET_NAME, DATETIME,
    DAY_FORMAT, PREDICTOR_FILE
)

def build_predictions() -> List[str]:
    """
    Makes number of crashes prediction for tomorrow for each street from STREETS_FOR_PREDICTIONS_FILE list.

    :return: list, top-10 streets where accidents are more likely to occur tomorrow.
    """

    with open(os.path.join(UTILS_PATH, STREETS_FOR_PREDICTIONS_FILE)) as f:
        streets_for_predictions = f.read().split('\n')

    street_to_id = {street: ind for ind, street in enumerate(streets_for_predictions)}

    yesterday = datetime.today() - timedelta(days=7) # shift for 5 days
    last_month = set([(yesterday - timedelta(days=x)).strftime(DAY_FORMAT) for x in range(30)])

    with open(os.path.join(UTILS_PATH, CURRENT_FILENAMES_FILE), "r") as f:
        FILENAMES = json.load(f)

    filename = FILENAMES[CRASHES_AFTER_ETL]
    conn = sql.connect(f"{METABASE_DATA_PATH}{filename}.db")
    query = f"{SELECT_DATETIME_STREETS_QUERY} '{filename}'"
    df = pd.read_sql_query(query, conn)

    df[DATETIME] = df[DATETIME].apply(lambda x: x.split("T")[0])
    df = df[df[STREET_NAME].isin(streets_for_predictions)]
    df = df.reset_index(drop=True)

    df = df[df[DATETIME].isin(last_month)]
    df[DATETIME] = pd.to_datetime(df[DATETIME])
    df = df.reset_index(drop=True)

    uniq_dates = sorted(set(df[DATETIME]))
    date_to_id = {date: idd for idd, date in enumerate(uniq_dates)}

    X = np.zeros((len(street_to_id), len(date_to_id)), dtype=np.uint32)

    for row in df.iterrows():
        info = row[1]
        date = info[DATETIME]
        street = info[STREET_NAME]

        date_id = date_to_id[date]
        street_id = street_to_id[street]

        X[street_id, date_id] += 1

    model = CatBoostRegressor()
    model.load_model(os.path.join(UTILS_PATH, PREDICTOR_FILE))

    y_pred = model.predict(X)
    top_10_strets_inds = np.argsort(y_pred)[::-1][:10]
    top_10_streets = [streets_for_predictions[ind] for ind in top_10_strets_inds]

    logging.info("Predictions sucessfully made.")

    return top_10_streets


