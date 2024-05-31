# import pandas as pd
# from sqlalchemy import create_engine

# # Configura los detalles de tu base de datos Aiven
# user = 'avnadmin'
# password = 'AVNS_EFCz8BR33pf0DTARSKL'
# host = 'mysql-eduardofarina-self-01.a.aivencloud.com'
# port = 27648  # Puerto típico de MySQL
# database = 'self-properties'

# # Crear la cadena de conexión
# connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

# # Crear el motor de conexión
# engine = create_engine(connection_string)

# # Supongamos que tienes un DataFrame llamado df que quieres subir
# df = pd.DataFrame({
#     'columna1': [1, 2, 3],
#     'columna2': ['a', 'b', 'c']
# })

# # Sube el DataFrame a la base de datos
# tabla_destino = 'nombre_de_tu_tabla'
# df.to_sql(name=tabla_destino, con=engine, if_exists='replace', index=False)

# print(f"Datos subidos correctamente a la tabla '{tabla_destino}' en la base de datos '{database}'.")

import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configura los detalles de tu base de datos Aiven
user = 'avnadmin'
password = 'AVNS_EFCz8BR33pf0DTARSKL'
host = 'mysql-eduardofarina-self-01.a.aivencloud.com'
port = 27648  # Puerto típico de MySQL
database = 'self-properties'

# Crear conexión a la base de datos
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    if connection.is_connected():
        print("Conectado a la base de datos")

        cursor = connection.cursor()

        # Crear el DataFrame
        df = pd.DataFrame({
            'columna1': [1, 2, 3],
            'columna2': ['a', 'b', 'c']
        })

        # Crear una tabla si no existe
        tabla_destino = 'nombre_de_tu_tabla'
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {tabla_destino} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            columna1 INT,
            columna2 VARCHAR(255)
        )
        """)

        # Insertar datos del DataFrame en la tabla
        for index, row in df.iterrows():
            cursor.execute(f"""
            INSERT INTO {tabla_destino} (columna1, columna2)
            VALUES ({row['columna1']}, '{row['columna2']}')
            """)

        connection.commit()
        print(f"Datos subidos correctamente a la tabla '{tabla_destino}' en la base de datos '{database}'.")

except Error as e:
    print("Error al conectar a la base de datos", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada")
