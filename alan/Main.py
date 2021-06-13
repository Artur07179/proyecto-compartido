# Inicializa la importación de módulos y librerías
import Def as misfunciones
import Model as miclase
import datetime
from datetime import date
from colorit import *
from colorama import Fore, init


# * Inicializa imprimir en la consola a color
init()
init_colorit()


# * Inicializa la manipulación de fecha y hora
currentTime = datetime.datetime.now()
format = currentTime.strftime('[%d-%m-%y]-[%Ihrs %Mmin]')

print("")
print(Fore.BLUE + "Inicio del software 🚥\n")

try:
    # * Crea los encabezados en el documento a generar
    header = open('DiferenciaFechas-'+format+'.txt', "a", encoding='utf8')
    header.write("AÑOS")
    header.write('\t')
    header.write("MESES")
    header.write('\t')
    header.write("DIAS")
    header.write('\t')
    header.write("COMPLETA")
    header.write('\n')
    header.close()
    


    # * Pide la fecha al usuario
    ejemploFecha = ("15/07/1997")
    dateUsuario = str((input("Ingrese una fecha con el siguiente formato " + "'" + ejemploFecha + "':\n")))


    #!Llamado funcion 1
    dateUsuario01 = dateUsuario
    dateObj = datetime.datetime.strptime(dateUsuario01, '%d/%m/%Y')
    resultadoAnos = misfunciones.diferencia_anos_dos_fechas(dateObj)
    print("")
    print("La diferencia de años entre las fechas es de: {0}".format(resultadoAnos) + ' ' + 'años')
    print("Fin llamado a la funcion número 1\n")

    
    #!Llamado funcion 2
    dateUsuario02 = dateUsuario
    dateObj02 = datetime.datetime.strptime(dateUsuario02, '%d/%m/%Y')
    resultadoMeses = misfunciones.diferencia_meses_dos_fechas(dateObj02)
    print("La diferencia de meses entre las fechas es de: {0}".format(resultadoMeses) + ' ' + 'meses')
    print("Fin llamado a la funcion número 2\n")

    #!Llamado funcion 3
    dateUsuario03 = dateUsuario
    #dateSTR03 = datetiSme.datetime.strftime(dateUsuario03, '%d/%m/%Y')
    #print(dateSTR03)
    dateObj03 = datetime.datetime.strptime(dateUsuario03, '%d/%m/%Y')
    resultadoDias = misfunciones.diferencia_dias_dos_fechas(dateObj03)
    print("La diferencia de dias entre las fechas es de: {0}".format(resultadoDias) + ' ' + 'dias')
    print("Fin llamado a la funcion número 3\n")

    #!Llamado funcion 4
    dateUsuario04 = dateUsuario
    dateObj04 = datetime.datetime.strptime(dateUsuario04, '%d/%m/%Y')
    resultadoCompleto = misfunciones.diferencia_completa_dos_fechas(dateObj04)
    resultadoTexto = "La diferencia completa entre las fechas es de:"
    resultadoOperacion = (str(resultadoCompleto[0]) + ' ' + 'años con' + ' ' + str(resultadoCompleto[1]) + ' ' + 'meses y' + ' ' + str(resultadoCompleto[2]) + ' ' + 'dias')
    resultadoFinal= resultadoTexto + ' ' + resultadoOperacion
    print(resultadoFinal)
    print("Fin llamado a la funcion número 4\n")

    # * Genera el archivo
    contents = open('DiferenciaFechas-'+format+'.txt', "a", encoding='utf8')
    contents.write(str(resultadoAnos))
    contents.write('\t')
    contents.write(str(resultadoMeses))
    contents.write('\t')
    contents.write(str(resultadoDias))
    contents.write('\t')
    contents.write(str(resultadoOperacion))
    contents.write('\n')
    contents.close()
    
    
except Exception as e:
    print(e)


finally:
    print(color("Fin del software 🏁\n", Colors.green))


Reporte01 = miclase.Reporte("Alan", "Manipular fechas", "6/12/2021")
print(Fore.LIGHTMAGENTA_EX + "Y un pequeño reporte 📋" + "\n")
Reporte01.mostrar_reporte()
