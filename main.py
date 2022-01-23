from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from solver.board import *
from solver.solver import *

class Numbers(BaseModel):
    numbers: List[int]


app = FastAPI()


@app.get("/")
def read_root():
    return "pong"


@app.post("/solve")
def read_item(numbers: List[List[int]]):
    board = Board(numbers)
    return solve(board)
