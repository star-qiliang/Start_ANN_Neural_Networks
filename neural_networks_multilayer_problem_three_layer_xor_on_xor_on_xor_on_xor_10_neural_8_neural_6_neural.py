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
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1],

    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1],

    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],

    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],


    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],

    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],

    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],

    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]

    
])

# True output or targets for the XOR problem
y = np.array([
    [0],
    [1],
    [1],
    [0],
    [1],
    [0],
    [0],
    [1],

    [1],
    [0],
    [0],
    [1],
    [0],
    [1],
    [1],
    [0],


    [1],
    [0],
    [0],
    [1],
    [0],
    [1],
    [1],
    [0],

    [0],
    [1],
    [1],
    [0],
    [1],
    [0],
    [0],
    [1]



])

# Set a random seed for reproducibility
# np.random.seed(42)

# # Neural network parameters
input_neurons = 5      # Number of input features
hidden1_neurons = 10   # Number of neurons in the first hidden layer
hidden2_neurons = 8    # Number of neurons in the second hidden layer
hidden3_neurons = 6    # Number of neurons in the third hidden layer
output_neurons = 1     # Number of neurons in the output layer


# Initialize weights and biases with random values
W_hidden1 = np.random.uniform(low=-1.0, high=1.0, size=(input_neurons, hidden1_neurons))
b_hidden1 = np.random.uniform(low=-1.0, high=1.0, size=(1, hidden1_neurons))
W_hidden2 = np.random.uniform(low=-1.0, high=1.0, size=(hidden1_neurons, hidden2_neurons))
b_hidden2 = np.random.uniform(low=-1.0, high=1.0, size=(1, hidden2_neurons))
W_hidden3 = np.random.uniform(low=-1.0, high=1.0, size=(hidden2_neurons, hidden3_neurons))
b_hidden3 = np.random.uniform(low=-1.0, high=1.0, size=(1, hidden3_neurons))
W_output = np.random.uniform(low=-1.0, high=1.0, size=(hidden3_neurons, output_neurons))
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
# epochs = 100000  # Number of training iterations
# epochs = 1000000  # Number of training iterations

# Training loop
for epoch in range(epochs):
    # -------- Forward Propagation --------
    # Compute input for first hidden layer
    hidden1_input = np.dot(X, W_hidden1) + b_hidden1
    hidden1_output = sigmoid(hidden1_input)
    
    # Compute input for second hidden layer
    hidden2_input = np.dot(hidden1_output, W_hidden2) + b_hidden2
    hidden2_output = sigmoid(hidden2_input)
    
    # Compute input for third hidden layer
    hidden3_input = np.dot(hidden2_output, W_hidden3) + b_hidden3
    hidden3_output = sigmoid(hidden3_input)
    
    # Compute input for output neuron
    final_input = np.dot(hidden3_output, W_output) + b_output
    predicted_output = sigmoid(final_input)
    
    # -------- Compute the Error --------
    # Difference between actual output and network's prediction
    error = y - predicted_output
    
    # Step to help monitor training progress (using Mean Squared Error)
    mse = np.mean(np.square(error))
    
    # -------- Backpropagation --------
    # For the output layer, compute the delta/error term
    d_predicted_output = error * sigmoid_derivative(final_input)
    
    # Propagate error back into the third hidden layer
    error_hidden3_layer = d_predicted_output.dot(W_output.T)
    d_hidden3_layer = error_hidden3_layer * sigmoid_derivative(hidden3_input)
    
    # Propagate error back into the second hidden layer
    error_hidden2_layer = d_hidden3_layer.dot(W_hidden3.T)
    d_hidden2_layer = error_hidden2_layer * sigmoid_derivative(hidden2_input)
    
    # Propagate error back into the first hidden layer
    error_hidden1_layer = d_hidden2_layer.dot(W_hidden2.T)
    d_hidden1_layer = error_hidden1_layer * sigmoid_derivative(hidden1_input)
    
    # -------- Update Weights and Biases --------
    # Update for the output layer
    W_output += learning_rate * hidden3_output.T.dot(d_predicted_output)
    b_output += learning_rate * np.sum(d_predicted_output, axis=0, keepdims=True)
    
    # Update for the third hidden layer
    W_hidden3 += learning_rate * hidden2_output.T.dot(d_hidden3_layer)
    b_hidden3 += learning_rate * np.sum(d_hidden3_layer, axis=0, keepdims=True)
    
    # Update for the second hidden layer
    W_hidden2 += learning_rate * hidden1_output.T.dot(d_hidden2_layer)
    b_hidden2 += learning_rate * np.sum(d_hidden2_layer, axis=0, keepdims=True)
    
    # Update for the first hidden layer
    W_hidden1 += learning_rate * X.T.dot(d_hidden1_layer)
    b_hidden1 += learning_rate * np.sum(d_hidden1_layer, axis=0, keepdims=True)
    
    # Optionally, print the error every 1000 epochs to monitor loss convergence
    if (epoch + 1) % 1000 == 0:
        print(f"Epoch {epoch+1}/{epochs}, Mean Squared Error: {mse}")

# -------- Final Prediction --------
print("\nFinal predictions after training:")
print(predicted_output)

# Convert prediction probabilities to binary outputs (using a threshold of 0.5)
print("\nBinary predictions (threshold=0.5):")
print((predicted_output > 0.5).astype(int))



print("\nW_hidden1:\n", W_hidden1)
print("\nb_hidden1:\n", b_hidden1)
print("\nW_hidden2:\n", W_hidden2)
print("\nb_hidden2:\n", b_hidden2)
print("\nW_hidden3:\n", W_hidden3)
print("\nb_hidden3:\n", b_hidden3)
print("\nW_output:\n", W_output)
print("\nb_output:\n", b_output)



print("\nTarget values:")
print(y)

print("\nComparing predictions with targets:")
predictions = (predicted_output > 0.5).astype(int)
correct = np.sum(predictions == y)
total = len(y)
accuracy = correct / total * 100

print(f"\nAccuracy: {accuracy}% ({correct}/{total} correct)")

# Display detailed comparison
print("\nDetailed comparison:")
print("Prediction\tTarget\tCorrect?")
print("-" * 40)
for pred, target in zip(predictions, y):
    is_correct = "✓" if pred == target else "✗"
    print(f"{pred[0]}\t\t{target[0]}\t{is_correct}")

