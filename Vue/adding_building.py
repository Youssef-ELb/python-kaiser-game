import pygame
import math

from .selectionneur_zone import SelectionneurZone

class Adding_Building(SelectionneurZone):
    def __init__(self, surface, path):
        SelectionneurZone.__init__(self, surface)
        self.path = path
        self.can_thinking = False

    def events(self, event):
        SelectionneurZone.events(self, event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: self.can_thinking = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.can_thinking:
            last_grid = self.grid_to_draw[len(self.grid_to_draw)-1]
            for grid in self.grid_to_draw:
                self.treat_event(grid, last_grid)
            
            self.is_progress = False

    def treat_event(self, grid, last_grid):
        if grid[0] >= 0 and grid[1] >= 0 and len(self.carriere.informations_tiles) > grid[0] and len(self.carriere.informations_tiles[grid[0]]) > grid[1] and \
           self.carriere.controleur.check_if_construction_possible_on_grid(grid) and grid != (20,39) and self.carriere.controleur.check_if_path_exist_from_spawn_walker(grid):
           stop_loop = False
           for num_lig in range(0, len(self.carriere.informations_tiles)):
            for num_col in range(0, len(self.carriere.informations_tiles[num_lig])):
                if stop_loop == False and self.carriere.informations_tiles[num_lig][num_col]["building"].name[0:5] == "route" and self.calcul_distance_to_grid(grid, (num_lig, num_col)) <= 2:
                    self.carriere.controleur.add_building_on_point(grid, self.carriere.dictionnaire_reverse_by_path[self.path])
                    self.carriere.controleur.walker_creation((20,39),grid)
                    stop_loop = True
                if stop_loop:
                    if last_grid == grid: self.is_progress = False
                    return
                    
            if last_grid == grid: self.is_progress = False