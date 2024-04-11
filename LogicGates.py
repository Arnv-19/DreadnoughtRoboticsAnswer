import numpy as np

# Define the gate diagram
inputs = np.array([[1, 0, 0], 
                   [1, 0, 1], 
                   [1, 1, 0], 
                   [1, 1, 1]])
outputs = np.array([0, 1, 1, 0])

# Initialize the perceptron weights
weights = np.zeros(3)

# Implement the perceptron learning algorithm
learning_rate = 0.1
num_epochs = 100

for epoch in range(num_epochs):
    for i in range(len(inputs)):
        prediction = np.sign(np.dot(inputs[i], weights))
        error = outputs[i] - prediction
        weights += learning_rate * error * inputs[i]

# Test the perceptron
for i in range(len(inputs)):
    prediction = np.sign(np.dot(inputs[i], weights))
    print(f"Input: {inputs[i]}, Output: {prediction}")