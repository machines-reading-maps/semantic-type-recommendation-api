# Entity Recommendation API
Entity recommendation API is developed based on [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.

## Installation
1. Clone this repository
```
$ git clone https://github.com/machines-reading-maps/entity-recommendation-api.git
```

> Configure port number in [Dockerfile](https://github.com/machines-reading-maps/entity-recommendation-api/blob/05cafad85257b0e5fd6ec8e7f3257fdd1128f2f3/Dockerfile#L16-L17) before installing docker image

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
### 1. Return All Entities
- Description: Return all entities
- Request URL: http://127.0.0.1:8000/entities/all
- Request Value: None.
- Return Values: all_entities


### 2. Return Entity Search Suggestions for a User Input
- Description: Return a list of entities sorted by similarity score for a (required) user input.
- Request URL: http://127.0.0.1:8000/entities?input=
- Request Value: a user input
- Return Values: input, cadidates
- Example Request: 
  if user input was retrieved as "store",
  http://127.0.0.1:8000/entities?input=store
