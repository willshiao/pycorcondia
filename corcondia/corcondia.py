import tensorly as tl
from tensorly.tenalg import mode_dot
from tensorly.decomposition import parafac
import numpy as np

def kronecker_mat_ten(matrices, X):
    for k in range(len(matrices)):
        M = matrices[k]
        X = mode_dot(X, M, k)
    return X

# Shortcut to invert singular values.
# Given a vector of singular values, returns the inverted matrix
def invert_sing(s):
    return np.diag(1.0 / s)

def corcondia_3d(X, k = 1, init='random', **kwargs):
    # Weights are not important since normalize_factors is false by default
    #  so the weights will be all ones.
    _, X_approx_ks = parafac(X, k, init=init, **kwargs)

    A, B, C = X_approx_ks
    Ua, Sa, Va = np.linalg.svd(A, full_matrices=False)
    Ub, Sb, Vb = np.linalg.svd(B, full_matrices=False)
    Uc, Sc, Vc = np.linalg.svd(C, full_matrices=False)

    inverted = [invert_sing(x) for x in (Sa, Sb, Sc)]

    part1 = kronecker_mat_ten([Ua.T, Ub.T, Uc.T], X)
    # TODO: line below can be omitted if we multiply the k-th column
    #  of Ua, Ub and Uc by the inverse of the corresponding k-th singular value, that is 1/σ_k.
    #  Then, the previous line will need to use the updated Ua, Ub and Uc
    # (note by Yorgos)
    part2 = kronecker_mat_ten(inverted, part1)
    G = kronecker_mat_ten([Va.T, Vb.T, Vc.T], part2)

    for i in range(k):
        G[:,:,i] = G[:,:,i] / G[i,i,i]

    T = np.zeros((k, k, k))
    for i in range(k):
        T[i,i,i] = 1

    return 100 * (1 - ((G-T)**2).sum() / float(k))
