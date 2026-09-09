import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    x=np.asarray(a)
    y=np.asarray(b)
    a2=np.linalg.norm(x)
    b2=np.linalg.norm(y)
    if a2==0 or b2 ==0:
        return 0.0
    return float(np.dot(x,y)/(a2*b2))