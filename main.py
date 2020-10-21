import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import json

from dataloader import get_dataloader
import nettverk

with open("config.json") as json_file:
    config = json.load(json_file)

_nettverk = nettverk()


# print("\n\n\n" + batch_idx + "\n\n\n")