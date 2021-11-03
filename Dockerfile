FROM python:3.8.12-slim
WORKDIR /entity-recommendation-api

RUN apt-get update && \
    apt-get install -y gcc g++ make git

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/facebookresearch/fastText.git && \
    cd fastText && \
    pip install .

COPY . .

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]