import numpy as np
import scipy as sp
# This is a comment

weights = {'node_0_0': np.array([2,4]),
           'node_0_1': np.array([4, -5]),
           'node_1_0': np.array([-1, 1]),
           'node_1_1': np.array([2, 2]),
           'output': np.array([2, 7])}

def relu(x):
    return max(0, x)

def predict_with_network(input_data, weights):
    node_0_0_input = (input_data * weights['node_0_0']).sum()
    node_0_0_output = relu(node_0_0_input)
    node_0_1_input = (input_data * weights['node_0_1']).sum()
    node_0_1_output = relu(node_0_1_input)
    hidden_0_outputs = np.array([node_0_0_output, node_0_1_output])
    node_1_0_input = (hidden_0_outputs * weights['node_1_0']).sum()
    node_1_0_output = relu(node_1_0_input)
    node_1_1_input = (hidden_0_outputs * weights['node_1_1']).sum()
    node_1_1_output = relu(node_1_1_input)
    hidden_1_outputs = np.array([node_1_0_output, node_1_1_output])
    model_output = (hidden_1_outputs * weights['output']).sum()
    return model_output

input_data = np.array([3, 5])
print(predict_with_network(input_data, weights))