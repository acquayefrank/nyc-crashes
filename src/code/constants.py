CRASHES = "crashes"
HOSPITALS = "hospitals"
CURRENT_FILENAMES_FILE = "current_filenames.json"

LOCATION_1 = "Location 1"
COORDINATES = "coordinates"
LOCATION = "LOCATION"
CRASH_DATE = "CRASH DATE"
CRASH_TIME = "CRASH TIME"

VEHICLE_CRASHES_LINK = "https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD"
HOSPITALS_LINK = "https://data.cityofnewyork.us/api/views/ymhw-9cz9/rows.csv?accessType=DOWNLOAD"

DATA_PATH = "../data/"
METABASE_DATA_PATH = "../metabase-data/"

HOSPITALS_QUERY_TEMPLATE = "SELECT `Facility Name`, `Facility Type`, `Borough`, `Location 1` FROM"
CRASHES_QUERY_TEMPLATE = "SELECT `CRASH DATE`, `CRASH TIME`, `LOCATION`, `ON STREET NAME`, `NUMBER OF PERSONS INJURED`,\
`NUMBER OF PERSONS KILLED`, `VEHICLE TYPE CODE 1`, `VEHICLE TYPE CODE 2`, `VEHICLE TYPE CODE 3`, \
`VEHICLE TYPE CODE 4`, `VEHICLE TYPE CODE 5` FROM"

HOSPITALS_ETL_COLS = ["facility_name", "facility_type", "borough", "address", "coordinates"]
CRASHES_ETL_COLS = ["datetime", "location", "street_name", "persons_injured", "persons_killed", "vehicle_1",
                    "vehicle_2", "vehicle_3", "vehicle_4", "vehicle_5", ]