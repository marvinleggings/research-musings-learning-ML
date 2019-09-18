# Blurb

It seems that the basis of a feed-forward neural network is a single layer perceptron. This at its most basic consists of input values which are then multiplied by weights and these values are passed into what is effectively a summing junction. The outputs can be calculated using simple matrix algebra, and then passed through an activation function. 

For a simple example the activation could be a peice wise defined a threshold. 

![equation](https://latex.codecogs.com/gif.latex?f%28x%29%20%3D%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%201%20if%20x%3E0%20%5C%5C%200%20otherwise%20%5Cend%7Bmatrix%7D%5Cright.)

This is ofcourse a step function very familiar to anyone who has studied control or related systems theory.

## Training the SLP 

We must now use a training set which has input corresponding to outputs and we can use the error or difference from the predicted output and the desired output to update the weights and cycle through this until we have reached a satisfactory result or decided that the model will not train. 

