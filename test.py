import torch
import numpy as np

w = np.array([[2,3,4,5],[1,2]])
print(w.shape())
w = torch.FloatTensor(w)
print(w)
w = torch.unsqueeze(w,0)
print(w)