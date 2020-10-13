import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import numpy as np
import json

with open("config.json") as json_file:
    config = json.load(json_file)




print(config['cuda']['use_cuda'])