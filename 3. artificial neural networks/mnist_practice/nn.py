'''
Neural Network for mnist 

Author : Sangkeun Jung (2019)
'''

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

class mlp(nn.Module):
    def __init__(self):
        super(mlp, self).__init__()

        """
        Implement this part (network design part)
        !! this part is conducted only one time in the initialization step

        3 layer fully connected networks

        512 --> 256 --> 10
        """

    def forward(self, x):

        """
        Implement this part (forward calculation)

        This part will be called every parameter update

        1) activation function : relu
        2) do not activate the final value
        """
        return x # <-- x will be the final value 
    
    def name(self):
        return "mlp"