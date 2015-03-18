# this needs to be tested and stressed. I will ultimately need a base converter that exceeds the typical int and long variable sizes

'''
aybe this shouldn't be an answer, but it could be helpful for some: the built-in format function does convert numbers to string in a few bases:

>>> format(255, 'b') # base 2
'11111111'
>>> format(255, 'd') # base 10
'255'
>>> format(255, 'o') # base 8
'377'
>>> format(255, 'x') # base 16
'ff'


A function has "constant" growth if its output does not change based on the input, the n. The easy way to identify constant functions is find those that have no n in their expression anywhere, or have n
​0
​​ . In this case, 1 and 1000 are constant.
A function has "linear" growth if its output increases linearly with the size of its input. The way to identify linear functions is find those where n is never raised to a power (although n
​1
​​ is OK) or used as a power. In this case, 3n and (3/2)n are linear.
A function has "polynomial" growth if its output increases according to a polynomial expression. The way to identify polynomial functions is to find those where n is raised to some constant power. In this case, 2n
​3
​​  and 3n
​2
​​  are polynomial.
A function has "exponential" growth if its output increases according to an exponential expression. The way to identify exponential functions is to find those where a constant is raised to some expression involving n. In this case, 2
​n
​​  and (3/2)
​n
​​  are exponential.



Within the logarithmic functions, the lesser bases grow more quickly than the higher bases - so log
​2
​​ n will grow more quickly than log
​8
​​ n.



The linearithmic functions are those that multiply linear terms by a logarithm, of the form nlog
​k
​​ n. With the n being the same in both, then the growth is dependent on the base of the logarithms. And as we just stated, the lesser bases grow more quickly than the higher bases - so nlog
​2
​​ n will grow more quickly than nlog
​6
​​ n. 


'''

import math


class NumericTool:

	@staticmethod
	def byteToBits(int_byte): # Convert a positive number (num) to its digit representation in base (base).
		
		bits = []

		while int_byte > 0:

			bits.insert(0, int_byte % 2)

			int_byte  = int_byte // 2 # integer division


		while len(bits) < 8:
			bits.insert(0, 0)

		return bits

	@staticmethod
	def toDigits(num, base): # Convert a positive number (num) to its digit representation in base (base).
		
		digits = []

		if base > 0:

			while num > 0:

				digits.insert(0, num % base)

				num  = num // base # integer division

		return digits


	@staticmethod
	def fromDigits(digits, base): # Compute the number given by digits in base base.

	    n = 0

	    for d in digits:

	        n = base * n + d

	    return n


	@staticmethod
	def shiftBinaryBits(binary_value, shift_type=">>>", shift_amount=1):

		new_binary = []

		if shift_type == "<<":

			new_binary = list( str( int(''.join(map(str, binary_value)), 2) << shift_amount) )

		if shift_type == ">>":

			new_binary = list( str( int(''.join(map(str, binary_value)), 2) >> shift_amount) )

		#if shift_type == ">>>": # does not work in python for some reason
			#new_binary = list( str( int(''.join(map(str, binary_value)), 2) >>> shift_amount) )



		new_binary = list(map(int, new_binary))

		return new_binary

	@staticmethod
	def getFormattedNumber(number, base, use_special_formatting= True):

		symbols 		= ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Չ')

		formated_number = ''

		if base <= len(symbols):

			for i, n in reversed(list(enumerate(number))):

				formated_number = symbols[n] + formated_number

				if use_special_formatting and base == 2:

					regular_iteration = int(len(number) - i)

					#print(regular_iteration, n)

					if regular_iteration % 4 == 0 and regular_iteration > 2: # adda  space for every 4 characters
						formated_number = ' ' + formated_number


		elif base <= 55296:

			for i, n in reversed(list(enumerate(number))):

				formated_number = chr(n) + formated_number

				if use_special_formatting and base == 2:

					regular_iteration = int(len(number) - i)

					#print(regular_iteration, n)

					if regular_iteration % 4 == 0 and regular_iteration > 2: # adda  space for every 4 characters
						formated_number = ' ' + formated_number

		else:
			print("FATAL: NumericTool only supports formatted conversions up to "+str(len(symbols))+" symbols. Your request for base "+str(base)+" cannot be converted without adding support in the NumericTool code.")


		return formated_number

	def addPadding(numeric_string, padding, use_spaced_format=True):

		formated_number = numeric_string

		if len(formated_number) < padding:

			for i in range(padding - len(formated_number)):

				formated_number = "0" + formated_number


		if use_spaced_format:
			formated_number = ' '.join(formated_number[i:i+4] for i in range(0, len(formated_number), 4))

		return formated_number


	@staticmethod
	def getSquareNumbersRange(range_min, range_max):

		import time
		start_time = time.time()

		squares = [[num, (num**0.5)] for num in range(range_min, range_max+1) if (num**0.5) % 1 == 0]

		print(squares)

		end_time	= time.time()

		print("run_time:", end_time - start_time)

	@staticmethod
	def getNumericMedian(a_list):

		length 			= len(a_list)

		center_index 	= math.floor(length/2)

		if length % 2 == 0:
			# then even number. set median to average of the two center numbers

			return sum(a_list[center_index-1:center_index+1]) / 2
		else:

			return a_list[center_index]


	@staticmethod
	def getNumericListMetaData(list_of_numbers):

		list_of_numbers.sort()

		length		= len(list_of_numbers)

		list_sum 	= sum(list_of_numbers)
		list_min 	= min(list_of_numbers)
		list_max	= max(list_of_numbers)
		list_range	= list_max - list_min
		list_mean	= list_sum / length
		list_median	= NumericTool.getNumericMedian(list_of_numbers)
		list_mode	= "--"
		list_mad 	= sum([abs(list_mean-num) for num in list_of_numbers]) / length

		center_index= math.floor(length/2)

		if length % 2 == 0:

			list_even	= "even"

			left_bw 	= NumericTool.getNumericMedian(list_of_numbers[:center_index])
			right_bw	= NumericTool.getNumericMedian(list_of_numbers[center_index:])
		else:

			list_even	= "odd"

			left_bw 	= NumericTool.getNumericMedian(list_of_numbers[:center_index])
			right_bw	= NumericTool.getNumericMedian(list_of_numbers[center_index+1:])




		print("RAW:\t", list_of_numbers)
		print("count:\t", list_even, length, "\n\n")
		print("Min:\t", list_min)
		print("Max:\t", list_max)
		print("Sum:\t", list_sum)
		print("Range:\t", list_range)
		print("Mean:\t", list_mean)
		print("Median:\t", list_median)
		print("Mode:\t", list_mode)
		print("M.A.D:\t", list_mad)

		print("B & W:\t", left_bw, list_median, right_bw)

		#print("TEST EVEN:\t", center_index, list_of_numbers[:center_index], list_of_numbers[center_index:])
		#print("TEST ODD:\t", center_index, list_of_numbers[:center_index], list_of_numbers[center_index+1:])


	@staticmethod
	def terminalDraw(size):

		import os
		rows, columns = os.popen('stty size', 'r').read().split()

		test_square = "...TEST...\n"  # ["0" for count in range(1,size)]

		for i in range(0, size):

			test_square += "\n".join(["0" for count in range(0,size)])

		print(test_square)