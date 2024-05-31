import pandas as pd
from sqlalchemy import create_engine

# Configura tus credenciales de la base de datos
host = 'mysql-eduardofarina-self-01.a.aivencloud.com:27648'
usuario = 'avnadmin'
contraseña = 'AVNS_EFCz8BR33pf0DTARSKL'
base_de_datos = 'self-properties'

# Crea una cadena de conexión SQLAlchemy
cadena_conexion = f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{base_de_datos}"

# Crea una conexión a la base de datos
engine = create_engine(cadena_conexion)

# Consulta SQL para obtener los datos (reemplaza con tu consulta)
nombre_tabla = 'mispropiedades'
consulta_sql = f"SELECT * FROM {nombre_tabla}"

# Carga los datos en un DataFrame de pandas
df = pd.read_sql(consulta_sql, engine)

# Ahora puedes trabajar con el DataFrame 'df'
print(df.head())
