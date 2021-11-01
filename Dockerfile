FROM python:3.8.12-slim
WORKDIR /entity-recommendation-api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .