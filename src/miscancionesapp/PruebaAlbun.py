from src.miscancionesapp.modelo.cancion import Cancion
from src.miscancionesapp.modelo.interprete import Interprete
from src.miscancionesapp.modelo.album import Medio, Album
from src.miscancionesapp.modelo.declarative_base import Session, engine, Base
from src.miscancionesapp.logica.coleccion import Coleccion

if __name__ == '__main__':
    #Crea la BD
    Base.metadata.create_all(engine)

    #Abre la sesion
    session = Session()
    colecion=Coleccion()
    if colecion.agregar_album("La incondicional" , 1990 , "Son baladas" , Medio.CD ):
        print("Se añadio  on exito")
    else:
        print ( "Ya se encuentra el album" )

    if colecion.agregar_cancion("Amor",2, 30, "Prisioneros"):
        print("La cancion se añadio con exito")
    else:
        print("Ya se encuentra la cancion")