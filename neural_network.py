import torch
from torch import nn

# Training data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])

y = torch.tensor([[3.0], [5.0], [7.0], [9.0], [11.0]])

print(X)
print(y)

# Create neural network
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer = nn.Linear(1, 1)

    def forward(self, x):
        return self.layer(x)


model = MyModel()

print(model)