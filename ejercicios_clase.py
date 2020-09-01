#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0    

    '''
    Realizar un programa que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    fi = open('notas.txt', 'r')

    for line in fi:
        cantidad_lineas += 1
                
    print(cantidad_lineas)
        
    fi.close()

def contar_lineas(nombre_archivo):

    cantidad_lineas = 0
    fi = open('notas.txt', 'r')

    for line in fi:
        cantidad_lineas += 1
                
    print(cantidad_lineas)
        
    fi.close()


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)
    # Recuerde cerrar los archivos al final ;)

    
    fi = open('notas.txt', 'r')         
    fo = open('notas_copia.txt', 'w')   
    
    while True:
        line = fo.write(fi.readline())
        cantidad_lineas += 1
        
        if not line:
            break
    
    print('Cantidad lineas', cantidad_lineas)
    
    fi.flush()
    fi.close()
    fo.flush()
    fo.close()


def ej3():
    # Ejercicios con archivos CSV
    
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrer dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    archivo = open('propiedades.csv')
    data = list(csv.DictReader(archivo))

    cantidad_filas = len(data)
    cantidad_dos_ambientes = 0
    cantidad_tres_ambientes = 0
    
    for i in range(cantidad_filas):
        row = data[i]
        ambientes = row.get('ambientes')
        if ambientes == '2':
            cantidad_dos_ambientes += 1

        elif ambientes == '3':
            cantidad_tres_ambientes += 1
        
    print('Cantidad departamentos dos ambientes:', cantidad_dos_ambientes)
    print('Cantidad departamentos tres ambientes:', cantidad_tres_ambientes)

    archivo.close()


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''
    
    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    fruta_verdura = str(input('Ingrese el NOMBRE DE LA FRUTA/VERDURA:\n Escriba "FIN" para salir:\n'))
    
    while fruta_verdura != 'FIN':
        cantidad = int(input('Ingrese cantidad en stock:\n'))
        inventario[fruta_verdura] = cantidad
        print('Inventario', inventario)
        fruta_verdura = str(input('Ingrese el NOMBRE DE LA FRUTA/VERDURA:\n Escriba "FIN" para salir:\n'))

        if fruta_verdura == 'FIN ':
            break


def ej5():
    # Ejercicios con archivos CSV
    inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    csvfile = open('inventario.csv', 'w', newline='')

    header = ['Fruta Verdura', 'Cantidad']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
 
    fruta_verdura = str(input('Ingrese el NOMBRE DE LA FRUTA/VERDURA:\n Escriba "FIN" para salir:\n'))
    
    while fruta_verdura != 'FIN':
        if fruta_verdura != 'FIN':
            try:
                cantidad = int(input('Ingrese cantidad en stock:\n'))
            except:
                print('El valor ingresado no es un número, intente nuevamente')
                cantidad = int(input('Ingrese cantidad en stock:\n'))

            writer.writerow({'Fruta Verdura': fruta_verdura, 'Cantidad': cantidad})
            fruta_verdura = str(input('Ingrese el NOMBRE DE LA FRUTA/VERDURA:\n Escriba "FIN" para salir:\n'))
                
        elif fruta_verdura == 'FIN ':
            break             


    csvfile.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #contar_lineas(nombre_archivo='notas.txt')
    #ej2()
    #ej3()
    #ej4()
    ej5()
 