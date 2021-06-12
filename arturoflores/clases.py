import datetime
from datetime import date

class fechaCal:

	def __init__(self, dia, diaFin, mes, mesFin, año, añoFin):
		self.dia = dia
		self.mes = mes
		self.año = año
		self.diaFin = diaFin
		self.mesFin = mesFin
		self.añoFin = añoFin

	def calcularFechaT(self):
		dayI = self.dia
		monthI = self.mes
		yearI = self.año
		dayEnd = self.diaFin
		monthEnd = self.mesFin
		yearEnd = self.añoFin

		dayTot = int(dayEnd) - int(dayI)
		monthTot = int(monthEnd) - int(monthI)
		yearTot = int(yearEnd) - int(yearI)

		parseoDay = str(dayTot)
		parseoMonth = str(monthTot)
		parseoYear = str(yearTot)

		complete = ("Hay " + parseoDay + " dias, " + parseoMonth + " meses y " + parseoYear + " años de diferencia")

		return complete

	def calcularMes(self):
		diaI = self.dia 
		mesI = self.mes 
		añoI = self.año 
		diaF = self.diaFin 
		mesF = self.mesFin
		añoF = self.añoFin 

		start_date = datetime.date(int(añoI), int(mesI), int(diaI))
		end_date = datetime.date(int(añoF), int(mesF), int(diaF))

		num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
		
		monthsStr = str(num_months)

		return monthsStr

	def calcularAño(self):
		añoI = self.año
		añoF = self.añoFin

		totalAño = int(añoF) - int(añoI)
		totalAñoStr = str(totalAño)

		return totalAñoStr

	def calcularTotalDias(self):
		diaI = self.dia
		mesI = self.mes
		añoI = self.año
		diaF = self.diaFin
		mesF = self.mesFin
		añoF = self.añoFin

		fecha1 = date(int(añoI), int(mesI), int(diaI))
		fecha2 = date(int(añoF), int(mesF), int(diaF))

		diferencia = fecha2 - fecha1
		diferenciaStr=str(diferencia.days)

		
		return diferenciaStr