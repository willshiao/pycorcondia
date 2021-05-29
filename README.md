# pycorcondia
[![](https://img.shields.io/pypi/v/corcondia.svg)](https://pypi.org/pypi/corcondia/)

CORCONDIA (Core Consistency Diagnostic) implementation in Python. It uses Tensorly with the Numpy backend.

## Installation

```bash
pip install -U corcondia
```

## Usage

Currently, the only implemented function is `corcondia_3d`, which calculates the Core Consistency Diagnostic (CORCONDIA) for a 3D tensor. Additional arguments will be forwarded to the [`tensorly.decomposition.parafac`](http://tensorly.org/stable/modules/generated/tensorly.decomposition.parafac.html#tensorly.decomposition.parafac) call.

An example on a random tensor is shown below.

```python3
import numpy as np
from corcondia import corcondia_3d

X = np.random.rand(5, 5, 5)
print(corcondia_3d(X, k=3))
```

## References

This is based off of the original MATLAB implementation by Evangelos (Vagelis) Papalexakis:

```
@inproceedings{inproceedings,
author = {Papalexakis, Evangelos and Faloutsos, Christos},
year = {2015},
month = {04},
pages = {5441-5445},
title = {Fast efficient and scalable Core Consistency Diagnostic for the parafac decomposition for big sparse tensors},
doi = {10.1109/ICASSP.2015.7179011}
}
```

CORCONDA was first introduced by Bro and Kiers (2003) [here](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/cem.801).

Thanks to Alessandro Bessi for his initial implementation [here](https://github.com/alessandrobessi/corcondia), which led to the creation of this repo.

Also, thanks to Yorgos Tsitsikas for his valuable feedback and suggestions.
