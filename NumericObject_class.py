# a new object that supports being deserialised from simple json or dict 


from NumericTool_namespace import NumericTool

class NumericObject:

	def __init__(self, value, base, dict_data=None):

		self.base2			= "0000 0000"
		self.base10 		= 0
		self.base16 		= "0000"
		self.custom_base	= 0
		self.custom_value	= []

		if dict_data is None: # then do a normal init


			if type(value) is list:

				self.raw_value 	= ''.join(map(str, value))
			else:

				self.raw_value	= value


			self.raw_base		= base
			self.int_value		= int(self.raw_value, self.raw_base)

			self.base2 			= NumericTool.toDigits(self.int_value, 2)
			self.base10			= NumericTool.toDigits(self.int_value, 10)
			self.base16			= NumericTool.toDigits(self.int_value, 16)
		else: # then do a factory deserialized intit

			self.raw_value		= dict_data["raw_value"]
			self.raw_base		= dict_data["raw_base"]
			self.int_value		= dict_data["int_value"]

			self.base2 			= dict_data["base2"]
			self.base10			= dict_data["base10"]
			self.base16			= dict_data["base16"]

			self.custom_base	= dict_data["custom_base"]
			self.custom_value	= dict_data["custom_value"]




	def calculateCustomBase(self, custom_base):

		self.custom_base	= custom_base
		self.custom_value	= []

		if custom_base > 0:
			self.custom_value	= NumericTool.toDigits(self.int_value, custom_base)