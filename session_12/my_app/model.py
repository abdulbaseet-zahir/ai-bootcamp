import torch
import torch.nn as nn


# Simple Model architecture
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        return self.fc2(torch.relu(self.fc1(x)))
