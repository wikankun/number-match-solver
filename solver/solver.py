from .bfs import BFS


class Node:
    def get_hash(self):
        raise NotImplementedError("error: need an implementation for get_hash")

    def get_neighbors(self):
        raise NotImplementedError("error: need an implementation for get_hash")


class GraphNode(Node):
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
                    if self.board.is_row_complete(p1):
                        continue

                    new_board = self.board.clone()
                    new_board.mark_as_match(p0, p1)
                    neighbor.append(GraphNode(new_board, (p0, p1), self))
            return neighbor

    def get_hash(self):
        rows = self.board.rows
        return ";".join([str(row) for row in rows])

    def get_board(self):
        return self.board

    def get_moves_to_node(self):
        moves = []
        if self.prev_node is not None:
            moves.extend(self.prev_node.get_moves_to_node())
        if self.prev_move is not None:
            moves.append([self.prev_move])
        return moves


def solver(board):
    startNode = GraphNode(board, None, None)

    traversal = BFS(startNode)
    while not traversal.is_done():
        current_node = traversal.cur_node()
        is_solved = current_node.get_board().is_complete()
        if is_solved:
            return {
                "isSolvable": True,
                "moves": current_node.get_moves_to_node()
            }
        traversal.iterate()

    return {
        "isSolvable": False,
        "moves": current_node.get_moves_to_node()
    }