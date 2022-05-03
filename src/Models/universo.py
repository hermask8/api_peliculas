class universo:

    cantidadRegistros= 0.00
    bagOfDirectors = {}
    bagOfActors = {}
    bagOfGenres = {}
    cantidadGenres = 0.00
    bagOfKeyWords = {}
    cantidadKeyWords = 0.00
    bagOfLanguages = {}
    bagOfImdbScore = {}

    def __init__(self,cantidadGenres,bagOfGenres):
        self.cantidadGenres = cantidadGenres
        self.bagOfGenres = bagOfGenres
        return

    def agregarDirector(self,director):
        if director in self.bagOfDirectors:
            self.bagOfDirectors[director] = self.bagOfDirector[director]+1
        else:
            self.bagOfDirectors[director] = 1.00

        self.cantidadRegistros= self.cantidadRegistros + 1
        return
    
    def agregarActors(self,actors):
        if actors in self.bagOfActors:
            self.bagOfActors[actors] = self.bagOfActors[actors]+1
        else:
            self.bagOfDirectors[actors] = 1.00
        return


    def agregarGeneros(self,generosJuntos):
        generos = generosJuntos.split("|")
        for genero in generos:
            if genero in self.bagOfGenres:
                self.bagOfGenres[genero] = self.bagOfGenres[genero] + 1
            else:
                self.bagOfGenres[genero] = 1.00
            self.cantidadGenres = self.cantidadGenres +1  
        return
    









