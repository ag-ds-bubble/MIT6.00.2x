# Problem Set 4
### Problem 2: R^2

### After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained by the model.

### Implement the function r_squared. This function will take in:

### list, y, that represents the y-coordinates of the original data samples estimated, which is a corresponding list of y-coordinates estimated from the regression model

### This function should return the computed R^2 value. You can compute R^2 as follows, where ei is the estimated y value for the i-th data point (i.e. predicted by the regression), yi is the y value for the ith data point, and mean is the mean of the original data samples.


R2=1−∑ni=1(yi−ei)2∑ni=1(yi−mean)2

### If you are still confused about R^2 , its wikipedia page has a good explanation 
about its use/how to calculate it.

```py
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV
```

