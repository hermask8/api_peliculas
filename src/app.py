from flask import Flask
import json
from config import config
from Models.pelicula import pelicula
from Models.recomendacion import recomendacion
from Models.universo import universo
from math import log,exp

app=Flask(__name__)

@app.route('/')
def index():
    return "LKAsjdlaksjdlkasd"


def CalcularProbabilidad(peli,cardDir, cardAct,cardKey,cardGen,cardLang,cardScore,comunes,positivo,negativo):

    probabilidad = 0.00
    ProbLogLike = 0.00
    ProbLogDislike = 0.00
    cantApariciones = 0.00

   

    #Calculamos la variable apriori
    ProbLogLike =+ log((positivo.cantidadRegistros+1)/(positivo.cantidadRegistros+negativo.cantidadRegistros+2))
    ProbLogDislike =+ log((negativo.cantidadRegistros +1)/(positivo.cantidadRegistros+negativo.cantidadRegistros +2))

    #print("AprioriLike= " + str(ProbLogLike))
    #print("AprioriDis= " + str(ProbLogDislike))

    
    """
     for item in positivo.bagOfGenres:
        print("positivo: " + str(item))
    
    for item in negativo.bagOfGenres:
        print("negativo: " + str(item))

    #Calculamos probabilidad de directores.
    if peli.getDirector() in positivo.BagOfDirectors.keys():
        cantApariciones = positivo.bagOfDirectors.get(peli.getDirector())
    ProbLogLike =+ log((cantApariciones+1)/(positivo.cantidadRegistros+cardDir))
    cantApariciones = 0.00

    if peli.getDirector() in negativo.BagOfDirectors.keys():
        cantApariciones = negativo.bagOfDirectors.get(peli.getDirector())

    ProbLogDislike =+ log((cantApariciones+1)/(negativo.cantidadRegistros+cardDir))
    cantApariciones = 0.00
    """
    """
    #calculamos la probabilidad de los actores.
    if peli.getActor1() in positivo.BagOfActors:
        cantApariciones = positivo.BagOfActors[peli.getActor1()]
    
    ProbLogLike =+ log((cantApariciones+1)/((positivo.cantidadRegistros*3)+cardAct))
    cantApariciones = 0.00

    if peli.getActor2() in positivo.BagOfActors:
        cantApariciones = positivo.BagOfActors[peli.getActor2()]
    
    ProbLogLike =+ log((cantApariciones+1)/((positivo.cantidadRegistros*3)+cardAct))
    cantApariciones = 0.00


    if peli.getActor3() in positivo.BagOfActors:
        cantApariciones = positivo.BagOfActors[peli.getActor3()]
    
    ProbLogLike =+ log((cantApariciones+1)/((positivo.cantidadRegistros*3)+cardAct))
    cantApariciones = 0.00

    #Dislike
    if peli.getActor1() in negativo.BagOfActors:
        cantApariciones = negativo.BagOfActors[peli.getActor1()]
    
    ProbLogDislike =+ log((cantApariciones+1)/((negativo.cantidadRegistros*3)+cardAct))
    cantApariciones = 0.00

    if peli.getActor2() in negativo.BagOfActors:
        cantApariciones = negativo.BagOfActors[peli.getActor2()]
    
    ProbLogDislike =+ log((cantApariciones+1)/((negativo.cantidadRegistros*3)+cardAct))
    cantApariciones = 0.00

    if peli.getActor3() in negativo.BagOfActors:
        cantApariciones = negativo.BagOfActors[peli.getActor3()]
    
    ProbLogDislike =+ log((cantApariciones+1)/((negativo.cantidadRegistros*3)+cardAct))
    cantApariciones = 0.00
    """
    #Calcular la probabilidad de los generos
    
    generosPeli = peli.getGenero().split("|")
    print("Asi empieza el like: " + str(ProbLogLike))
    for gener in generosPeli:
        cantApariciones = 0.00
        if gener in positivo.bagOfGenres.keys():
            cantApariciones = positivo.bagOfGenres.get(gener)
            #print("apariciones: " +gener + " "+str(cantApariciones))
        ProbLogLike = ProbLogLike + log((cantApariciones+1)/(positivo.cantidadGenres + cardGen))
        #print("Con " + gener + "el like es: " + str(ProbLogLike) )
        cantApariciones = 0.00
        if gener in negativo.bagOfGenres.keys():
            cantApariciones = negativo.bagOfGenres.get(gener)
           # print("apariciones: " +gener + " "+str(cantApariciones))
        ProbLogDislike = ProbLogDislike + log((cantApariciones+1)/(negativo.cantidadGenres + cardGen))
        #print("Con " + gener + "el dislike es: " + str(ProbLogLike) )

    #print("Asi termina el like: " + str(ProbLogLike))
    #print("Asi termina el dislike: " + str(ProbLogDislike))
    probabilidad = (exp(ProbLogLike)/(exp(ProbLogLike)+exp(ProbLogDislike)))*100
    #print("La probabilidad es: " + str(probabilidad))
    

    return probabilidad


@app.route('/peliculas', methods = ['GET'])
def peliculas():
    try:
        peli = pelicula("Oso el Osos","edwin","ted","oso","juguete","risa|comedia|romance","numeros","espaniol","cien")
        peli2 = pelicula("Oso el Osos","edwin","ted","oso","juguete","accion|terror|aventura","numeros","espaniol","cien")

        generosRecomen = {'risa': 20.00, 'comedia': 100.00,'romance':30.00}
        generosNoRecomen = {'accion': 1.00, 'terror': 1.00,'aventura':1.00}


        recomen = recomendacion(peli,15.6)
        recomen2 = recomendacion(peli,14.3)
        positivo = universo(150.00,generosRecomen)
        negativo = universo(3.00,generosNoRecomen)


        prob = CalcularProbabilidad(peli2,0,0,0,6,0,0,0,positivo,negativo)
        
        pythonDictionary = {'Proobabilidad':prob, 'Peli Genero':peli2.getGenero()}
        dictionaryToJson = json.dumps(pythonDictionary)
        return dictionaryToJson
    except Exception as ex:
        return 'seasde'

if __name__== '__main__':
    app.config.from_object(config['development'])
    app.run()

