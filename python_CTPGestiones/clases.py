import calendar

import tkinter as tk
from tkinter import filedialog
import webbrowser
from patrondiseño import Singleton

class Acceso:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Acceso de entrada para docentes")

        # Creamos el cuadro de texto para ingresar la contraseña
        clave_label = tk.Label(self.root, text="Ingrese la clave de acceso:")
        clave_label.pack()

        self.clave_box = tk.Entry(self.root, show="*")
        self.clave_box.pack()

        # Creamos el cuadro de texto para ingresar la cédula del docente
        cedula_label = tk.Label(self.root, text="Ingrese la cédula del docente:")
        cedula_label.pack()

        self.cedula_box = tk.Entry(self.root)
        self.cedula_box.pack()
        self.nombreDocente = "Roxinny Jimenez Vega"

        # Creamos el botón para agregar los datos
        add_button = tk.Button(self.root, text="Agregar", command=self.agregar_datos)
        add_button.pack()

    # Función para agregar los datos
    def agregar_datos(self):
        clave_acceso = self.clave_box.get()
        if clave_acceso == "0922":
            cedula = self.cedula_box.get()
            if cedula == "112560081":
                print("Bienvenida al sistema Docente de Informática Educativa ")
                print("Datos del Docente:", self.nombreDocente)
                print("Acceso concedido")
                self.root.destroy()
                root2 = tk.Tk()
                root2.geometry("800x600")
                app = MyApplication(root2)
                s = Singleton.get_instance(root2)
                root2.mainloop()
            else:
                print("Cédula incorrecta. Intente de nuevo.")
        else:
            print("Clave de acceso incorrecta. Intente de nuevo.")

    def on_close(self, root2):
        root2.destroy()
class MyApplication:

    def __init__(self, root):
        self.root = root
        self.opcion = tk.StringVar()
        self.opcion.set("tarea")
        # Crear la barra de menú
        menubar = tk.Menu(self.root)

        # Crear la opción "Archivo" en la barra de menú
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=self)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_command(label="Guardar como...", command=self.guardar_archivo_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=root.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)

        # Crear la opción "Calendario" en la barra de menú
        calendario_menu = tk.Menu(menubar, tearoff=0)
        calendario_menu.add_command(label="Ver calendario", command=self.calendario)
        menubar.add_cascade(label="Calendario", menu=calendario_menu)

        # Menú Ver
        ver_menu = tk.Menu(menubar, tearoff=0)
        ver_menu.add_radiobutton(label="Tarea", variable=self.opcion, value="tarea", command=self.mostrar_tarea)
        ver_menu.add_radiobutton(label="Cuestionario", variable=self.opcion, value="cuestionario",
                                 command=self.mostrar_cuestionario)
        menubar.add_cascade(label="Ver Tareas asignadas", menu=ver_menu)

        self.root.config(menu=menubar)


        # Crear la opción "Consulta" en la barra de menú
        consulta_menu = tk.Menu(menubar, tearoff=0)
        consulta_menu.add_command(label="Buscar en Google", command=self.buscar_en_google)
        menubar.add_cascade(label="Consulta", menu=consulta_menu)

        self.tarea_1 = {
            'descripcion':
                '\n\nconsiste en realizar un análisis crítico de un artículo científico, lo que implica la lectura cuidadosa y detallada del texto \n'
                'para identificar sus fortalezas y debilidades, así como su relevancia y contribución a la disciplina en cuestión.\n'
                ' Se espera que el análisis se realice de manera objetiva y rigurosa,\n'
                ' severa en evidencia concreta y evitando prejuicios o suposiciones infundadas.\n\n',
            'fecha_entrega': '2023-05-01\n',
            'porcentaje': 20,
            '\objetivos':
                '\n\nDesarrollar habilidades de lectura crítica y síntesis, lo que implica la capacidad de analizar \n'
                'y evaluar la información de manera rigurosa y sistemática, así como de resumir y presentar los descubrimientos \n'
                'de manera clara y concisa. Estas habilidades son fundamentales en la investigación científica y en cualquier campo \n'
                'que requiera la evaluación crítica de la información y la toma de decisiones basada en evidencia.\n'
        }

        self.cuestionario = {
            'descripcion': '\n\n Consiste en resolver un cuestionario de 10 preguntas\n'
                           ' relacionadas con la programación orientada a objetos.\n \n'
                           'El cuestionario se enfoca en conceptos fundamentales\n'
                           ' como son la herencia, el polimorfismo, la encapsulación,\n'
                           'las clases, los objetos,los métodos, las instancias y \n'
                           'la sobrecarga de operadores..\n\n'

                           '1. ¿Qué es la programación orientada a objetos?\n\n'
                           '2. ¿Cuáles son los cuatro principios fundamentales\n'
                           ' de la programación orientada a objetos?\n\n'
                           '3. ¿Qué es la herencia en programación orientada a objetos?\n\n'
                           '4. ¿Qué es el polimorfismo en programación orientada a objetos?\n\n'
                           '5. ¿Qué es la encapsulación en programación orientada a objetos?\n\n'
                           '6. ¿Qué es una clase de programación orientada a objetos?\n\n'
                           '7. ¿Qué es un objeto en programación orientada a objetos?\n\n'
                           '8. ¿Qué es un método de programación orientada a objetos?\n\n'
                           '9. ¿Qué es una instancia de programación orientada a objetos?\n\n'
                           '10. ¿Qué es la sobrecarga de operadores en programación orientada a objetos?\n\n\n',

            'fecha_entrega': '2023-02-20\n',

            'porcentaje': '10 \n',

            'objetivos': '\n \nReconocer los conceptos fundamentales de la programación orientada a objetos,\n'
                         ' lo que implica la capacidad de identificar y comprender los conceptos básicos de \n'
                         'la programación orientada a objetos, así como de aplicar los en situaciones prácticas.\n '
                         'Esta habilidad es fundamental en el desarrollo de software y en cualquier campo \n'
                         'que requiera el uso de programación orientada a objetos..\n'
        }

        self.root.config(menu=menubar)
        self.root.title("Editor de Archivos y Busqueda Web")

        self.texto_predefinido = "Plan Nacional Informática Educativa\nMSc. Jhovanny Loaiza Porras (director)\nColegio Técnico Profesional de Quepos \n\n\nDocente:\n\nFECHA: \nASUNTO:  Elaboración de proyectos Educativos\n………………………………………………………………………………………………………………….. \n\nDescripción:\n\nEntrega:\n\n\nValor:\n\nObjetivos: "
        self.texto = tk.Text(self.root)
        self.texto.pack(fill=tk.BOTH, expand=True)
        self.texto.insert(tk.END, self.texto_predefinido)
        self.texto.config(fg="black", bg="white", font=("Arial", 12))

        self.encabezado = tk.Label(self.root,
                                   text="Saludos cordiales, la siguiente plataforma es para la elaboración de machotes de proyectos educativos para los estudiantes, pueden hacer uso del mismo, generando su propia creatividad.")
        self.encabezado.pack()

    def mostrar_tarea(self):

        if self.opcion.get() == "tarea":
            tarea = self.tarea_1

        ventana = tk.Toplevel(self.root)
        ventana.title("Detalles de la Tarea")
        descripcion_label = tk.Label(ventana, text="Descripción: " + tarea['descripcion'])
        descripcion_label.pack()
        fecha_label = tk.Label(ventana, text="Fecha de entrega: " + tarea['fecha_entrega'])
        fecha_label.pack()
        porcentaje_label = tk.Label(ventana, text="Porcentaje: " + str(tarea['porcentaje']) + "%")
        porcentaje_label.pack()

    def mostrar_cuestionario(self):
        if self.opcion.get() == "Cuestionario":
            tarea = self.cuestionario
        else:
            tarea = self.cuestionario

        ventana = tk.Toplevel(self.root)
        ventana.title("Detalles del cuestionario")
        descripcion_label = tk.Label(ventana, text="Descripción: " + tarea['descripcion'])
        descripcion_label.pack()
        fecha_label = tk.Label(ventana, text="Fecha de entrega: " + tarea['fecha_entrega'])
        fecha_label.pack()
        porcentaje_label = tk.Label(ventana, text="Porcentaje: " + str(tarea['porcentaje']) + "%")
        porcentaje_label.pack()
        objetivos_label = tk.Label(ventana, text="Objetivos: " + tarea['objetivos'])
        objetivos_label.pack()
    def abrir_archivo(self):
        archivo = filedialog.askopenfile(defaultextension=".txt",
                                         filetypes=[("Archivos de texto", ".txt"), ("Todos los archivos", ".*")])
        if archivo is not None:
            self.texto.delete("1.0", tk.END)
            self.texto.insert(tk.END, archivo.read())
    def guardar_archivo(self):
        archivo_guardado = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                                    filetypes=[("Archivos de texto", ".txt"),
                                                               ("Todos los archivos", ".*")])
        if archivo_guardado is not None:
            archivo_guardado.write(self.texto.get("1.0", tk.END))
            archivo_guardado.close()
    def guardar_archivo_como(self):
        archivo_guardado = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                                    filetypes=[("Archivos de texto", ".txt"),
                                                               ("Todos los archivos", ".*")])
        if archivo_guardado is not None:
            archivo_guardado.write(self.texto.get("1.0", tk.END))
            archivo_guardado.close()
    def buscar_en_google(self):
        busqueda = self.texto.get("1.0", tk.END)
        webbrowser.open("https://www.google.com/search?q=" + busqueda)
    def calendario(self):
        # Crear la ventana principal
        root = tk.Tk()
        root.title("Calendario Docente 2023")

        # Crear un objeto de calendario para todo el año 2023
        calendario = calendar.Calendar()

        # Crear una lista de todos los meses del año
        year = 2023
        months = [calendario.monthdatescalendar(year, i + 1) for i in range(12)]

        # Crear un widget Canvas para mostrar los meses en filas de tres
        canvas = tk.Canvas(root, bg='#ffffff')
        canvas.pack(side='left', fill='both', expand=True)

        # Crear un frame para contener las tablas de los meses
        frame = tk.Frame(canvas, bg='#ffffff')
        canvas.create_window((0, 0), window=frame, anchor='nw')

        # Agregar las tablas de cada mes al frame
        for i, month in enumerate(months):
            subframe = tk.Frame(frame, bg='#ffffff')
            subframe.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            label = tk.Label(subframe, text=calendar.month_name[i + 1], font=('Arial', 12, 'bold'))
            label.pack(pady=5)
            table = tk.LabelFrame(subframe, bg='#ffffff')
            table.pack()
            # Configurar los encabezados de la tabla
            days = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
            for j, day in enumerate(days):
                header = tk.Label(table, text=day, font=('Arial', 10, 'bold'), bg='#ffffff')
                header.grid(row=0, column=j, padx=3, pady=3)
            # Agregar los días de cada semana a la tabla
            for j, week in enumerate(month):
                for k, day in enumerate(week):
                    if day.month != i + 1:
                        # Mostrar días vacíos para los días que no corresponden al mes actual
                        label = tk.Label(table, text='', font=('Arial', 10), bg='#ffffff')
                    else:
                        # Mostrar el número del día correspondiente al mes actual
                        label = tk.Label(table, text=day.day, font=('Arial', 10), bg='#ffffff')
                    label.grid(row=j + 1, column=k, padx=3, pady=3)

        # Configurar el scroll para el canvas
        scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))




