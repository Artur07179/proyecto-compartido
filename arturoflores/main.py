import clases as c1


print("Ingresa la fecha inicial : (ejem. dd-mm-aaaa 04-06-2021)")
fechaIni = input()
inicio = fechaIni.split (sep = "-")

diaIni = inicio[0]
mesIni = inicio[1]
añoIni = inicio[2]

print("Ingresa la fecha final : (ejem. dd-mm-aaaa 04-06-2021)")
fechaFin = input()
final = fechaFin.split (sep = "-")

diaFin = final[0]
mesFin = final[1]
añoFin = final[2]

try:
	fecha = c1.fechaCal(diaIni, diaFin, mesIni, mesFin, añoIni, añoFin)
	#calDia = fecha.calcularDia()
	calcTDias = fecha.calcularTotalDias() 
	calMes = fecha.calcularMes() 
	calAño = fecha.calcularAño()
	calTotal = fecha.calcularFechaT()

	#print("Total de días de diferencia es : " + calDia )
	print("El total de días es: " + calcTDias)
	print("El total de meses de diferencia es: " + calMes )
	print("El total de años de diferencia es: " + calAño )
	print(calTotal)
except:
	print("Has ingresado una fecha incorrecta")
	print("Puedes Volver a Intentarlo")