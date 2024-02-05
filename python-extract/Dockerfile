# NOTE name need to be Dockerfile
FROM python:3.9
FROM google/cloud-sdk:latest

COPY ./src /src
WORKDIR /src

RUN pip install mysql-connector-python
RUN pip install requests
RUN pip install sqlalchemy
RUN pip install pandas
RUN pip install google-cloud-bigquery
RUN pip install openpyxl
RUN chmod +x /src/config/set_conf_gcp.sh
RUN /src/config/set_conf_gcp.sh

#COPY connectors.py ./
#COPY censusreporter_api.py ./
#COPY Utils.py ./
#COPY ./data /data
#COPY main.py ./