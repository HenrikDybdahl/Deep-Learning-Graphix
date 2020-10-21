import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import numpy as np
import json

import nettverk

with open("config.json") as json_file:
    config = json.load(json_file)

_nettverk = nettverk()


print(config['cuda']['use_cuda'])