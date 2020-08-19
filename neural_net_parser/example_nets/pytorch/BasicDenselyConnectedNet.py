import torch.nn as nn
import torch.nn.functional as F
import torch
### SOURCE: https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

"""
#Testing
Base = BasicNet(30)

input = torch.randn(1, 1, 28, 28) #nSamples * nChannels * Height * Width, MNIST
out = Base(input)
"""

class BasicNet(nn.Module):

    def __init__(self, num_classes = 10):
        super(BasicNet, self).__init__()
        # 1 input image channel, 6 output channels, 3x3 square convolution
        # kernel
        self.stuff = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=3),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(6, 16, kernel_size=3),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),
            ###pure fc layers below
            nn.Flatten(),
            nn.Linear(16*5*5, 120),
            nn.ReLU(inplace=True),
            nn.Linear(120, 84),
            nn.ReLU(inplace=True),
            nn.Linear(84, int(num_classes))
        )

    def forward(self, x):
        x = self.stuff(x)
        return x