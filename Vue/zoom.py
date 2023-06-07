
class Zoom:

    def __init__(self):
        self.init_level_zoom = 70
        self.level_zoom = self.init_level_zoom
        self.multiplier = self.level_zoom/100
        self.should_scale = False

    def update(self, diff):
        self.level_zoom += diff
        self.multiplier = self.level_zoom/100
        self.should_scale = True
