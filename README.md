# Flask API/Microservice kind of thing

Experimenting with building a simple API with few endpoints doing some data manipulation using Flask framework

Below are docs mostly for me, so I don't forget.

### Running this with reloading
flask --app main.py --debug run

### Examples of calling endpoints
How to call various endpoints and expected result.

#### Root endpoint

`curl http://localhost:8080/`

returns {
  "message": "Hello, World!"
}


#### Endpoint /hello/{name}/
`curl http://localhost:8080/hello/jakub/`

returns {
  "message": "Hello there, Jakub!"
}

#### Endpoint /numbers/
`curl -H 'Content-Type: application/json' -X POST -d '[1, 2, 3]' http://localhost:5000/numbers/`

returns {
  "average": 2.0,
  "max": 3,
  "min": 1,
  "sum": 6
}

#### Endpoint /dict2list/
`curl -H 'Content-Type: application/json' -X POST -d '{"fav_food": "pizza", "fav_drink": "coca-cola", "fav_chips": "Pringles BBQ"}' http://localhost:5000/dict2list/`

returns {
  "result": [
    "pizza",
    "coca-cola",
    "Pringles BBQ"
  ]
}

#### Endpoint /storytime/
`curl -H 'Content-Type: application/json' -X POST -d '{"name": "Jakub", "lastname": "Stastka", "age": 34, "favourite_animals": ["dog", "opposum", "lizard"]}' http://localhost:5000/numbers/`

returns {
  "storytime": "Jakub Stastka was born around 1988, and has 3 favourite animals: dog, opposum, lizard."
}
