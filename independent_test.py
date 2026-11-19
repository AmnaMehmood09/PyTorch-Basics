import torch
from torch import nn

data = torch.tensor([20, 15, 30, 45, 60])

number = torch.zeros(2, 4)

task = torch.rand(3, 2)
print(data)
print(task)
print(number)
print(data.float().mean())
print(data.sum())