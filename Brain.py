# import the necessary module for building neural network
import torch.nn as nn

# Define a neural network class by inheriting the nn.Module class
class NeuralNetwork(nn.Module):

    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        # Define three fully connected layers with input_size, hidden_size, and num_classes number of neurons respectively
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        # Define ReLU activation function
        self.relu = nn.ReLU()

    def forward(self, x):
        # Define the forward pass of the neural network
        # Pass the input through first fully connected layer, and then apply the ReLU activation function
        out = self.l1(x)
        out = self.relu(out)
        # Pass the output of the previous layer through the second fully connected layer, and again apply the ReLU activation function
        out = self.l2(out)
        out = self.relu(out)
        # Pass the output of the previous layer through the third fully connected layer, and return the output
        out = self.l3(out)
        return out

