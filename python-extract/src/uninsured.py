#!/usr/bin/env python3
from censusreporter_api import *
from sqlalchemy import create_engine
from google.cloud import bigquery

def main():

    engine = create_engine("mysql+mysqlconnector://root:root@mysql:3306/db")
    df_uninsured = pd.read_excel(open('/src/data/uninsured-estimates-state-eligibility-2021.xlsx', 'rb'), sheet_name='All Uninsured (#)')
    df_uninsured.to_sql('uninsurance_2021', con=engine, if_exists='replace', index=False)
    print(df_uninsured)

if __name__ == "__main__":
    main()