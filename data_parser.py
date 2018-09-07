import os
import urllib.request

def download_data():
	if (not os.path.isdir('./data')):
		os.makedirs('./data/train')
		os.makedirs('./data/test')
		urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz', './data/train/train-images.gz')
		urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz', './data/train/train-labels.gz')
		urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz', './data/test/test-images.gz')
		urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz', './data/test/test-labels.gz')
