#!/usr/bin/python3.4

'''
2.7.14 created to help understand bit operations

need a quick way to view a number in different angles or base versions.

input/output should be:

root@cpu:> get_numeric_info.py value base optional_base_conversion_request


root@cpu:> get_numeric_info.py 5 10

base2:		0000 0101
base10:		5
base16:		5
basex:		(this line will only show up if the user inputed the 3rd optional argument)



FLAGS / ARGS:

-b OR --base			default 10
-c OR --custom-base		a custom base to add to the conversion chart
-v OR --value			no default, required input


-l OR --left			does left << bitshift and returns both the original values and the newly shifted values (NOTE that <<< is unecesarry unsigned because the value will always go up into positive)
-ls OR --left-shift		alias for -l

-r OR --right					(SIGNED >> )same as left but right shift
-rs OR --right-shift			alias to -r

-urs OR --unsigned-right-shift	(UNSIGNED >>>) considered logical shift operator
-ur OR -rrr OR -rrs				alias to -urs

'''


import sys
import time
import datetime

# custom imports
from CyclopsLogger_class import CyclopsLogger
from NumericTool_namespace import NumericTool
from NumericObject_class import NumericObject
from ObjectJson_namespace import ObjectJson



def Main(args):

	log 		= CyclopsLogger("get_numeric_info.log", 9)

	is_bitshift = False

	epoch_time 	= int(time.time())



	log.write("\n\n\n\n...::: Numeric Information :::...", 1)
	log.write(str(epoch_time) + " : " + str(datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S') ) +"\n\n\n\n", 1)



	log.write("\nSTEP 1: Get Arguments\n", 3)
	log.write("Raw Serialized Arguments:", 8)
	log.write(args, 8)


	if len(args) < 3:

		log.write("FATAL: there are not enough arguments given to use this tool", 1)
		log.write(["args captured:", args])

		print("\n\nAcceptable Options :\n\n-b OR --base\t\t\t\tdefault 10\n-c OR --custom-base\t\t\tcustom base to add to the conversion chart\n-v OR --value\t\t\t\tno default, required input!\n-l OR --left\t\t\t\tdoes left << bitshift (NOTE that <<< is unecesarry unsigned because the value will always go up into positive)\n-ls OR --left-shift\t\t\talias for -l\n-r OR --right\t\t\t\t(SIGNED >> )same as left but right shift\n-rs OR --right-shift\t\t\talias to -r\n-urs OR --unsigned-right-shift\t\t(UNSIGNED >>>) considered logical shift operator\n-ur OR -rrr OR -rrs\t\t\talias to -urs")
		exit(0)
	else:

		action_data = getDeserializedArgs(args)

		log.write("Action Data:", 8)
		log.write(action_data, 8)
		

		log.write("\nSTEP 2: Create NumericObject Object\n", 3)
				

		info = NumericObject(action_data["value"], action_data["base"])

		info.calculateCustomBase(action_data["custom_base"])

		log.write(info, 8)

		log.write(ObjectJson.encode(info), 8)

		# this line is just a test to ensure that the decode function was working and for documentation
		# log.write(ObjectJson.decode(ObjectJson.encode(info)))

		if "bitshift_operation" in action_data:

			# then perform a bitshift operation on the Numericinfo object and display its new values
			is_bitshift = True

			log.write("\nSTEP 2.5: Detected bitshift request. Performing shift\n", 3)


			new_binary 				= NumericTool.shiftBinaryBits( info.base2, action_data["bitshift_operation"], action_data["bitshift_value"])

			shifted_number_info 	= NumericObject(new_binary, 10)

			shifted_number_info.calculateCustomBase(action_data["custom_base"])

			log.write(shifted_number_info, 8)

			log.write(ObjectJson.encode(shifted_number_info), 8)




		log.write("\nSTEP 3: Display Report in Pretty Format\n", 3)

		log.write("Original number", 1)
		log.write("BASE_2  : " + NumericTool.getFormattedNumber(info.base2, 2), 1)
		log.write("BASE_10 : " + NumericTool.getFormattedNumber(info.base10, 10), 1)
		log.write("BASE_16 : " + NumericTool.getFormattedNumber(info.base16, 16), 1)
		log.write("BASE_XX : " + NumericTool.getFormattedNumber(info.custom_value, info.custom_base), 1)


		log.write("\n--------------------\n", 1)

		if is_bitshift:


			origin_base2_string = NumericTool.getFormattedNumber(info.base2, 2, False)
			shifty_base2_string = NumericTool.getFormattedNumber(shifted_number_info.base2, 2, False)


			longer_string	= len(origin_base2_string)

			if longer_string < len(shifty_base2_string):

				longer_string = len(shifty_base2_string)

			padded_length = longer_string + (4 - longer_string % 4)


			origin_base2_string = NumericTool.addPadding(origin_base2_string, padded_length)
			shifty_base2_string = NumericTool.addPadding(shifty_base2_string, padded_length)

			log.write("Shifted number (by " + action_data["bitshift_operation"] + " " + str(action_data["bitshift_value"]) + ")" , 1)
			log.write("BASE_2  : " + NumericTool.getFormattedNumber(shifted_number_info.base2, 2), 1)
			log.write("BASE_10 : " + NumericTool.getFormattedNumber(shifted_number_info.base10, 10), 1)
			log.write("BASE_16 : " + NumericTool.getFormattedNumber(shifted_number_info.base16, 16), 1)
			log.write("BASE_XX : " + NumericTool.getFormattedNumber(shifted_number_info.custom_value, shifted_number_info.custom_base), 1)


			log.write("\n--------------------\n", 1)

			log.write("Bitshift Comparison\n", 1)

			log.write("original : " + origin_base2_string, 1)
			log.write("direction: " + action_data["bitshift_operation"] +" "+ str(action_data["bitshift_value"]) + " " + action_data["bitshift_operation"], 1)
			log.write("aftermath: " + shifty_base2_string, 1)

	log.write("\ndone!\n", 1)

	log.close()
	exit(1)





def getDeserializedArgs(args):

	action_data = {"base":10, "custom_base":0 ,"value":0}

	for index, arg in enumerate(args):

		arg_lower = arg.lower()

		if arg_lower == "-b" or arg_lower == "--base":
			action_data["base"] = int(args[ (index+1) ])

		if arg_lower == "-c" or arg_lower == "--custom-base":
			action_data["custom_base"] = int(args[ (index+1) ], 10)

		if arg_lower == "-v" or arg_lower == "--value":
			action_data["value"] = args[ (index+1) ]

		if arg_lower == "-l" or arg_lower == "--left" or arg_lower == "-ls" or arg_lower == "--left-shift":
			action_data["bitshift_operation"] 	= "<<"
			action_data["bitshift_value"] 		= int(args[ (index+1) ])

		if arg_lower == "-r" or arg_lower == "--right" or arg_lower == "-rs" or arg_lower == "--right-shift":
			action_data["bitshift_operation"] 	= ">>"	
			action_data["bitshift_value"] 		= int(args[ (index+1) ])

		if arg_lower == "-urs" or arg_lower == "--unsigned-right-shift" or arg_lower == "-ur" or arg_lower == "--rrr" or arg_lower == "--rrs":
			action_data["bitshift_operation"] 	= ">>>"
			action_data["bitshift_value"] 		= int(args[ (index+1) ])

	return action_data



Main(sys.argv)
