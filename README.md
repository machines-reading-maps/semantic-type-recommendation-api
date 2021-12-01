# Entity Recommendation API
Entity recommendation API is developed based on [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.

## Installation
1. Clone this repository
```
$ git clone https://github.com/machines-reading-maps/entity-recommendation-api.git
```

> Configure port number in [Dockerfile](https://github.com/machines-reading-maps/entity-recommendation-api/blob/05cafad85257b0e5fd6ec8e7f3257fdd1128f2f3/Dockerfile#L16-L17) and [app.py](https://github.com/machines-reading-maps/entity-recommendation-api/blob/c90619dddb3adb6cba1d410b0b3d6ccf7b84a387/app.py#L53) before installing docker image

2. Build docker image
```
$ cd entity-recommendation-api/
$ docker build -t entity-recommendation-api .
```

3. Download [word vectors](https://fasttext.cc/docs/en/pretrained-vectors.html) trained on Wikipedia using fastText  
```
$ cd data/
$ wget https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.en.zip
$ unzip wiki.en.zip
```

## Querying the API
- Return all entities
  - Description: Return all entities
  - Request URL: http://127.0.0.1:8000/entities/all
  - Request value: None.
  - Return values: all_entities


- Return entity search suggestions for a user input
  - Description: Return a list of entities sorted by similarity score for a (required) user input.
  - Request URL: http://127.0.0.1:8000/entities?input=
  - Request value: a user input
  - Return values: input, cadidates
  - Example request: 
    if user input was retrieved as "store",
    http://127.0.0.1:8000/entities?input=store
