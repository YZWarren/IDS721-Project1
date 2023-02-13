import torch
import torchvision

import numpy as np
from src.acgan.ACGAN import *

def generate():
    latent_dim = 100
    num_classes = 10
    batch_size = 16

    generator = Generator(latent_dim + num_classes)
    generator.load_state_dict(torch.load('src/acgan/generator.pth', map_location=torch.device('cpu')))
    generator.eval()

    label = np.random.randint(0, 9)
    z = torch.randn(batch_size, latent_dim)
    gen_class = np.random.randint(label, label+1, batch_size)
    z_labels = torch.zeros(batch_size, num_classes)
    z_labels[np.arange(batch_size), gen_class] = 1.0
    z = torch.concat((z, z_labels), 1)
    gen_class = torch.from_numpy(gen_class).type(torch.LongTensor)

    gen_imgs = generator(z).detach()
    return torchvision.utils.make_grid(gen_imgs, nrow=4).numpy()
