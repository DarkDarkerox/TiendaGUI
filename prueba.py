import sqlite3 as sql
import openpyxl


excel_document = openpyxl.load_workbook('base2.xlsx')

sheet = excel_document.get_sheet_by_name('hoja1')


# En la lista 'datos' tenemos diccionarios que contiene informacion
# del elemento, listos para hacer el Query.
datos = []

for i in range(2, 1114):
    # Inicializamos el diccionario temporal
    dict_test = {'Descripcion del producto' : None, 'Costo' : None,
            'Clave' : None, 'Fecha' : None}
    for j in range(1, 13):
        temp_value = sheet.cell(row = i, column = j).value
        if j == 1:
            dict_test['Clave'] = temp_value
        elif j == 2:
            dict_test['Descripcion del producto'] = temp_value
        elif j == 6:
            dict_test['Costo'] = temp_value    
        elif j == 4:
            dict_test['Fecha'] = temp_value
    datos.append(dict_test)

query = """ 
INSERT INTO tienda_alpha(Descripcion, Costo, Clave, Fecha) VALUES(?, ?, ?, ?)
"""

# Vamos a cargar nuestra base de datos.
# Ademas vamos a agregar un articulo
# with sql.connect('prueba2.db') as conn:
#     cursor = conn.cursor()
#     result = cursor.execute(query, ('JAJA', '230', '202022', '20/20/20'))
#     conn.commit()

# Para eliminar ciertos datos de la DB
with sql.connect('prueba2.db') as conn:
    cursor = conn.cursor()
    result = cursor.execute("DELETE FROM tienda_alpha WHERE Descripcion ='JAJA'", ())
    conn.commit()
      
# Vamos a leer el primer articulo que tengamos en la base de datos
with sql.connect('prueba2.db') as conn:
    cursor = conn.cursor()
    result = cursor.execute('SELECT * FROM tienda_alpha', ())
    conn.commit()    

for x in result:
    print(x)
