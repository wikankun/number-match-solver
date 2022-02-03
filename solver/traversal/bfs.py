class BFS():
    def __init__(self, start_node):
        self.visited = set()
        self.visited.add(start_node.get_hash())

        self.bfs_queue = list()
        self.bfs_queue.append(start_node)

    def is_done(self):
        return len(self.bfs_queue) == 0

    def cur_node(self):
        return self.bfs_queue[0]

    def iterate(self):
        node = self.bfs_queue.pop(0)

        for neighbor in node.get_neighbors():
            neighborHash = neighbor.get_hash()
            if neighborHash not in self.visited:
                self.bfs_queue.append(neighbor)
                self.visited.add(neighborHash)