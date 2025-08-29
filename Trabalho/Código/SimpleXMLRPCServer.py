from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restringir a um caminho.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000),# Criar Server

                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    def tabuada(x) : #fFunçao Tabuada
        resultado="" #Declara a string
        for n in range (0,11): # Vai dando valor
            resultado += f"{x} x {n} = {x * n}\n"# Tabuada
        return resultado # Output da Tabuada

    server.register_function(tabuada, 'tb')# Registar a funçao

    server.serve_forever()   # Executar o servidor

