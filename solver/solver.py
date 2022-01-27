from .bfs import BFS


class GraphNode():
    def __init__(self, board, prev_move, prev_node):
        self.prev_node = prev_node
        self.board = board
        self.prev_move = prev_move

    def get_neighbors(self):
        neighbor = []
        for i in range(len(self.board.rows)):
            for j in range(len(self.board.rows[0])):
                p0 = (i, j)
                for p1 in self.board.find_all_possible_matches(p0):
                    new_board = self.board.clone()
                    new_board.mark_as_match(p0, p1)
                    neighbor.append(GraphNode(new_board, (p0, p1), self))
        return neighbor

    def get_hash(self):
        rows = self.board.rows
        return ",".join([str(row) for row in rows])

    def get_board(self):
        return self.board

    def get_moves_to_node(self):
        moves = []
        if self.prev_node is not None:
            moves.extend(self.prev_node.get_moves_to_node())
        if self.prev_move is not None:
            moves.append([self.prev_move])
        return moves


def solve(board):
    startNode = GraphNode(board, None, None)

    traversal = BFS(startNode)
    while not traversal.is_done():
        current_node = traversal.cur_node()
        is_solved = current_node.board.is_complete()
        if is_solved:
            return {
                "isSolvable": True,
                "moves": current_node.get_moves_to_node(),
                "board": current_node.board.rows
            }
        traversal.iterate()

    if current_node.get_moves_to_node() == [] and current_node.board.rows != []:
        temp_board = current_node.board.clone()
        temp_rows = []
        for row in temp_board.rows:
            temp_row = []
            for i in row:
                if i != 0:
                    temp_row.append(i)
            temp_rows.append(temp_row)
        temp_board.rows.extend(temp_rows)

        return solve(temp_board)

    return {
        "isSolvable": False,
        "moves": current_node.get_moves_to_node(),
        "board": current_node.board.rows
    }