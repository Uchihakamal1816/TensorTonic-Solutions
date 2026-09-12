import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    x=np.asarray(X)
    xc=X-np.mean(x,axis=0)
    n=len(x)
    covar=(xc.T@xc)
    covar=covar/(n-1)
    return covar
    
    