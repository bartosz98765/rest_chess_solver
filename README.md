# REST CHESS SOLVER
Very simple REST app helping play chess.

Written with Python 3.8

## Installation
```
Install with pip:
$ pip install -r requirements.txt
```

## Run flask for develop
```
$ python3 solver/rest_app.py
```

## Run Docker
In repository you have files: Dockerfile and docker-compose.yml.

Build and run server with app:

`$ docker-compose up -d`

Stop sever:

`$ docker-compose down`

##API url's
####Show list of available moves for chess figures. Choose from: king, queen, rook, bishop, knight, pawn.

[GET] `/api/v1/{chess-figure}/{current-field}`

e.g. `curl http://localhost:5000/api/v1/king/d8`

{"availableMoves":["C7","C8","D7","E7","E8"],"currentField":"D8","error":null,"figure":"king"}


####To validate move:

[GET] `/api/v1/{chess-figure}/{current-field}/{dest-field}`

e.g. `curl http://localhost:5000/api/v1/king/d8/d9`

{"currentField":"D8","destField":"D9","error":"Field does not exist.","figure":"king","move":null}


##Test
For test run `pytest` from `tests` directory
