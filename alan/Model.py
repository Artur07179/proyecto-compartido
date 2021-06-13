class Reporte:

    def __init__(self, n, c, f):
        self.autor = n
        self.contenido = c
        self.fecha = f

    def mostrar_reporte(self):
        print("El software lo diseño: "+self.autor + '\n' + "El contendio del software es de: " + self.contenido + '\n' "El software se desarrollo el dia: "+self.fecha + '\n')
