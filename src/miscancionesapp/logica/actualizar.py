from src.miscancionesapp.modelo.cancion import Cancion
from src.miscancionesapp.modelo.interprete import Interprete
from src.miscancionesapp.modelo.album import Album, Medio
from src.miscancionesapp.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__' :
  session = Session ( )
  cancion = session.query ( Cancion ).get ( 2 )
  interprete = session.query(Interprete).get(4)

  cancion.minutos = 5
  cancion.segundos = 30
  cancion.compositor = "Pedro Pérez"
  cancion.interpretes.append(interprete)
  session.add(cancion)
  session.commit()
  session.close()
