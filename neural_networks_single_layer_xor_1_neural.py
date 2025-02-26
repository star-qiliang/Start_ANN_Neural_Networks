"""
I want to learn neural networks from very basics.

Can you please give me python code step by step that I can write a neural network using numpy and python?



"""

"""
A step-by-step implementation of a simple neural network using NumPy.

This network is designed to solve the XOR problem:
    Input:  [0, 0] -> Expected Output: [0]
            [0, 1] -> Expected Output: [1]
            [1, 0] -> Expected Output: [1]
            [1, 1] -> Expected Output: [0]

The neural network consists of:
    - An input layer of 2 neurons (for the two features).
    - A hidden layer of 2 neurons.
    - An output layer of 1 neuron.

Each neuron's activation is computed using the sigmoid function.
"""

import numpy as np

# Define the Sigmoid activation function and its derivative
def sigmoid(x):
    """Compute the sigmoid of x."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Compute the derivative of the sigmoid function."""
    sx = sigmoid(x)
    return sx * (1 - sx)

# XOR dataset
# Each row is a sample with 2 features
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# True output or targets for the XOR problem
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Set a random seed for reproducibility
np.random.seed(42)

# Neural network parameters
input_neurons = 2      # Number of input features
hidden_neurons = 1     # Number of neurons in the hidden layer
output_neurons = 1     # Number of neurons in the output layer


# input_neurons = 2      # Number of input features
# hidden_neurons = 2     # Number of neurons in the hidden layer
# output_neurons = 1     # Number of neurons in the output layer

# input_neurons = 2      # Number of input features
# hidden_neurons = 10     # Number of neurons in the hidden layer
# output_neurons = 1     # Number of neurons in the output layer


# input_neurons = 2      # Number of input features
# hidden_neurons = 10     # Number of neurons in the hidden layer
# output_neurons = 1     # Number of neurons in the output layer


# Initialize weights and biases with random values
W_hidden = np.random.uniform(low=-1.0, high=1.0, size=(input_neurons, hidden_neurons))
b_hidden = np.random.uniform(low=-1.0, high=1.0, size=(1, hidden_neurons))
W_output = np.random.uniform(low=-1.0, high=1.0, size=(hidden_neurons, output_neurons))
b_output = np.random.uniform(low=-1.0, high=1.0, size=(1, output_neurons))

# Hyperparameters
learning_rate = 0.1
# epochs = 10  # Number of training iterations
# epochs = 100  # Number of training iterations
# epochs = 1000  # Number of training iterations
# epochs = 2000  # Number of training iterations
# epochs = 3000  # Number of training iterations
# epochs = 4000  # Number of training iterations
# epochs = 5000  # Number of training iterations
# epochs = 7000  # Number of training iterations
# epochs = 10000  # Number of training iterations
epochs = 50000  # Number of training iterations
# epochs = 1000000  # Number of training iterations

# Training loop
for epoch in range(epochs):
    # -------- Forward Propagation --------
    # Compute input for hidden layer neurons
    hidden_input = np.dot(X, W_hidden) + b_hidden
    hidden_output = sigmoid(hidden_input)
    
    # Compute input for output neuron
    final_input = np.dot(hidden_output, W_output) + b_output
    predicted_output = sigmoid(final_input)
    
    # -------- Compute the Error --------
    # Difference between actual output and network's prediction
    error = y - predicted_output
    
    # Step to help monitor training progress (using Mean Squared Error)
    mse = np.mean(np.square(error))
    
    # -------- Backpropagation --------
    # For the output layer, compute the delta/error term
    d_predicted_output = error * sigmoid_derivative(final_input)
    
    # Propagate error back into the hidden layer
    error_hidden_layer = d_predicted_output.dot(W_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_input)
    
    # -------- Update Weights and Biases --------
    # Update for the output layer
    W_output += learning_rate * hidden_output.T.dot(d_predicted_output)
    b_output += learning_rate * np.sum(d_predicted_output, axis=0, keepdims=True)
    
    # Update for the hidden layer
    W_hidden += learning_rate * X.T.dot(d_hidden_layer)
    b_hidden += learning_rate * np.sum(d_hidden_layer, axis=0, keepdims=True)
    
    # Optionally, print the error every 1000 epochs to monitor loss convergence
    if (epoch + 1) % 1000 == 0:
        print(f"Epoch {epoch+1}/{epochs}, Mean Squared Error: {mse}")

# -------- Final Prediction --------
print("\nFinal predictions after training:")
print(predicted_output)

# Convert prediction probabilities to binary outputs (using a threshold of 0.5)
print("\nBinary predictions (threshold=0.5):")
print((predicted_output > 0.5).astype(int))



print("\nW_hidden:\n", W_hidden)
print("\nb_hidden:\n", b_hidden)
print("\nW_output:\n", W_output)
print("\nb_output:\n", b_output)

