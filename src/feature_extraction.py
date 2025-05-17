import numpy as np

def combine_features(image_features, env_features):
    return np.hstack((image_features, env_features))