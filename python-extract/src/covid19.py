#!/usr/bin/env python3
from censusreporter_api import *
from sqlalchemy import create_engine
from google.cloud import bigquery

def main():

    engine = create_engine("mysql+mysqlconnector://root:root@mysql:3306/db")
    client = bigquery.Client()
    sql = """
    WITH tmp AS
    (SELECT state_name state_name_1, MAX(date) date_1 
    FROM `claroinsurance.covid19.us_states`
    GROUP BY state_name)
    SELECT * EXCEPT (state_name_1,date_1) FROM `claroinsurance.covid19.us_states` a
    INNER JOIN tmp b
        ON a.state_name = b.state_name_1 AND a.date = b.date_1;
    """    
    df_covid19 = client.query(sql).to_dataframe()
    df_covid19.to_sql('covid19', con=engine, if_exists='replace', index=False)
    print(df_covid19)

if __name__ == "__main__":
    main()


