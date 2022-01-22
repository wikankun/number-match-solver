class Traversal:

    def is_done(self):
        raise NotImplementedError("error: needs an implementation of is_done")

    def cur_node(self):
        raise NotImplementedError("error: needs an implementation of cur_node")

    def iterate(self):
        raise NotImplementedError("error: need an implementation of iterate")