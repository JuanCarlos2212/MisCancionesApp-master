from src.miscancionesapp.modelo.cancion import Cancion
from src.miscancionesapp.modelo.interprete import Interprete
from src.miscancionesapp.modelo.album import Album, Medio
from src.miscancionesapp.modelo.declarative_base import Session, engine, Base
from src.miscancionesapp.logica.coleccion import Coleccion

if __name__ == '__main__':
    #Crea la BD
    Base.metadata.create_all(engine)

    #Abre la sesion
    session = Session()
    colecion=Coleccion()
    colecion.agregar_album("Titulo1" , 2020 , "nn" , Medio.CD )


