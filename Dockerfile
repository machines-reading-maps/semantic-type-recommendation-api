FROM python:3.8.12-slim
WORKDIR /entity-recommendation-api
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .