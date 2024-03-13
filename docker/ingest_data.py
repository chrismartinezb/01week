#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import argparse
from sqlalchemy import create_engine
import os
from tqdm import tqdm


def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    file_name = 'output.parquet'

    # Determine file extension and set the appropriate pandas read function
    file_ext = file_url.split('.')[-1].lower()
    if file_ext in ['parquet']:
        read_func = pd.read_parquet
        filename += '.parquet'
    elif file_ext in ['csv']:
        read_func = pd.read_csv
        filename += '.csv'
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

    print('Initialize data download from source')
    os.system(f'wget {file_url} -O {filename}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = read_func(filename)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_parquet(file_name)

    print('Schema created')
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    chunksize = int(len(df) / 100)  # For example, you might want to process 10% of rows at a time
    print('Moving parquet to database')
    with tqdm(total=len(df), desc="Rows processed") as pbar:
        for start in range(0, len(df), chunksize):
            end = min(start + chunksize, len(df))
            df.iloc[start:end].to_sql(name=table_name, con=engine, if_exists='append', index=True)
            pbar.update(end - start)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the parquet file')

    args = parser.parse_args()

    main(args)





