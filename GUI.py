from tkinter import *
from tkinter import ttk

class main_window:
    """
    Representa la ventana principal de la GUI.
    
    Parametros
    ----------
    window objet: objeto de Tkinter.Tk()
    ----------
    """
    
    def __init__(self, window):

        self.wind = window
        
        # Creamos el Frame
        self.frame = Frame(self.wind)
        self.frame.grid(columnspan = 2, rowspan = 2)
        
        # Creamos el header de con el nombre de la tienda.
        self.message = Label(self.frame, text='Tiendita de don panchito')
        self.message.grid(column = 0, row = 0, sticky='WE', columnspan=2)
        self.message.config(font=('arial', 25))
        
        # Creamos los botones
            # Boton add_art
        self.boton_aniadir_articulo = Button(self.frame, text='Añadir articulo',
                                             command=lambda: self.nueva_ventana(tag=0))
        self.boton_aniadir_articulo.grid(column=0, row=1, sticky='WE')
        
            # Boton 'ver inventario'
        self.boton_ver_inventario = Button(self.frame, text='Ver inventario',
                                           command=lambda: self.nueva_ventana(tag=1))
        self.boton_ver_inventario.grid(column=0, row=2, sticky='WE')
        
            # Boton add_art_inv
        self.boton_aniadir_inventario = Button(self.frame, text='Añadir articulo al inventario',
                                               command=lambda: self.nueva_ventana(tag=2))
        self.boton_aniadir_inventario.grid(column=0, row=3, sticky='WE')
        
            # Boton quitar_art_inv
        self.boton_quitar_inventario = Button(self.frame, text='Quitar articulo del inventario',
                                              command=lambda: self.nueva_ventana(tag=3))
        self.boton_quitar_inventario.grid(column=0, row=4, sticky='WE')
        
            # Boton de expedir nota
        self.boton_expedir_nota = Button(self.frame, text='Expedir nota')
        self.boton_expedir_nota.grid(column=0, row=6, sticky='WE')

        # Aniadimos la box de informacion de articulos en caja.
        self.descripcion_caja = Text(self.frame, height=10, width=30, bg='white')
        self.descripcion_caja = Text(self.frame, height=10, width=30, bg='white')
        self.descripcion_caja.grid(column=1, row=1, rowspan=4, padx=10)
        
        # Aniadimos la box de informacion del precio.
        self.precio_acumulado = Text(self.frame, height=2.5, width=30, bg='white')
        self.precio_acumulado.grid(column=1, row=6, pady=10)
        
        # Boton de salida
        self.boton_de_salida = Button(self.frame, text='Salir',
                                      command= lambda: self.frame.quit())
        self.boton_de_salida.grid(column=1, row=7, padx=10)

        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
    def desplegar_informacion(self, item_, articulos_, label_):
        articulos_prueba = {'Huevo': {'Categoria': 'Comida', 'SKU': '112334', 'No. Piezas': 10}, 
        'Libreta': {'Categoria': 'Papeleria', 'SKU': '112324', 'No. Piezas': 12}, 
        'Plumas': {'Categoria': 'Cuidado Personal', 'SKU': '112355', 'No. Piezas': 100}}

        
        item = articulos_.get(item_)
        item_contenido = articulos_prueba.get(item)
                      
        texto = f"""
        Categoria: {item_contenido.get('Categoria')}
        SKU: {item_contenido.get('SKU')}
        No. Piezas: {item_contenido.get('No. Piezas')}
        """
        label_.config(text=texto, font=('Arial', 14) )
    
    def nueva_ventana(self, tag=None):
        """
        Esta función nos abre una nueva ventana,
        segun que etiqueta 'tag' tenga la ventana, le vamos
        a dar cierto estilo, dimension, etc.
        La convención para los tag es la siguiente:
        
        tag = 0 --> Añadir Articulo
        tag = 1 --> Inventario
        tag = 2 --> Añadir articulo a inventario
        tag = 3 --> Quitar articulo del inventario
        
        """
        # TopLevel es el objeto que sera utilizado
        # como una nueva venta
        nueva_ventana = Toplevel(self.frame)
        nueva_ventana.resizable(False, False)
             
        # Aqui vamos a personalizar la ventana en cuestion.
        if tag == 0:
            
            nombre = 'Añadir Articulo'
            nueva_ventana.title(nombre)
            nueva_ventana.geometry('300x300')
            
            #* Categoria
            lb = Label(nueva_ventana, text='Categoria')
            lb.grid(row=0, column=0)
                        
            lista_articulos =  ttk.Combobox(nueva_ventana,
                                            values = ['asd'])
            lista_articulos.grid(row = 0, column = 1)
            
            #* Lista de articulos
            lb = Label(nueva_ventana, text='Articulo')
            lb.grid(row=1, column=0)
                        
            lista_articulos =  ttk.Combobox(nueva_ventana,
                                            values = ['asd'])
            lista_articulos.grid(row = 1, column = 1)
            
            #* Selector de cantidad de elementos
            lb = Label(nueva_ventana, text='Cantidad')
            lb.grid(row=2, column=0)
            
            selector = ttk.Combobox(nueva_ventana,
                                    values = [x for x in range(1, 99)])
            selector.grid(row = 2, column = 1)
            
            #* Botones de aceptar y cancelar
            
            cancelar_boton = Button(nueva_ventana, text='CANCELAR',
                                   command= nueva_ventana.destroy)
            cancelar_boton.grid(row =3, column=1)
            
            aceptar_boton = Button(nueva_ventana, text='ACEPTAR',
                                   command= nueva_ventana.destroy)
            aceptar_boton.grid(row =3, column=0)
            
        elif tag == 1:
            # Caracteristicas de la ventana
            nombre = 'Inventario'
            nueva_ventana.title(nombre)
            nueva_ventana.geometry('600x400')
            
            #* TITULO INVENTARIO
            message_inventario = Label(nueva_ventana, text='Inventario de la tienda de don panchito')
            message_inventario.grid(row = 0, column = 0, columnspan = 2,
                                    sticky='we')
            message_inventario.config(font =('Arial', 20, 'italic'))
                        
            #* Selector de categoria de articulos
            lb = Label(nueva_ventana, text='Categoria')
            lb.grid(row=1, column=0, padx=5, pady=5, sticky='e')
            
            lista_articulos =  ttk.Combobox(nueva_ventana, values = [x for x in range(1,4)])
            lista_articulos.grid(row = 1, column = 1, sticky='w')
            lista_articulos.current(0)
            
            #* Lista de lista_articulos
            lista_de_articulos = ['Huevo', 'Libreta', 'Plumas']
        
            # Creamos su scrollbar
            scrollbar = Scrollbar(nueva_ventana, orient=VERTICAL)
            
            articulos = Listbox(nueva_ventana, yscrollcommand=scrollbar.set)
            articulos.insert(END, *lista_de_articulos)
            articulos.grid(row = 2, column = 0)
            articulos.selection_set( first = 0 )
            
            scrollbar.config(command=articulos.yview)
            scrollbar.grid(row=2, column=1, sticky='wns')

            # Frame donde vamos a desplegar la informacion
            informacion = Label(nueva_ventana)
            informacion.grid(row = 2, rowspan=3, column= 1, sticky='nw')
            
            boton = Button(nueva_ventana, text="picale", command=lambda: self.desplegar_informacion(articulos.curselection(), articulos, informacion))
            boton.grid(row = 4, column = 0, sticky='w', padx=10, pady=10)
            
        elif tag == 2:
            nombre = 'Añadir articulos a inventario'
            nueva_ventana.title(nombre)
            nueva_ventana.geometry('400x300')
        elif tag == 3:
            nombre = 'Eliminar articulos del inventario'
            nueva_ventana.title(nombre)
            nueva_ventana.geometry('400x300')   
            
        
window = Tk()
window.geometry('550x330')
window.title('Tiendita')
ventana = main_window(window)
window.resizable(False, False)
window.mainloop()