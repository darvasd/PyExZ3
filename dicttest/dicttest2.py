# Daniel Darvas, 2014.

def dicttest2(dict_in, in1):
	if dict_in[in1] == None:
		# in1 is not found in the dictionary
		if in1 > 0:
			# not found and positive
			return 1
		else:
			# not found and non-positive
			return -1
	else:
		# in1 is in the dictionary
		if in1 > 0:
			# found and positive
			return 2
		else:
			# found and non-positive
			return -2
		
	
def expected_result():
	return [-1,1,2,-2]