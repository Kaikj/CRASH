#Triple Modular Redundancy
#9/4/2016: assumes only flipping of bits, missing not accounted for i.e. missing bits require retransmission
#CONSTANTS
K = 3

#FUNCTIONS
#encode(input): takes in stream of bits and pads it to K bits for each bit with the bit itself
def encode(input):
	output = ""
	for x in str(input):
		output = output + x * K
	return output
	
#decode(input): takes in stream of bits, performs error correction by majority rule, returns the initial message
def decode(input):
	raw = input
	output = ""
	#if (len(raw) % 3) == 1:
	#	return -1
	while len(raw) >= 1:
		current = raw[0:K]
		if current == "111":
			output = output + '1'
			raw = raw[K:]
		elif current == "000":
			output = output + '0'
			raw = raw[K:]
		else:
			check = current.count('1', 0)
			if check == 2:
				output = output + '1'
				raw = raw[K:]
			else:
				output = output + '0'
				raw = raw[K:]
	return output
