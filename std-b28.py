import numpy as np

Y = np.zeros((1080, 1920), 'uint16')
U = np.ones((1080, 1920), 'uint16') * 512
V = np.ones((1080, 1920), 'uint16') * 512

a = 1920
b = 1080
c = 206
d = 240
e = 206
f = 205
g = 411
h = 171
i = 69
j = 68
k = 309
m = 206

# Pattern 1
h1 = int(b*7/12)
Y[0:h1, 0:d] = 414   # 40% Gray
Y[0:h1, d:(d+f)] = 721    # 75% White
Y[0:h1, (d+f):(d+f+c)] = 674    # Yellow
Y[0:h1, (d+f+c):(d+f+c+c)] = 581    # Cyan
Y[0:h1, (d+f+c+c):(d+f+c+c+e)] = 534    # Green
Y[0:h1, (d+f+c+c+e):(d+f+c+c+e+c)] = 251    # Magenta
Y[0:h1, (d+f+c+c+e+c):(d+f+c+c+e+c+c)] = 204    # Red
Y[0:h1, (d+f+c+c+e+c+c):(d+f+c+c+e+c+c+f)] = 111    # Blue
Y[0:h1, (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 414    # 40% Gray

U[0:h1, 0:d] = 512   # 40% Gray
U[0:h1, d:(d+f)] = 512    # 75% White
U[0:h1, (d+f):(d+f+c)] = 176    # Yellow
U[0:h1, (d+f+c):(d+f+c+c)] = 589    # Cyan
U[0:h1, (d+f+c+c):(d+f+c+c+e)] = 253    # Green
U[0:h1, (d+f+c+c+e):(d+f+c+c+e+c)] = 771    # Magenta
U[0:h1, (d+f+c+c+e+c):(d+f+c+c+e+c+c)] = 435    # Red
U[0:h1, (d+f+c+c+e+c+c):(d+f+c+c+e+c+c+f)] = 848    # Blue
U[0:h1, (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 512    # 40% Gray

V[0:h1, 0:d] = 512   # 40% Gray
V[0:h1, d:(d+f)] = 512    # 75% White
V[0:h1, (d+f):(d+f+c)] = 543    # Yellow
V[0:h1, (d+f+c):(d+f+c+c)] = 176    # Cyan
V[0:h1, (d+f+c+c):(d+f+c+c+e)] = 207    # Green
V[0:h1, (d+f+c+c+e):(d+f+c+c+e+c)] = 817    # Magenta
V[0:h1, (d+f+c+c+e+c):(d+f+c+c+e+c+c)] = 848    # Red
V[0:h1, (d+f+c+c+e+c+c):(d+f+c+c+e+c+c+f)] = 481    # Blue
V[0:h1, (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 512    # 40% Gray

# pattern 2
h2 = int(b/12)
Y[h1:(h1+h2), 0:d] = 754   # 100% Cyan
Y[h1:(h1+h2), d:(d+f)] = 940   # 100% White
Y[h1:(h1+h2), (d+f):(d+f+c+c+e+c+c+f)] = 721   # 75% White
Y[h1:(h1+h2), (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 127   # 100% Blue

U[h1:(h1+h2), 0:d] = 615   # 100% Cyan
U[h1:(h1+h2), d:(d+f)] = 512   # 100% White
U[h1:(h1+h2), (d+f):(d+f+c+c+e+c+c+f)] = 512   # 75% White
U[h1:(h1+h2), (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 960   # 100% Blue

V[h1:(h1+h2), 0:d] = 64   # 100% Cyan
V[h1:(h1+h2), d:(d+f)] = 512   # 100% White
V[h1:(h1+h2), (d+f):(d+f+c+c+e+c+c+f)] = 512   # 75% White
V[h1:(h1+h2), (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 471   # 100% Blue

# pattern 3
h3 = h2
Y[(h1+h2):(h1+h2+h3), 0:d] = 877    # 100% Yellow
Y[(h1+h2):(h1+h2+h3), d:(d+f)] = 64
# Y-Ramp
Rwidth = c+c+e+c+c
step = (940 - 64) / Rwidth
for x in np.arange(Rwidth):
    Y[(h1+h2):(h1+h2+h3), (d+f) + x] = step * x + 64
Y[(h1+h2):(h1+h2+h3), (d+f+c+c+e+c+c):(d+f+c+c+e+c+c+f)] = 940
Y[(h1+h2):(h1+h2+h3), (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 250    # 100% Red

U[(h1+h2):(h1+h2+h3), 0:d] = 64    # 100% Yellow
U[(h1+h2):(h1+h2+h3), d:(d+f+c+c+e+c+c+f)] = 512   # Y-Ramp
U[(h1+h2):(h1+h2+h3), (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 409    # 100% Red

V[(h1+h2):(h1+h2+h3), 0:d] = 553    # 100% Yellow
V[(h1+h2):(h1+h2+h3), d:(d+f+c+c+e+c+c+f)] = 512   # Y-Ramp
V[(h1+h2):(h1+h2+h3), (d+f+c+c+e+c+c+f):(d+f+c+c+e+c+c+f+d)] = 960    # 100% Red

# pattern 4
h4 = int(b*3/12)
Y[(h1+h2+h3):(h1+h2+h3+h4), 0:d] = 195   # 15% Gray
Y[(h1+h2+h3):(h1+h2+h3+h4), d:(d+k)] = 64    # 0% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k):(d+k+g)] = 940   # 100% White
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g):(d+k+g+h)] = 64   # 0% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h):(d+k+g+h+i)] = 46    # -2% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h+i):(d+k+g+h+i+j)] = 64    # 0% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h+i+j):(d+k+g+h+i+j+i)] = 82    # +2% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h+i+j+i):(d+k+g+h+i+j+i+j)] = 64    # 0% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h+i+j+i+j):(d+k+g+h+i+j+i+j+i)] = 99    # +4% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h+i+j+i+j+i):(d+k+g+h+i+j+i+j+i+m)] = 64    # 0% Black
Y[(h1+h2+h3):(h1+h2+h3+h4), (d+k+g+h+i+j+i+j+i+m):(d+k+g+h+i+j+i+j+i+m+d)] = 195    # 15% Gray

U[(h1+h2+h3):(h1+h2+h3+h4),] = 512
V[(h1+h2+h3):(h1+h2+h3+h4),] = 512

path = 'std-b28_1920x1080_yuv444p10le.yuv'
YUV = np.stack([Y, U, V], 0)
YUV.tofile(path)
