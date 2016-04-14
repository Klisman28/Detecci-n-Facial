from pybrain.tools.shortcuts import buildNetwork    #Para la crear la neurona
from pybrain.datasets import SupervisedDataSet      #Para crear la data set
from pybrain.supervised.trainers import BackpropTrainer #Para el entrenamiento
from PIL import Image                               #Para procesamiento de imagenes
from numpy import array                             #Para crear las matriz y los array
import numpy as np

#Convierte la imagen en una matriz (150,150)
def Conversion(Nombre):
    img = Image.open(Nombre)
    arr = array(img)
    return arr

#Convierte una matriz en un array de una dimension para pasarlo como entrada
def ConvertirA1D(Matriz):
    unadimension = np.asarray(Matriz).flatten()
    return unadimension

# Numero de entradas como la imagen es de 150x150 la multiplicacion de estos dos es el numero de entradas
n = 150*150

#Para hacer la neurona se declara buildNetwork y despues el numero de neurona de entradas, el de la capa oculta
# y por ultimo las salidas.
neurona = buildNetwork(n, 30, 3)

#Entradas
x1 = ConvertirA1D(Conversion("rostro1.bmp"))
x2 = ConvertirA1D(Conversion("rostro2.bmp"))
x3 = ConvertirA1D(Conversion("rostro3.bmp"))
x4 = ConvertirA1D(Conversion("rostro4.bmp"))
x5 = ConvertirA1D(Conversion("rostro5.bmp"))

#Salida
y = array([1,0,0])

#Datos
ds = SupervisedDataSet(n, 3)

#Agregando valores
ds.addSample(x1,y)
ds.addSample(x2,y)
ds.addSample(x3,y)
ds.addSample(x4,y)
ds.addSample(x5,y)

#El entranamiento es backprop
entrenamiento = BackpropTrainer(neurona,ds)

#Un error de 10 para comenzar
error = 10
#un ciclo para cuando el error total sea menor a 0.001 se detenga
while error > 0.001:
    #Se sustituye el error, por el nuevo error generado
    error=entrenamiento.train()

#Los pesos correctos serian
print error
print entrenamiento.trainUntilConvergence()
