from numpy import exp, array, random, dot
inp_array = list()

otp_array = list()

for i in range(0,3):
    
	n = raw_input()
    
	inp_array.append(int(n))
    


training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])

training_set_outputs = array([[0, 1, 1, 0]]).T



random.seed(1)

synaptic_weights = 2 * random.random((3, 1)) - 1



for iteration in xrange(20000):
    
	output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    
	synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    


otp_array = 1 / (1 + exp(-(dot(inp_array, synaptic_weights))))


print ('The output for', inp_array)

print ('is -> ', int(round(otp_array)))
