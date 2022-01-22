import copy

class Board:
    def __init__(self, rows):
        self.rows = rows

    def get_row(self, row_idx):
        return self.rows[row_idx]

    def is_row_complete(self, p0):
        for i in range(9):
            if self.rows[p0[0]][i] != 0:
                return False
        self.rows.pop(p0[0])
        return True
    
    def is_complete(self):
        if self.rows == []:
            return True
        return False

    def get_diagonal_pos(self, p0, d=1):
        if self.rows[p0[0]][p0[1]] == 0:
            return None
        for i in range(1, len(self.rows)):
            x = (p0[0] + i)
            y = (p0[1] + d*i)
            if x < len(self.rows) and y < len(self.rows[0]) and x >= 0 and y >= 0 and self.rows[x][y] != 0:
                return (x, y)
        return None

    def get_right_pos(self, p0):
        if self.rows[p0[0]][p0[1]] == 0:
            return None
        for i in range(p0[1] + 1, 9):
            x = p0[0]
            y = i
            if self.rows[x][y] != 0:
                return (x, y)
        return None
    
    def get_down_pos(self, p0):
        if self.rows[p0[0]][p0[1]] == 0:
            return None
        for i in range(p0[0] + 1, len(self.rows)):
            x = i
            y = p0[1]
            if self.rows[x][y] != 0:
                return (x, y)
        return None

    def get_next_pos(self, p0):
        if self.rows[p0[0]][p0[1]] == 0:
            return None
        for i in range(p0[0], len(self.rows)):
            for j in range(9):
                x = i
                y = j
                if (x == p0[0] and y > p0[1]) or x > p0[0]:
                    if self.rows[x][y] != 0 and p0 != (x, y):
                        return (x, y)
        return None

    def find_all_possible_matches(self, p0):
        dir = self.get_diagonal_pos(p0)
        dil = self.get_diagonal_pos(p0, -1)
        ri = self.get_right_pos(p0)
        do = self.get_down_pos(p0)
        ne = self.get_next_pos(p0)

        res = []
        if dir:
            if self.match(p0, dir):
                res.append(dir)
                # res['diagonal_right'] = dir
        if dil:
            if self.match(p0, dil):
                res.append(dil)
                # res['diagonal_left'] = dil
        if ri:
            if self.match(p0, ri):
                res.append(ri)
                # res['right'] = ri
        if do:
            if self.match(p0, do):
                res.append(do)
                # res['down'] = do
        if not ri and ne:
            if self.match(p0, ne):
                res.append(ne)
                # res['next'] = ne

        return res

    def match(self, p0, p1):
        if self.rows[p0[0]][p0[1]] == self.rows[p1[0]][p1[1]]:
            # self.rows[p0[0]][p0[1]], self.rows[p1[0]][p1[1]] = 0, 0
            return True
        if self.rows[p0[0]][p0[1]] + self.rows[p1[0]][p1[1]] == 10:
            # self.rows[p0[0]][p0[1]], self.rows[p1[0]][p1[1]] = 0, 0
            return True
        return False
    
    def mark_as_match(self, p0, p1):
        self.rows[p0[0]][p0[1]], self.rows[p1[0]][p1[1]] = 0, 0

    def clone(self):
        return copy.deepcopy(self)