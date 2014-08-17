def powtest(in1):
    if in1*in1 == 0:
        return 1
    elif in1*in1 > 0:
        return 2
		
	# This should be impossible, as the square of a real number cannot be negative.
	# However, because in this implementation Z3 works with bitvectors, this is possible.
	# PyExZ3 will check if the model given by Z3 is real (executable), but it will cause a looong execution.
	# If we would use Int, an unsat could be given for And(Not(in1*in1 == 0),Not(in1*in1 > 0)).
    return 0

def expected_result():
    return [1,2]