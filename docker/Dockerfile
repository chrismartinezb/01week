FROM python:3.9.1

WORKDIR /app

COPY ../requirements.txt /tmp/

RUN apt-get install wget
RUN pip install -r /tmp/requirements.txt

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]