FROM python:3.12-alpine

RUN apk --update add openssl wget unzip && rm -rf /var/cache/apk/*

RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py"]