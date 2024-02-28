from zeep import Client

client = Client('http://localhost:8000')
result1 = client.service.SumaDosNumeros(x=1,y=2)
result = client.service.Saludar(nombre="David")
result2 = client.service.CadenaPalindromo(cadena="oso")
print(result)
print(result1)
print(result2)