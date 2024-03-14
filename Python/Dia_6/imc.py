altura = input("Ingrese su altura en centimetros\n")
peso = input("ingrese su peso en Kg\n")
altura = float(altura)
altura = altura / 100
peso = float(peso)

print (type(peso))
print (type(altura))
imc = peso/(altura ** 2)  #La ecuación de imc

print(f"Tu IMC es de {imc:.2f}, según la clasificacíon de la OMS, te encuentras en el siguiente rango:")

if imc < 18.5:
    print("Bajo peso.")
elif imc >= 18.5 and imc <25:
    print("Peso adecuado.")
elif imc >= 25 and imc <30:
    print("Sobrepeso.")
elif imc >=30 and imc < 35:
    print("Obesidad grado I.")
elif imc >= 35 and imc < 40:
    print("Obesidad de grado II.")
else:
    print("Obesidad grado III.")
