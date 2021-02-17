weights = 0.1


def neural_network(input, weight):
    prediction = input * weight
    return prediction


numbers_of_toes = [8.5, 9.5, 10, 9]
input_data = numbers_of_toes[0]
pred = neural_network(input_data, weights)
print(pred)
