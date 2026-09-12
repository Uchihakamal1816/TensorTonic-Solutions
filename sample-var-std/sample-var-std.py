import numpy as np
import math
def sample_var_std(x: list) -> dict:
    a=np.asarray(x)
    b=np.mean(x)
    c=a-b
    var=float(np.sum(c**2)/(a.size-1))
    dev=float(math.sqrt(var))
    return {"variance":var,"standard_deviation":dev}
    
    