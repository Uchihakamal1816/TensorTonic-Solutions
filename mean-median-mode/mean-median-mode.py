from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    a=np.asarray(x)
    mean=np.mean(x)
    median=np.median(x)
    counter={}
    for i in a:
        counter[i]=counter.get(i,0)+1

    mode=min(counter,key=lambda x: (-counter[x],x))
    
    return {"mean":float(mean),"median":float(median),"mode":float(mode)}
        
        