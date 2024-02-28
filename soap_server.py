from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
def SumaDosNumeros(x,y):
    sum=x+y
    return sum
def CadenaPalindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)
dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"suma": int},
    args={"x": int, "y": int},
)
dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"cadena": bool},
    args={"cadena": str},
)
server = HTTPServer(("0.0.0.0", 8000),SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()