

"""keras-ocr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mBIzzB2Wa7hs8FOSeRmFyXBa7c1IEwuu

Documentation:
https://keras-ocr.readthedocs.io/en/latest/

Based on: https://github.com/clovaai/CRAFT-pytorch
"""

# !pip install keras-ocr

import keras_ocr
from matplotlib import pyplot as plt

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# List of three example images
images = [keras_ocr.tools.read(img) for img in ['/content/drive/My Drive/Colab Notebooks/data/billboard1.jpg',
                                               '/content/drive/My Drive/Colab Notebooks/data/billboard2.jpg',
                                                '/content/drive/My Drive/Colab Notebooks/data/handwritten.jpg'
                                               ]
]

#Print shape...
import numpy as np
print(np.shape(images))

# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
prediction_groups = pipeline.recognize(images)

# Plot the predictions
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)