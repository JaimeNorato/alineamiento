from Archivo import Archivo

class Alineamiento:

    def __init__(self):
        self.archivo=Archivo("adn1.txt")
        self.cargarData()
        self.matrizScore=dict({# a
            "AA":10,"AG":-1,"AC":-3,"AT":-4,
            # g
            "GA":-1,"GG":7,"GC":-5,"GT":-3,
            # c
            "CA":-3,"CG":-5,"CC":9,"CT":0,
            # t
            "TA":-4,"TG":-3,"TC":0,"TT":8,});

    #carga el archivo a memoria
    def cargarData(self):
        self.data=self.archivo.leer()

    #carga la secuencia de adn indecada dentro de un archivo
    def cargarSecuencia(self,index=0):
        return self.data.toArray(index)

    #crea la matriz con las dos cadenas de adn, que permitira el alineamiento
    def preAlineamineto(self):
        self.matrizParcial={}
        self.secuenciaX=self.cargarSecuencia(0)
        self.secuenciaY=self.cargarSecuencia(1)
        data=0
        cerosY=0
        i=j=0
        for value in self.secuenciaY:
            self.matrizParcial[i]={}
            #agrega valores en x segun la pocision y
            for item in self.secuenciaX:
                data = self.calcularDato(value,item,i,j,data)
                self.matrizParcial[i][j] = data
                j+=1

            # valor 0 en Y=0
            cerosY += -5
            data=cerosY
            i+=1
            j=0

        return self.armarAlineamiento(i,j)

    #arma el alineamiento
    def armarAlineamiento(self,i,j):
        arriba=""
        abajo=""
        data=self.buscarDato(i,j)
        abajo=data[0]+abajo
        arriba=data[1]+arriba
        if data[2]>=0 or data[3]>=0:
            cadenas=self.armarAlineamiento(data[2],data[3])
            arriba=cadenas[0]+arriba
            abajo=cadenas[1]+abajo

        return [arriba,abajo]


    #calcula el valor para posicion indicada
    def calcularDato(self,posY,posX,i,j,dato):
        # agrega columna 0 en X
        if posY == '0' and posX=='0':
            return 0
        elif posY=='0':
            return dato-5
        elif posX == '0':
            return dato
        else:
            diagonal=self.matrizParcial[i-1][j-1]+self.matrizScore[posY+posX]
            arriba=self.matrizParcial[i-1][j]+self.matrizScore[posY+posX]
            derecha=self.matrizParcial[i][j-1]+self.matrizScore[posY+posX]
            #print('------------------------------------------------------------------------------------------------------')
            #print(diagonal, self.matrizParcial[i - 1][j - 1], self.matrizScore[posY + posX])
            #print(arriba, self.matrizParcial[i - 1][j], self.matrizScore[posY + posX])
            #print(derecha, self.matrizParcial[i][j - 1], self.matrizScore[posY + posX])
            if diagonal>=arriba and diagonal>=derecha:
                return diagonal
            elif arriba>=derecha:
                return  arriba
            else:
                return derecha

    #busca el caracter que se alinea mejor
    def buscarDato(self,i,j):
        posY=self.secuenciaY[i]
        posX=self.secuenciaX[j]
        diagonal=self.matrizParcial[i-1][j-1]+self.matrizScore[posY+posX]
        arriba = self.matrizParcial[i - 1][j] + self.matrizScore[posY + posX]

        if diagonal==self.matrizParcial[i][j]:
            return [posY,posX,i-1,j-1]
        elif arriba==self.matrizParcial[i][j]:
            return [posY,'_', i-1, j]
        else:#derecha
            return ['_', posX, i, j-1]




alin=Alineamiento()
alin.preAlineamineto()
print(alin.matrizParcial)