from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from solver.board import *

class Numbers(BaseModel):
    numbers: List[int]


app = FastAPI()


@app.get("/")
def read_root():
    return {}


@app.post("/solve")
def read_item(numbers: List[List[int]]):
    board = Board(numbers)
    res = []
    for i in range(len(board.rows)):
        for j in range(len(board.rows[0])):
            res.append(board.find_all_possible_matches((i, j)))
    return {'result': res, 'board': board.rows}
