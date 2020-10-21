import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

class ML_network(nn.Module):
    def __init__(self):
        nn.Conv2d = nn.Conv2d(32, 32, 3, 1)
    
    def forward(self, x):
        print("kjsk")
        return x