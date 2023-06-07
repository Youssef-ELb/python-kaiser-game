from Model.building import Building
import random

class Tente(Building):
    def __init__(self, name, can_be_erase, can_constructible_over, can_be_walk_through, square_size):
        super().__init__(name, can_be_erase, can_constructible_over, can_be_walk_through, square_size)
        self.collapsing_state = random.randint(25000, 40000)
        self.should_refresh = False

    def reset_collapsing_state(self):
        if self.collapsing_state > 0:
            self.collapsing_state = random.randint(25000, 40000)
            self.should_refresh = True
    
    def reduce_collapsing_state(self):
        if self.collapsing_state > 0:
            self.collapsing_state = self.collapsing_state - random.randint(3,10)
            if self.collapsing_state <= 0:
                self.collapsing_state = 0
                self.should_refresh = True