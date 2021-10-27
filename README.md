# mrm-entity-api-demo
A prototype API for entity recommendation

## Installation

TBD

## Querying the API
1. Return All Entities
- Description: Return all entities
- Request URL: http://127.0.0.1:5000/entities/all
- Request Value: None.
- Return Values: all_entities


2. Return Suggestions of Entities for a User Input
- Description: Return a list of entities sorted by similarity score for a (required) user input.
- Request URL: http://127.0.0.1:5000/entities?input=
- Request Value: a user input
- Return Values: input, cadidates
- Example Request: 
  if user input was retrieved as "store",
  http://127.0.0.1:5000/entities?input=store
