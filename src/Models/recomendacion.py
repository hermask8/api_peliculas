
class recomendacion:
    
    def __init__(self,movie,probabilidad):
        self.movie = movie
        self.probabilidad = probabilidad
        return
    
    def compareTo(self,recomendacion):
        if self.probabilidad > recomendacion.getProbabilidad():
            return -1
        elif self.probabilidad < recomendacion.getProbabilidad():
            return 1
        else:
            return 0
        
    
    def getProbabilidad(self):
        return self.probabilidad
