import logging

from data_downloader import (
    download_data,
    export_csv_to_sqlite
)

from etl_procuder import (
    run_etl_crashes,
    run_etl_hospitals
)

from report_maker import make_report
from visualization_maker import make_visualization

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

if __name__ == "__main__":

    download_data()
    export_csv_to_sqlite()
    run_etl_crashes()
    run_etl_hospitals()
    make_report()
    make_visualization()