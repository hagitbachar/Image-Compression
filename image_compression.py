from numpy import diag, zeros, dot
from numpy.linalg import svd, norm
from matplotlib.pyplot import *
import scipy.misc as misc

MATRIX_LEN = 512

ascent = misc.ascent()
u, s, v = svd(ascent)

n = MATRIX_LEN
zeroM = zeros((MATRIX_LEN, MATRIX_LEN))
compress_ratio_array = []
frobenius_distance_array = []

for k in range(0, 511):
    if k != 0:
        zeroM[k -1][k -1] = s[k - 1]
    uzero = dot(u, zeroM)
    compress_matrix = dot(uzero, v)
    compress_ratio_array.append(1- (2*n*k + k)/(2*n**2 + n))
    frobenius_distance_array.append(norm(ascent - compress_matrix))
    if(k==2 or k==30 or k==60 or k==100 or k==510):
        imshow(compress_matrix)
        title(str(k) + " iterations")
        show()
plot(compress_ratio_array)
xlabel("k")
ylabel("compress ratio")
title("compress ratio")
show()
plot(frobenius_distance_array)
xlabel("k")
ylabel("frobenius distance")
title("frobenius distance")

show()
