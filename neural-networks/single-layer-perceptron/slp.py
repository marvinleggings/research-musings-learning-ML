import numpy as np

#Single layer perceptron consists of
#x inputs and y outputs
#KISS - 2 inputs - 1 output

class SingleLayerPerceptron:
	inputs = [[0,0],[0,1],[1,0],[1,1]]
	desired_outputs = [0,0,0,1]
	def __init__(self, no_of_inputs,bias, epochs=1000, learning_rate=0.01):
		self.epochs = epochs
		self.learning_rate = learning_rate
		self.bias=bias
		self.weights = np.zeros(no_of_inputs)

	def activation(self, x):
		if x > 0:
			return 1
		else:
			return 0

	def predict(self, inputs):
		for a in inputs:
			input_matrix = a
			weights_matrix = np.asarray(self.weights)
			output = self.activation(np.dot(input_matrix, weights_matrix) + self.bias)
			print(output)

	def train(self):
		for i in range(self.epochs):
			for iteration, a in enumerate(self.inputs):
				input_matrix = np.asarray(a)
				weights_matrix = np.asarray(self.weights)
				output = self.activation(np.dot(input_matrix, weights_matrix) + self.bias)
				self.weights = (weights_matrix + self.learning_rate*(self.desired_outputs[iteration]-output)*input_matrix)
				self.bias = self.learning_rate*(self.desired_outputs[iteration]-output)
	

test = SingleLayerPerceptron(2,1)

# test.inputs=[1,2]
# test.weights=[1,0]

test.train()
test.predict([[0,0],[0,1],[1,0],[1,1]])