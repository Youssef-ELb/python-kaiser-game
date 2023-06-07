class Walker:
    nb_walker = 0

    def __init__(self,actualPosition,destination):
        self.ID = Walker.nb_walker+1
        Walker.nb_walker=self.ID
        self.actualPosition = actualPosition #comment récupérer la position actuelle d'un walker?
        self.nextPosition = None
        self.destination = destination #position généralement désignée par la construction d'une maison
        self.name = "citizen" #fichier sprite du walker
        self.chemin = None
        self.nombreDeplacement = 0
        self.nb_deplacement_max = 10

    def set_nbdeplacement(self):
        self.nombreDeplacement = (self.nombreDeplacement+1)%self.nb_deplacement_max

    def set_nextPosition(self):
        if self.chemin != None and self.chemin != False and len(self.chemin) > 1:
            self.nextPosition = self.chemin[1]