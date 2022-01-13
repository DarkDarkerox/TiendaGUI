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
    

main_query = f"""
    INSERT INTO tienda_alpha(Descripcion, Costo, Clave, Fecha) VALUES(?, ?, ?, ?)
    """
for elemento in datos:
    # Informacion del elemento\
    Clave = elemento.get('Clave')
    Descripcion = elemento.get('Descripcion del producto')
    Costo = elemento.get('Costo')
    Fecha = elemento.get('Fecha')
        
    with sql.connect('prueba2.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(main_query, (Descripcion, Costo, Clave, Fecha))
        conn.commit()
    