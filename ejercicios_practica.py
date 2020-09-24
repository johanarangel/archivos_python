#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana 
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re


def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un programa que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "texto.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    fi = open('texto.txt', 'r')
    sumatoria_total = 0

    while True:
        line = fi.readline()
        caracteres_linea = len(line)
        sumatoria_total += caracteres_linea
                
        if not line:
            break
    
    print('La sumatoria total de caracteres del archivo "texto.txt" es:', sumatoria_total)
        
    fi.close()


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contando cuantos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fo = open('escritura.txt', 'w') 
    caracteres_archivo = 0

    while True:
        texto = str(input('Ingrese texto \n'))
        fo.write(texto)
        fo.write('\n')
        caracteres_linea = len(texto)
        caracteres_archivo += caracteres_linea
                        
        if len(texto) == 0:
            print('Ha salido del programa')
            break
    
    print('Se copiaron {} caracteres al archivo'.format(caracteres_archivo))
    
    
    fo.flush()
    fo.close()


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un programa que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    alquiler_ars = 0  
    consulta_ambientes = int(input('Ingrese la cantidad de ambientes:\n'))
    archivo = open('propiedades.csv')
    data = list(csv.DictReader(archivo))
    cantidad_filas = len(data)
    sumatoria = 0
    lista_precio = []
                
    for i in range(cantidad_filas):
        row = data[i]
        ambientes = row.get('ambientes')
        monedas = row.get('moneda')
        precio = float(row.get('precio'))
                                               
        if (ambientes == str(consulta_ambientes) and monedas == 'ARS'):
            sumatoria += precio
            lista_precio.append(precio)
            alquiler_ars += 1
            
    try:
        promedio = sumatoria / alquiler_ars 
    except:
        print('No se puede dividir por cero')
                                      
    print('Los alquileres en "pesos" disponibles por {} ambientes son {}'.format(consulta_ambientes, alquiler_ars))
    print('El promedio de los alquileres en "pesos" de {} ambientes es {}'.format(consulta_ambientes, round(promedio, 2)))
    print('El máximo valor de alquiler en "pesos" es {} por {} ambientes'.format(max(lista_precio), consulta_ambientes))
    print('El mínimo valor de alquiler en "pesos" es {} por {} ambientes'.format(min(lista_precio), consulta_ambientes))

    archivo.close()


def ejercicio_extra():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
           
    
    archivo = '2019 Ironman World Championship Results.csv'
    #-----------categoria MPRO---------
    time_swim = []
    time_bike = []
    time_run = []

    #-----------categoria M45-49---------
    tiempo_swim = []
    tiempo_bike = []
    tiempo_run = []

    #-----------categoria M25-29---------
    tiempo_swim_m2529 = []
    tiempo_bike_m2529 = []
    tiempo_run_m2529 = []

    #-----------categoria M18-24---------
    tiempo_swim_m1824 = []
    tiempo_bike_m1824 = []
    tiempo_run_m1824 = []

    with open(archivo) as csvfile:
        data = list(csv.DictReader(csvfile))
        cantidad_filas = len(data)
    
    #-------------------- categoria MPRO, Swim--------------------------
        for i in range(cantidad_filas):
            row = data[i]
            categoria = row.get('Division')
            swim = row.get('Swim')
            bike = row.get('Bike')
            run = row.get('Run')

            if  categoria== 'MPRO':
                time= swim.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                time_swim.append(total_segundos)
                promedio_swim = sum(time_swim) / len(time_swim)

    #-------------------- categoria MPRO, Bike--------------------------
        
                time= bike.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                time_bike.append(total_segundos)
                promedio_bike = sum(time_bike) / len(time_bike)

    #-------------------- categoria MPRO, Run--------------------------
        
                time= run.split(sep=':')
                    
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                    
                except ValueError:
                    pass

                time_run.append(total_segundos)
                promedio_run = sum(time_run) / len(time_run)

               
        #-------------------- categoria M45-49, Swim--------------------------
        #---------------------------------------------------------------------
        
            elif  categoria== 'M45-49':
                time= swim.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                tiempo_swim.append(total_segundos)
                promedio_swim_m4549 = sum(tiempo_swim) / len(tiempo_swim)

    #-------------------- categoria M45-49, Bike--------------------------
        
                time= bike.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                tiempo_bike.append(total_segundos)
                promedio_bike_m4549 = sum(tiempo_bike) / len(tiempo_bike)

    #-------------------- categoria M45-49, Run--------------------------
        
                time= run.split(sep=':')
                    
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                    
                except ValueError:
                    pass

                tiempo_run.append(total_segundos)
                promedio_run_m4549 = sum(tiempo_run) / len(tiempo_run)

        #-------------------- categoria M25-29, Swim--------------------------
        #---------------------------------------------------------------------
        
            elif  categoria== 'M25-29':
                time= swim.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                tiempo_swim_m2529.append(total_segundos)
                promedio_swim_m2529 = sum(tiempo_swim_m2529) / len(tiempo_swim_m2529)

    #-------------------- categoria  M25-29, Bike--------------------------
        
                time= bike.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                tiempo_bike_m2529.append(total_segundos)
                promedio_bike_m2529 = sum(tiempo_bike_m2529) / len(tiempo_bike_m2529)

    #-------------------- categoria  M25-29, Run--------------------------
        
                time= run.split(sep=':')
                    
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                    
                except ValueError:
                    pass

                tiempo_run_m2529.append(total_segundos)
                promedio_run_m2529 = sum(tiempo_run_m2529) / len(tiempo_run_m2529)

        #-------------------- categoria M18-24, Swim--------------------------
        #---------------------------------------------------------------------
        
            elif  categoria== 'M18-24':
                time= swim.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                tiempo_swim_m1824.append(total_segundos)
                promedio_swim_m1824 = sum(tiempo_swim_m1824) / len(tiempo_swim_m1824)

    #-------------------- categoria M18-24, Bike--------------------------
        
                time= bike.split(sep=':')
                
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                
                except ValueError:
                    pass

                tiempo_bike.append(total_segundos)
                try:
                    promedio_bike_m1824 = sum(tiempo_bike_m1824) / len(tiempo_bike_m1824)
                
                except ZeroDivisionError:
                    pass
                
    #-------------------- categoria M18-24, Run--------------------------
        
                time= run.split(sep=':')
                    
                try:
                    horas = int(time[0])
                    minutos = int(time[1])
                    segundos = int(time[2])
                    total_segundos = horas * 3600 + minutos * 60 + segundos
                    
                except ValueError:
                    pass

                tiempo_run_m1824.append(total_segundos)
                promedio_run_m1824 = sum(tiempo_run_m1824) / len(tiempo_run_m1824)

        #-------------------- Resultados categoria MPRO, swim--------------------------
        try: 
            print('El tiempo máximo realizado en la categoria: MPRO, en Swim es', max(time_swim), 'seg') 
            print('El tiempo mínimo realizado en la categoria: MPRO, en Swim es', min(time_swim), 'seg')
            print('El tiempo promedio en la categoria: MPRO, en Swim es', round(promedio_swim, 2), 'seg')
        
        #-------------------- Resultados categoria MPRO, bike--------------------------
         
            print('El tiempo máximo realizado en la categoria: MPRO, en Bike es', max(time_bike), 'seg') 
            print('El tiempo mínimo realizado en la categoria: MPRO, en Bike es', min(time_bike), 'seg')
            print('El tiempo promedio en la categoria: MPRO, en Bike es', round(promedio_bike, 2), 'seg')
        
        #-------------------- Resultados categoria MPRO, run--------------------------

            print('El tiempo máximo realizado en la categoria: MPRO, en Run es', max(time_run), 'seg') 
            print('El tiempo mínimo realizado en la categoria: MPRO, en Run es', min(time_run), 'seg')
            print('El tiempo promedio en la categoria: MPRO, en Run es', round(promedio_run, 2), 'seg')

        #-------------------- Resultados categoria M45-49, swim--------------------------
        #--------------------------------------------------------------------------------
        
            print('El tiempo máximo realizado en la categoria:M45-49, en Swim es', max(tiempo_swim), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M45-49, en Swim es', min(tiempo_swim), 'seg')
            print('El tiempo promedio en la categoria: M45-49, en Swim es', round(promedio_swim_m4549, 2), 'seg')
        
        #-------------------- Resultados categoria M45-49, bike--------------------------
         
            print('El tiempo máximo realizado en la categoria: M45-49, en Bike es', max(tiempo_bike), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M45-49, en Bike es', min(tiempo_bike), 'seg')
            print('El tiempo promedio en la categoria: M45-49, en Bike es', round(promedio_bike_m4549, 2), 'seg')
        
        #-------------------- Resultados categoria M45-49, run--------------------------

            print('El tiempo máximo realizado en la categoria: M45-49, en Run es', max(tiempo_run), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M45-49, en Run es', min(tiempo_run), 'seg')
            print('El tiempo promedio en la categoria: M45-49, en Run es', round(promedio_run_m4549, 2), 'seg')

        #-------------------- Resultados categoria M25-29, swim--------------------------
        #--------------------------------------------------------------------------------
        
            print('El tiempo máximo realizado en la categoria:M25-29, en Swim es', max(tiempo_swim_m2529), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M25-29, en Swim es', min(tiempo_swim_m2529), 'seg')
            print('El tiempo promedio en la categoria: M25-29, en Swim es', round(promedio_swim_m2529, 2), 'seg')
        
        #-------------------- Resultados categoria M25-29, bike--------------------------
         
            print('El tiempo máximo realizado en la categoria: M25-29, en Bike es', max(tiempo_bike_m2529), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M25-29, en Bike es', min(tiempo_bike_m2529), 'seg')
            print('El tiempo promedio en la categoria: M25-29, en Bike es', round(promedio_bike_m2529, 2), 'seg')
        
        #-------------------- Resultados categoria M25-29, run--------------------------

            print('El tiempo máximo realizado en la categoria: M25-29, en Run es', max(tiempo_run_m2529), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M25-29, en Run es', min(tiempo_run_m2529), 'seg')
            print('El tiempo promedio en la categoria: M25-29, en Run es', round(promedio_run_m2529, 2), 'seg')
        
        #-------------------- Resultados categoria M18-24, swim--------------------------
        #--------------------------------------------------------------------------------
        
            print('El tiempo máximo realizado en la categoria: M18-24, en Swim es', max(tiempo_swim_m1824), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M18-24, en Swim es', min(tiempo_swim_m1824), 'seg')
            print('El tiempo promedio en la categoria: M18-24, en Swim es', round(promedio_swim_m1824, 2), 'seg')
        
        #-------------------- Resultados categoria M18-24, bike--------------------------
         
            print('El tiempo máximo realizado en la categoria: M18-24, en Bike es', max(tiempo_bike_m1824), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M18-24, en Bike es', min(tiempo_bike_m1824), 'seg')
            print('El tiempo promedio en la categoria: M18-24, en Bike es', round(promedio_bike_m1824, 2), 'seg')
        
        #-------------------- Resultados categoria M18-24 , run--------------------------

            print('El tiempo máximo realizado en la categoria: M18-24, en Run es', max(tiempo_run_m1824), 'seg') 
            print('El tiempo mínimo realizado en la categoria: M18-24, en Run es', min(tiempo_run_m1824), 'seg')
            print('El tiempo promedio en la categoria: M18-24, en Run es', round(promedio_run_m1824, 2), 'seg')
        except ValueError:
            pass
                
        

    csvfile.close()
     

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ejercicio_extra()
