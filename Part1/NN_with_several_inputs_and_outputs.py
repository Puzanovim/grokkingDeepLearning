weights = [
    [0.1, 0.1, -0.3],
    [0.1, 0.2, 0.0],
    [0.0, 1.3, 0.1]
]


def w_sum(a, b):
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


def vect_mat_mul(vect, matrix):
    output = [0, 0, 0]
    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix[i])

    return output


def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred


toes = [8.5, 9.5, 10, 9]
wlerc = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
input_data = [toes[0], wlerc[0], nfans[0]]

pred = neural_network(input_data, weights)

for i in range(len(pred)):
    print(pred[i])
