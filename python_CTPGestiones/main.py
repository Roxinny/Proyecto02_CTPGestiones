from patrondiseño import Singleton
from clases import MyApplication
import tkinter as tk
from clases import Acceso


## Crear una instancia de la clase Acceso acceso = Acceso()
# Ejecutar el método mainloop() de la instancia de Acceso acceso.root.mainloop()

if __name__ == '__main__':
    acceso = Acceso()
    acceso.root.mainloop()


#Crear otra instancia de Tk y de MyApplication utilizando el patrón Singleton
root1 = tk.Tk()
app1 = Singleton.get_instance(root1)

root2 = tk.Tk()
app2 = Singleton.get_instance(root2)

# comprobar si son la misma instancia
print(app1 == app2)  # True
