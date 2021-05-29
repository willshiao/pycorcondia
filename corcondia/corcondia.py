import tensorly as tl
from tensorly.tenalg import mode_dot
from tensorly.decomposition import parafac
import numpy as np

def kronecker_mat_ten(matrices, X):
    for k in range(len(matrices)):
        M = matrices[k]
        X = mode_dot(X, M, k)
    return X

def corcondia(X, k = 1, init='random', **kwargs):
    weights, X_approx_ks = parafac(X, k, init=init, **kwargs)

    A, B, C = X_approx_ks
    x = tl.cp_to_tensor((weights, X_approx_ks))

    Ua, Sa, Va = np.linalg.svd(A)
    Ub, Sb, Vb = np.linalg.svd(B)
    Uc, Sc, Vc = np.linalg.svd(C)

    SaI = np.zeros((Ua.shape[0], Va.shape[0]), float)
    np.fill_diagonal(SaI, Sa)

    SbI = np.zeros((Ub.shape[0], Vb.shape[0]), float)
    np.fill_diagonal(SbI, Sb)

    ScI = np.zeros((Uc.shape[0], Vc.shape[0]), float)
    np.fill_diagonal(ScI, Sc)

    SaI = np.linalg.pinv(SaI)
    SbI = np.linalg.pinv(SbI)
    ScI = np.linalg.pinv(ScI)

    part1 = kronecker_mat_ten([Ua.T, Ub.T, Uc.T], x)
    part2 = kronecker_mat_ten([SaI, SbI, ScI], part1)
    G = kronecker_mat_ten([Va.T, Vb.T, Vc.T], part2)

    T = np.zeros((k, k, k))
    for i in range(k):
        T[i,i,i] = 1

    return 100 * (1 - ((G-T)**2).sum() / float(k))
