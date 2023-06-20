FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
 python-is-python3 \
 curl \
 bash

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . ./

ENV PORT 8080

RUN curl -sSL https://sdk.cloud.google.com | bash

ENV PATH $PATH:/root/google-cloud-sdk/bin

RUN pip install --no-cache-dir -r requirements.txt

CMD exec uvicorn app.api:app --host 0.0.0.0 --port ${PORT} --workers 1
