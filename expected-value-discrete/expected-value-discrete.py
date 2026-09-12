import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    a=np.asarray(x)
    b=np.asarray(p)
    c=np.sum(float(np.dot(a,b)))
    return c
    
    