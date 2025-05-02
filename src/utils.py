def set_random_seed(seed: int) -> None:
    import random
    import numpy as np
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def load_config(config_path: str) -> dict:
    import json

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config