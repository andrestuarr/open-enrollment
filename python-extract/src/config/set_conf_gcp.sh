#!/bin/bash
export PATH_PROJECT=/src/
export PROJECT_ID=claroinsurance
export FEC_PROCESO=`date +"%Y-%m-%d"`
export DATE_TODAY=`date "+%Y%m%d"`
export GOOGLE_APPLICATION_CREDENTIALS="/src/config/claroinsurance-34db9caf27f6.json"
gcloud auth activate-service-account claro-insurance@${PROJECT_ID}.iam.gserviceaccount.com --key-file ${GOOGLE_APPLICATION_CREDENTIALS}
gcloud config set project ${PROJECT_ID}