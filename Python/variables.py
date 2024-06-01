#dato
nombre = "Endert"

#concatenar con f-strings
bienvenida = f"Hola  {nombre}  ¿Como estas?"

#concatenar con +
bienvenida= "Hola " + nombre + " ¿Como estas?"

#operadores de pertenencia(in y not in)
print("elpepe" in bienvenida)
print("elpepe" not in bienvenida)

print(bienvenida)

#type(dato) nos devuelve que tipo de dato es
tipo_de_dato = type("hola")
tipo_de_dato1 = type(("hola",55,22))
tipo_de_dato2 = type(["hola",55,66])
tipo_de_dato3 = type({"hola",55,66})


print(tipo_de_dato)
print(tipo_de_dato1)
print(tipo_de_dato2)
print(tipo_de_dato3)



