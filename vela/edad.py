import datetime
from dateutil.relativedelta import relativedelta



def fecha():
    
    

    a = input("ingresa la fecha inicial:") #datetime.datetime.now()
    b = input("ingresa la fecha final:")

    start = datetime.datetime.strptime(a, "%Y-%m-%d")
    ends = datetime.datetime.strptime(b, "%Y-%m-%d")

    diff = relativedelta(start, ends)

    print ("Tienes %d años con %d meses y %d dias " % (diff.years, diff.months, diff.days))


print(fecha())
