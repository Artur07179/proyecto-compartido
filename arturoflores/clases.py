import datetime
from datetime import date
from dateutil import relativedelta


class fechaCal:

	def __init__(self, dia, diaFin, mes, mesFin, año, añoFin):
		self.dia = dia
		self.mes = mes
		self.año = año
		self.diaFin = diaFin
		self.mesFin = mesFin
		self.añoFin = añoFin

	def calcularFechaT(self):
		yearsI = self.año
		monthsI = self.mes
		daysI = self.dia

		yearsE = self.añoFin
		monthsE = self.mesFin
		daysE = self.diaFin

		date1 = datetime.date(int(yearsI), int(monthsI), int(daysI))
		date2 = datetime.date(int(yearsE), int(monthsE), int(daysE))

		diff = relativedelta.relativedelta(date2, date1)
		years = diff.years 
		months = diff.months 
		days = diff.days

		complete = ('La diferencia es de {} días, {} meses y {} años'.format(days, months,years))

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

