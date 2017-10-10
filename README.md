JLT-for-dimension-reduction
Finish the JLT for dimension reduction by Gaussian random matrix and python.

the basic strcuture of whole program:
create a dataset with the customized size:
  dataset's size is N*n, N is the number of datapoints, n is the dimension of the original dataset
  each row of the dataset is a vector if data point with n features.
  each vector has the form as, (cosk, 1, 0, 0, ... ,0), k is the unformly distributed by [0,2\pi)
  
creat the Gaussian random matrix for projection matrix
each entry of this matrix is a Gaussian random variable ~ N(0,1)
  
JLT function

error of JLT
