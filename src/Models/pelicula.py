
class pelicula:

    def __init__(self,titulo,director,actor1,actor2,actor3,genero,plotKeyWords,lenguaje,score):
        self.titulo = titulo
        self.director = director
        self.actor1 = actor1
        self.actor2 = actor2
        self.actor3 = actor3
        self.genero = genero
        self.plotKeyWords = plotKeyWords
        self.lenguaje = lenguaje
        self.score = score
        return
    
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self,titulo):
        self.titulo = titulo
        return

    def getDirector(self):
        return self.director
    
    def setDirector(self,director):
        self.director = director
        return

    def getActor1(self):
        return self.actor1
    
    def setActor1(self,actor1):
        self.actor1 = actor1
        return

    def getActor2(self):
        return self.actor2
    
    def setActor2(self,actor2):
        self.actor2 = actor2
        return
    
    def getActor3(self):
        return self.actor2
    
    def setActor3(self,actor3):
        self.actor3 = actor3
        return

    def getGenero(self):
        return self.genero
    
    def setGenero(self,genero):
        self.genero = genero
        return
    
    def getPlotKeyWords(self):
        return self.plotKeyWords
    
    def setPlotKeyWords(self,plotKeyWords):
        self.plotKeyWords = plotKeyWords
        return
    
    def getLenguaje(self):
        return self.lenguaje
    
    def setLenguaje(self,lenguaje):
        self.lenguaje = lenguaje
        return
    
    def getScore(self):
        return self.score
    
    def setScore(self,score):
        self.score = score
        return


    
    
    



