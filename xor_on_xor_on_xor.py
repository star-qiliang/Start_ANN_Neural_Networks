"""

I have a dataset of 4 features and 1 target.

x1, x2, x3, x4 -> y

xor(x1, xor(x2, xor(x3, x4))) = y

check if below dataset is correct

X = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],

    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],

    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],

    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
])

# True output or targets for the XOR problem
y = np.array([
    [0],
    [1],
    [1],
    [0],
    [1],
    [0],
    [0],
    [1],

    [1],
    [0],
    [0],
    [1],
    [0],
    [1],
    [1],
    [0]

])






"""