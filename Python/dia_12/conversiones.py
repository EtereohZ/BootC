import sys

sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])
CLP = float(sys.argv[4])

sol_convertido = CLP * sol_peruano
peso_convertido = CLP * peso_argentino
dolar_convertido = CLP * dolar

print(f"""
los {CLP} pesos equivalen a:
{sol_convertido} Soles
{peso_convertido} Pesos argentinos
{dolar_convertido} dolares

      """)