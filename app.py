from flask import Flask
from flask import Flask, render_template
import io
from acgan.ACGAN import *
import torch
import torchvision
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import base64

app = Flask(__name__)


def generate():
    latent_dim = 100
    num_classes = 10
    batch_size = 16

    generator = Generator(latent_dim + num_classes)
    generator.load_state_dict(torch.load('./acgan/generator.pth', map_location=torch.device('cpu')))
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

@app.route('/generate')
def refresh_generate():
    gen_imgs = generate()
    gen_imgs = gen_imgs / 2 + 0.5
    
    plt.imshow(np.transpose(gen_imgs, (1, 2, 0)))
    plt.axis('off')
    
    data = io.BytesIO()
    plt.savefig(data, format='png')
    img_stream = base64.b64encode(data.getvalue()).decode()
    return render_template('generate.html',
                           img_stream=img_stream)

@app.route('/')
def hello():
    """return an HTTP greeting and show code rain."""
    return "Welcome to GAN playground, please go to /generate to generate image"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
