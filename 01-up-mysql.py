import pandas as pd
from sqlalchemy import create_engine

# Configura tus credenciales de la base de datos en Aiven Cloud
host = 'mysql-eduardofarina-self-01.a.aivencloud.com:27648'
usuario = 'avnadmin'
contraseña = 'AVNS_EFCz8BR33pf0DTARSKL'
base_de_datos = 'self-properties'

# Crea una cadena de conexión SQLAlchemy
cadena_conexion = f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{base_de_datos}"

# Crea una conexión a la base de datos
engine = create_engine(cadena_conexion)

# Tu DataFrame de pandas (reemplaza con tus datos)
data = {
    'columna1': [1, 2, 3, 5, 10, 67],
    'columna2': ['A', 'B', 'C', 'D', 'E', 'F']
}
df = pd.DataFrame(data)


# Nombre de la tabla en la base de datos
nombre_tabla = 'mispropiedades'

# Sube el DataFrame a la base de datos
df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)

print(f"DataFrame subido exitosamente a la tabla '{nombre_tabla}' en la base de datos.")

# ¡Listo! Ahora los datos están en tu base de datos en Aiven Cloud.


