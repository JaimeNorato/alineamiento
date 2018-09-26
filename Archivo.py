class Archivo:
    def __init__(self,dir=""):
        self.dir=dir
    # abre el archivo espesificad
    def abrir(self):
        archivo=False
        try:
            archivo=open(self.dir,"r")
        except:
            print("Error al abrir el archivo ")

        return archivo
    #cierra el archivo espesificado
    def cerrar(self,archivo):
        archivo.close()
    #lee y retorna el contenido de un archvo especificad
    def leer(self):
        data=""
        archivo=self.abrir()
        if archivo:
            data=archivo.readlines()
            self.cerrar(archivo)
        return data


arch=Archivo("adn2.txt")
dat=arch.leer()
print(dat)