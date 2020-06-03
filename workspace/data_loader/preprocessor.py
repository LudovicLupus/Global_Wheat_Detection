"""
To-do:

1) Use Pathlib library to create path objects for training/test data
"""
from pathlib import Path
import numpy as np
import pandas as pd
import cv2
import os

# Path to training data
TRAIN_DATA = Path.cwd() / "global-wheat-detection" / "train"    # Directory
# Path to test data
TEST_DATA = Path.cwd() / "global-wheat-detection" / "test"      # Directory
# Path to training annotations
TRAIN_LABELS = Path.cwd() / "global-wheat-detection" / "train.csv"  # CSV File
# Create dataframe with labels
labels = pd.read_csv(TRAIN_LABELS)

print(Path.cwd())
# # Load and view sample training image (first in TRAIN_DATA)
# # Reference faster_rcnn_simple.py (uses matplotlib)
# img = cv2.imread(str(TRAIN_DATA / os.listdir(TRAIN_DATA)[0]))
# # Output img with window name as 'image'
# cv2.imshow('wheat image (hopefully)', img)
# # Maintain output window until user presses a key
# cv2.waitKey(0)
# # Destroying present windows on screen
# cv2.destroyAllWindows()




