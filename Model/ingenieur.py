from .walker import Walker
import random

class Ingenieur(Walker):
    def __init__(self, actualPosition, destination):
        super().__init__(actualPosition, destination)
        self.position_reference = actualPosition
        self.nextPosition = self.actualPosition
        self.name = "citizen_engeneer"
        self.old_position = None
        self.nb_deplacement_max = 30

    def reset_position(self, position):
        self.nextPosition = position
        self.actualPosition = position
        self.nombreDeplacement = 0

    def find_new_destination(self, monde):
        self.set_nbdeplacement()
        if self.nombreDeplacement == 0:
            self.actualPosition = self.nextPosition

            matrix = [(-1,0),(1,0),(0,-1),(0,1)]
            valid_matrix = []
            for coord in matrix:
                new_grid = (self.actualPosition[0]+coord[0], self.actualPosition[1]+coord[1])
                if new_grid != self.old_position and new_grid[0] >= 0 and new_grid[1] >= 0 and \
                   new_grid[0] < len(monde.board) and new_grid[1] < len(monde.board[new_grid[0]]) and \
                   monde.board[new_grid[0]][new_grid[1]]["building"].name[0:5] == "route" or \
                   monde.board[new_grid[0]][new_grid[1]]["building"].name == "engeneer" and \
                   monde.board[new_grid[0]][new_grid[1]]["building"].position_reference == self.position_reference:
                    valid_matrix.append(coord)
            
            self.old_position = self.actualPosition
            if len(valid_matrix) > 0:
                new_dest = valid_matrix[random.randint(0,len(valid_matrix)-1)]
                new_dest = (self.actualPosition[0]+new_dest[0], self.actualPosition[1]+new_dest[1])
            else:
                new_dest = self.old_position

            self.nextPosition = new_dest

    def heal_around(self, monde):
        if self.nombreDeplacement == 0:
            matrix = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)]
            for coord in matrix:
                new_grid = (self.actualPosition[0]+coord[0], self.actualPosition[1]+coord[1])
                if new_grid[0] >= 0 and new_grid[1] >= 0 and \
                   new_grid[0] < len(monde.board) and new_grid[1] < len(monde.board[new_grid[0]]) and \
                   monde.board[new_grid[0]][new_grid[1]]["building"].name == "tente":
                    monde.board[new_grid[0]][new_grid[1]]["building"].reset_collapsing_state()