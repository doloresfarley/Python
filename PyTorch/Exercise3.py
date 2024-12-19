import torch

input_tensor = torch.tensor([[0.8]])

# Create a sigmoid function and apply it on input_tensor


# Create a sigmoid function and apply it on input_tensor
sigmoid = torch.nn.Sigmoid()  # Using nn.Sigmoid module
probability = sigmoid(input_tensor)

print(probability)
