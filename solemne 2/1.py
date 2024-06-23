# resumen = []
# dias = {1:'Lunes', 2:'Martes', 3:'Miercoles', 4:'Jueves', 5:'Viernes'}
# num_empleados =  int(input('Ingrese la cantidad de empleados a registrar:'))

# def datos():
#     for i in range(num_empleados):
#         empleado = [] #Guardo los datos de mi empleado

#         nombre_empleado = input(f'ingrese el nombre del empleado N°{i+1}: ')
#         etiqueta_empleado = input(f'Ingrese la etiqueta del empleado N° {i+1}\n 1- Programador \n 2- Depurador \n 3- Backend \n 4- Devops \n ')

#         nombre_etiqueta = (nombre_empleado, etiqueta_empleado)
#         empleado.append(nombre_etiqueta)

#         for j in range(0,5):
#             horas_trabajadas = int(input(f'Ingrese las horas trabajadas por {nombre_empleado} para el día {dias[j+1]}: '))
#             dia = (dias[j+1], horas_trabajadas)
#             empleado.append(dia)

#         resumen.append(empleado)

#     print(resumen)
# datos()


# def dla_mes_hora(dias, resumen):
#     num_etiqueta = int(input('Ingrese el numero de etiqueta: '))
#     dia_seleccionado = int(input('Seleccione un dia: \n 1- Lunes \n 2- Martes \n 3- Miercoles \n 4- Jueves \n 5- Viernes \n'))
#     max_horas = 0
#     max_empleado = ''

#     dia_nombre = dias[dia_seleccionado]

#     for empleado in resumen:
#         nombre_empleado, etiqueta_empleado = empleado[0]

#         if etiqueta_empleado ==  num_etiqueta:
#             for dia in empleado[1:]:
#                 if dia[0] == dia_nombre and dia[1] > max_horas:
#                     max_horas = dia[1]
#                     max_empleado = nombre_empleado

#     print(f'El empleado que mas horas trabajo fue {max_empleado} con {max_horas} el dia {dia_nombre}')

# dla_mes_hora(dias, resumen)

# def empleado_top():
#     max_horas_semanal = 0
#     max_empleado_semanal = ''
#     total_horas = 0

#     for empleado in resumen:
#         nombre_empleado, etiqueta_empleado = empleado[0]
#         for dia in empleado[1:]:
#             total_horas += dia[1]

#         if total_horas > max_horas_semanal:
#             max_horas_semanal = total_horas
#             empleado_max_semanal = nombre_empleado

#     print(f'El empleado que mas horas trabajo en la semana fue {empleado_max_semanal} con {max_empleado_semanal}')

# empleado_top()



def datos():
    num_empleados = int(input('Ingrese el numero de empleados a registrar: '))
    for i in range(num_empleados):
        data_empleado = []
        nombre = input(f'Ingrese el nombre del empleado {i+1}: ')
        etiqueta = int(input(f'Ingrese la etiqueta del empleado {i+1}: '))

        nombre_etiqueta = (nombre, etiqueta)
        data_empleado.append(nombre_etiqueta)

datos()

