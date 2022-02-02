# Number Match Solver
A Solver for [Number Match on Play Store](https://play.google.com/store/apps/details?id=com.easybrain.number.puzzle.game)

# Getting Started

## About the Project
This project is written in python 3, using FastAPI, and dockerized for easy access.

It uses BFS strategy to find the best possible solution. But BFS implementation requires optimization as it takes ages to solve more than 5 rows.

PRs are wellcomed.

## Pre-requisite
- Python 3.9
- Docker

## How to run

```
docker build -t number-match-solver:0.0.1 .
```

```
docker run -d -p 8080:8080 number-match-solver:0.0.1
```
