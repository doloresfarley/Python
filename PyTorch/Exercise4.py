import torch

input_tensor = torch.tensor([[1.0, -6.0, 2.5, -0.3, 1.2, 0.8]])


# Create a sigmoid function and apply it on input_tensor
sigmoid = torch.nn.Sigmoid()  # Using nn.Sigmoid module

softmax = torch.nn.Softmax(dim=-1)
probability = softmax(input_tensor)
print(probability)
