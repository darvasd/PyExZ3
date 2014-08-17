# Daniel Darvas, 2014.

# Note that the dictionary is not an input!
def dicttest1(in1):
    dict_d = {123 : 0}
    dict_d[in1] = 1
	
    if dict_d[123] > 0:
		# If in1==123, this branch will be executed.
        return 1
    else:
        return 2
        
    
def expected_result():
    return [1,2]