def transfer(in1):
	b = (-1 * in1)
	c = b + 5
	d = b + c 
	if d < 0:
		return 1
	else:
		return 2

def expected_result():
	return [1,2] 