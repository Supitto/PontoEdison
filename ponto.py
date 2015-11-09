import json

class Ponto:
	def __init__(self):
		with open('config.json', 'r') as f:
			config = json.load(f)

		#edit the data
		self.ponto_id = config['ponto_id']