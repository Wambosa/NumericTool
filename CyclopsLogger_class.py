#import pprint

class CyclopsLogger:



	def __init__(self, filename=None, debug_level=5, is_self_verbose=False):

		self.is_self_verbose 	= False					# will display debug information on screen about the Cyclopslogger activity itself
		self.debug_level		= debug_level		# is dependant on the program. filters input higher than debug_level int. lower values are more important
		self.filename			= filename			# the string name of the file

		self.file_handle 		= None				# the connection to the file handle that is the log file

		if filename != None:
			# create file for writting. open up the handle

			self.file_handle = open(filename, "a")
		else:

			self.is_self_verbose = True
			print("New CyclopsLogger created in verbose mode...", "file handle automatically opened for:", filename)



	def close(self):

		self.file_handle.close()

		if self.is_self_verbose:
			print(self.filename, "file handle closed using CyclopsLogger.close()!")



	def clear(self, filename=None):

		is_cleared = 0

		if filename is not None:

			is_cleared = 1
			temp = open(filename, "w")
			temp.close()

		elif self.filename is not None:

			is_cleared = 1
			self.close()
			temp = open(self.filename, "w")
			temp.close()
			self.file_handle = open(self.filename, "a")


		if self.is_self_verbose & is_cleared:
			print(filename, "file was cleared of all text using CyclopsLogger.clear()!")



	def write(self, data, message_importance=1, is_auto_newline=1):

		newline_char = ""

		if is_auto_newline:
			newline_char = "\n"

		if message_importance <= self.debug_level:

			if type(data) is dict:

				import json
				new_string = json.dumps(data, sort_keys=True,indent=4)
			else:

				new_string = str(data) # pprint.pprint(data)   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PICK UP HERE

			print(new_string)

			if self.file_handle is not None:

				self.file_handle.write(new_string + newline_char)