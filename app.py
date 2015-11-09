from connection_util import *
from ponto import *
import server_util as server


def run():
	logging.basicConfig(level=logging.DEBUG)

	ponto = Ponto()
	
	server.init()

	server.fetch_bus(ponto)
	manage_connection(True)
	
	server.run_server()