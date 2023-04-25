
import tkinter as tk



class Singleton:
    __instance = None

    # Constructor de la clase
    def __init__(self, root):
        # Verificamos si ya existe una instancia creada
        if Singleton.__instance is not None:
            # Si ya existe, lanzamos una excepción indicando que no se puede crear otra instancia
            raise Exception("No se puede crear otra instancia de Singleton")
        else:
            # Si no existe, creamos la instancia y la asignamos al atributo de clase
            Singleton.__instance = self
            # Asignamos el parámetro 'root' a un atributo de instancia
            self.root = root
            # Creamos un label con el texto "Esta es una instancia Singleton" y lo agregamos al root
            self.label = tk.Label(self.root, text="Esta es una instancia Singleton")
            self.label.pack()


    # Método estático que devuelve la instancia única de la clase Singleton
    @staticmethod
    def get_instance(root):
        if Singleton.__instance is None: # Si no existe una instancia creada, la creamos
            Singleton(root)
        return Singleton.__instance  # Devolvemos la instancia creada o la existente




#Creamos la clase SingletonFactory
#class SingletonFactory:
# Método estático que crea una instancia única de la clase Singleton
# @staticmethod def create_singleton(root): return Singleton.get_instance(root)

class SingletonFactory:
    # Método estático que crea y devuelve una instancia única de la clase Singleton
    @staticmethod
    def create_singleton(root):
        return Singleton.get_instance(root)
