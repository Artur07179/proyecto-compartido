from datetime import date
import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta


def diferencia_anos_dos_fechas(fecha01):
    try:
        fecha_actual01 = date.today()  # ! Obtiene la fecha actual
        diferencia01 = fecha_actual01.year - fecha01.year
        diferencia01 -= ((fecha_actual01.month, fecha_actual01.day) < (fecha01.month, fecha01.day))
        return diferencia01
    except Exception as e:
        print(e)
    finally:
        pass


def diferencia_meses_dos_fechas(fecha02):
    try:
        today = datetime.datetime.now()
        todayFormat = today.strftime("%d/%m/%Y")
        fechaActualObj = datetime.datetime.strptime(todayFormat, '%d/%m/%Y')
        diferencia02 = rrule.rrule(
            rrule.MONTHLY, dtstart=fecha02, until=fechaActualObj).count()
        return diferencia02-1
    except Exception as e:
        print(e)
    finally:
        pass


def diferencia_dias_dos_fechas(fecha03):
    try:
        fecha_actual03 = date.today() # ! Obtiene la fecha actual
        todayString03 = fecha_actual03.strftime("%d/%m/%Y")
        todayObj03 = datetime.datetime.strptime(todayString03, '%d/%m/%Y')
        diferencia01 = todayObj03 - fecha03
        return diferencia01.days
    except Exception as e:
        print(e)
    finally:
        pass


def diferencia_completa_dos_fechas(fecha04):
    try:
        today = datetime.datetime.now()
        todayString = today.strftime("%d/%m/%Y")
        todayObj = datetime.datetime.strptime(todayString, '%d/%m/%Y')
        diff = relativedelta(todayObj, fecha04)
        return (diff.years, diff.months, diff.days)
        #return print("La diferencia completa entre las fechas es de: %d años con %d meses y %d dias" % (diff.years, diff.months, diff.days))
    except Exception as e:
        print(e)
    finally:
        pass
