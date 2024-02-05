#!/usr/bin/env python3
from censusreporter_api import *
from sqlalchemy import create_engine

def main():

    df_censo = get_dataframe(tables='B01001',column_names=True,level=1)
    engine = create_engine("mysql+mysqlconnector://root:root@mysql:3306/db")
    df_censo.to_sql('censo_2020', con=engine, if_exists='replace', index=False)
    print(df_censo)

if __name__ == "__main__":
    main()


