import numpy as np
import csv


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def cost_function(X, y, theta):
    m = len(y)
    h = sigmoid(X.dot(theta))
    cost = -1 / m * (y.dot(np.log(h)) + (1 - y).dot(np.log(1 - h)))
    return cost


def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    cost_history = []
    for _ in range(iterations):
        h = sigmoid(X.dot(theta))
        gradient = X.T.dot(h - y) / m
        theta -= alpha * gradient
        cost = cost_function(X, y, theta)
        cost_history.append(cost)
    return theta, cost_history


def predict(X, theta):
    return sigmoid(X.dot(theta))


def classify(probability, threshold=0.5):
    return 1 if probability >= threshold else 0


def main():
    with open("insurance_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        data = []


for row in reader:
    age = float(row[0])
    affordibility = float(row[1])
    bought_insurance = int(row[2])
    data.append([1, age, affordibility, bought_insurance])

data = np.array(data)

X = data[:, :3]
y = data[:, 3]

theta = np.zeros(3)
alpha = 0.01
iterations = 10000

theta, cost_history = gradient_descent(X, y, theta, alpha, iterations)

age_new = 60
affordability_new = 1
new_data = np.array([1, age_new, affordability_new])
probability = predict(new_data, theta)
prediction = classify(probability)

print(f"Probability of buying insurance: {probability}")

if prediction == 1:
    print("Prediction: Will buy insurance")
else:
    print("Prediction: Will not buy insurance")
if __name__ == "__main__":
    main()
