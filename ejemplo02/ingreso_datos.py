from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
datos_jugadores = open ('data/datos_jugadores.txt','r', encoding="utf8")
datos_clubs = open ('data/datos_clubs.txt','r', encoding="utf8")
#for f in f:

#session.query(Club).filter_by(nombre="LDU").one()
contenido_j=datos_jugadores.readlines()
contenido_c=datos_clubs.readlines()
#print(contenido

#Datos Clubs
c=''
for i in range (0,len(contenido_c),1): # split por ;
   d=contenido_c[i].split(";")
   p = Club(nombre=d[0], deporte=d[1], fundacion=d[2])
   session.add(p)

d=''
#Datos de Jugadores
for i in range (0,len(contenido_j),1): # split por ;
   d=contenido_j[i].split(";")

   p = Jugador(nombre=d[3], dorsal=d[2], posicion=d[1])
   session.add(p)

session.commit()

