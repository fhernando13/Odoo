import datetime

# hoy = datetime.date.today()
# print(hoy)
# hoy = str(hoy)
# hoy = hoy[0:4]
# print(hoy)

import datetime
fecha1 = datetime.date(2022, 10, 19)
fecha2 = datetime.date(2022, 10, 20)

if fecha1 == fecha2:
    print('son iguales')
elif fecha1 < fecha2:
    print('mañana')
elif fecha1 > fecha2:
    print('ayer')