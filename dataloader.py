import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import numpy as np
import mnist
import json

with open("config.json") as json_file:
    config = json.load(json_file)

train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('/files/', train=True, download=True,
    transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.1307), (0.3081))
    ])),
    batch_size=config['train_batch_size'], shuffle=True)

test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('/files/', train=False, download=True,
    transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.1307), (0.3081))
    ])),
    batch_size=config['test_batch_size'], shuffle=True)

def get_dataloader(self, train=True):
    if(train == True):
        return train_loader
    else:
        return test_loader

examples = enumerate(test_loader)
batch_idx, (data, labels) = next(examples)