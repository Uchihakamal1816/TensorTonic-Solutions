import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    var=float(p*(1-p))
    a=np.asarray([1-p if i==0 else p for i in x])
    
    return{"pmf":a,"mean":float(p),"variance":var}
    