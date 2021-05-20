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

#Lectura del archivos
datos_jugadores = open ('data/datos_jugadores.txt','r', encoding="utf8")
datos_clubs = open ('data/datos_clubs.txt','r', encoding="utf8")

contenido_j=datos_jugadores.readlines()
contenido_c=datos_clubs.readlines()

#Datos Clubs
c=''
for i in range (0,len(contenido_c),1): 
   d=contenido_c[i].split(";") # split por ;
   p = Club(nombre=d[0], deporte=d[1], fundacion=d[2])
   session.add(p)

#Consulta para obtener todos los datos de los clubs 
clubs = session.query(Club).all() 
d=''
#Datos de Jugadores
for i in range (0,len(contenido_j),1): # split por ;
   d=contenido_j[i].split(";")
   #Ciclo para evaluar el nombre del club a los que pertenecen los jiugadores
   #para asignarles el id del club al que pertenecen
   for club in clubs:
      if d[0] == club.nombre:
         id_club = club.id

   p = Jugador(nombre=d[3], dorsal=d[2], posicion=d[1],club_id=id_club)
   session.add(p)
# confirmacion de transacciones
session.commit()

