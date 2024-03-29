# Week one workbook


─ docker run -it \
  -e POSTGRES_USER='root' \
  -e POSTGRES_PASSWORD='root' \
  -e POSTGRES_DB='ny_taxi' \
  -v "$(pwd)"/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5433:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13


─ docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD='root' \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4


URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5433 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL}

docker run -it \
  --network=docker_pg-network \
  taxi_ingest:v001 \
  --user=root \
  --password=root \
  --host=pgdatabase \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL}

export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/ny-taxi.json

docker run -it \
  --network=docker_pg-network \
  taxi_ingest:v001 \
  --user=root \
  --password=root \
  --host=pgdatabase \git
  --port=5432 \
  --db=ny_taxi \
  --table_name=look_up_zone \
  --url=https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv