from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read() 

setup(
    name="tensorflow-plugins",
    version="0.1",
    description="Demo how Optimizers, Models, Loss functins, etc. might be grouped",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["tf_plugins"],
    install_requires=[
        "tensorflow~=2.5",
    ],
    entry_points="""
        [tensorflow.optimizers]
        Adadelta = tensorflow.keras.optimizers:Adadelta
        Adagrad = tensorflow.keras.optimizers:Adagrad
        Adam = tensorflow.keras.optimizers:Adam
        Adamax = tensorflow.keras.optimizers:Adamax
        Ftrl = tensorflow.keras.optimizers:Ftrl
        SGD = tensorflow.keras.optimizers:SGD
        Nadam = tensorflow.keras.optimizers:Nadam
        RMSprop = tensorflow.keras.optimizers:RMSprop

        [tensorflow.layers]
        AbstractRNNCell = tensorflow.python.keras.layers.recurrent:AbstractRNNCell
        RNN = tensorflow.python.keras.layers.recurrent:RNN
        SimpleRNN = tensorflow.python.keras.layers.recurrent:SimpleRNN
        SimpleRNNCell = tensorflow.python.keras.layers.recurrent:SimpleRNNCell
        StackedRNNCell = tensorflow.python.keras.layers.recurrent:StackedRNNCell
    """ 
)
