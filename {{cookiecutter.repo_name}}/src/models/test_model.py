import os
import sys

# add the 'src' directory as one where we can import modules
project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
src_dir = os.path.join(project_dir, "src")
sys.path.append(src_dir)

from data.make_dataset import *
from vis.visualize import *
from models.train_model import *
