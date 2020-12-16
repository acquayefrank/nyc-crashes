CRASHES = "crashes"
HOSPITALS = "hospitals"
DEPARTMENTS = "departments"

CRASHES_AFTER_ETL = "crashes_after_etl"
HOSPITALS_AFTER_ETL = "hospitals_after_etl"

CURRENT_FILENAMES_FILE = "current_filenames.json"
STREETS_FOR_PREDICTIONS_FILE = "streets_for_predictions.txt"
PREDICTOR_FILE = "catboost_predictor.dump"
CRASH_MAP_FILE = "crash_map.html"
REPORT_FOR_CITIZENS_FILE = "report_for_citizens.docx"
REPORT_FOR_MAYOR_FILE = "report_for_mayor.docx"
DEPARTMENTS_FILE = "police_departments_data.csv"

LOCATION = "LOCATION"
CRASH_DATE = "CRASH DATE"
CRASH_TIME = "CRASH TIME"
LOCATION_1 = "Location 1"
COORDINATES = "coordinates"
DATETIME = "datetime"
TIME = "time"
STREET_NAME = "street_name"
DAY_FORMAT = "%Y-%m-%d"
AFTER_ETL = "_after_etl"

VEHICLE_CRASHES_LINK = "https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD"
HOSPITALS_LINK = "https://data.cityofnewyork.us/api/views/ymhw-9cz9/rows.csv?accessType=DOWNLOAD"

DATA_PATH = "../data/"
METABASE_DATA_PATH = "../metabase-data/"
UTILS_PATH = "utils/"
RESULT_FOLDER = "../result_folder/"

HOSPITALS_QUERY_TEMPLATE = "SELECT `Facility Name`, `Facility Type`, `Borough`, `Location 1` FROM"
CRASHES_QUERY_TEMPLATE = "SELECT `CRASH DATE`, `CRASH TIME`, `LOCATION`, `ON STREET NAME`, `NUMBER OF PERSONS INJURED`,\
`NUMBER OF PERSONS KILLED`, `VEHICLE TYPE CODE 1`, `VEHICLE TYPE CODE 2`, `VEHICLE TYPE CODE 3`, \
`VEHICLE TYPE CODE 4`, `VEHICLE TYPE CODE 5` FROM"
SELECT_ALL_QUERY = "SELECT * FROM"
SELECT_DATETIME_STREETS_QUERY = "SELECT `datetime`, `street_name` FROM"

HOSPITALS_ETL_COLS = ["facility_name", "facility_type", "borough", "address", "coordinates"]
CRASHES_ETL_COLS = ["datetime", "location", "street_name", "persons_injured", "persons_killed", "vehicle_1",
                    "vehicle_2", "vehicle_3", "vehicle_4", "vehicle_5", ]